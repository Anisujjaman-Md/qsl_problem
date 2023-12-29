import jwt
from rest_framework import status, viewsets
from .authentication import JWTAuthentication
from .models import AuthUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings
from rest_framework import exceptions
from .serializers import ObtainTokenSerializer, UserLoginSerializer, RefreshTokenSerializer, UserRegistrationSerializer, \
    UpdateUserSerializer, UserListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')

            user = AuthUser.objects.get(email=email).first()
            if user is None:
                return Response({"path": "Login", "message": "Username and Password Wrong"},
                                status=status.HTTP_400_BAD_REQUEST)
            if user is None or not user.check_password(password):
                return Response({"path": "Login", "message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

            access_token = JWTAuthentication.generate_access_token(user)
            refresh_token = JWTAuthentication.generate_refresh_token(user)
            user_serializer = UserLoginSerializer(user)
            token = {
                "user": user_serializer.data,
                'access_token': access_token,
                'refresh_token': refresh_token,
            }
            return Response(token, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Unauthorized",
                "timestamp": timestamp,
            }, status=status.HTTP_400_BAD_REQUEST)


class CustomRefreshTokenAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RefreshTokenSerializer

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')

            if not refresh_token:
                return Response({"path": "Refresh Token", "message": "Refresh token is required."},
                                status=status.HTTP_401_UNAUTHORIZED)
            try:
                payload = jwt.decode(
                    refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                dict_response = {
                    "message": "Unauthorized",
                    "timestamp": timestamp,
                    "details": {
                        "path": "Refresh Token",
                        "message": "expired refresh token, please login again."
                    }
                }
                raise exceptions.AuthenticationFailed(dict_response)

            user = AuthUser.objects.filter(email=payload.get('user_identifier')).first()
            if user is None:
                dict_response = {
                    "message": "Unauthorized",
                    "timestamp": timestamp,
                    "details": {
                        "path": "User",
                        "message": "User not found"
                    }
                }
                raise exceptions.AuthenticationFailed(dict_response)

            access_token = JWTAuthentication.generate_access_token(user)
            refresh_token = JWTAuthentication.generate_refresh_token(user)
            user_serializer = UserLoginSerializer(user)

            token = {
                "user": user_serializer,
                'access_token': access_token,
                'refresh_token': refresh_token,
            }
            return Response(token, status=status.HTTP_200_OK)


        except Exception as e:

            return Response({

                "message": "Unauthorized",

                "timestamp": timestamp,

            }, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializers_class = UserRegistrationSerializer

    def create(self, request):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            password = serializer.validated_data['password']
            confirm_password = serializer.validated_data['confirm_password']
            if password != confirm_password:
                return Response({"message": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)
            user = AuthUser.objects.create_user(
                name=serializer.validated_data['name'],
                email=serializer.validated_data['email'],
                password=password,
            )
            user.save()
            user_data = serializer.data.copy()
            user_data.pop('password', None)
            user_data.pop('confirm_password', None)

            return Response(user_data, status=status.HTTP_200_OK)

        except Exception as e:

            return Response({

                "message": "Failed",

                "timestamp": timestamp,

            }, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetailViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            user = AuthUser.objects.get(phone_number=self.request.user)
            serializer = UserLoginSerializer(user, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:

            return Response({

                "message": "Failed",

                "timestamp": timestamp,

            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            user = AuthUser.objects.get(uuid=pk)
            serializer = UpdateUserSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(200, "User details Updated", serializer.data)
        except Exception as e:
            return Response({

                "message": "Failed",

                "timestamp": timestamp,

            }, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = UserListSerializer
