from rest_framework import serializers

from user_management.models import AuthUser


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, }


class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField(style={'placeholder': "Email or Phone Number"},
                                     help_text='Please enter your Email or Phone Number')
    password = serializers.CharField()


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['name', 'email', 'url_link', 'doc', ]


class UserRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(required=True)

    def validate_email(self, value):
        if AuthUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in used.")
        return value

    class Meta:
        exclude = ('password',)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        # fields = '__all__'

        exclude = ['password', 'is_staff', 'is_superuser', 'date_joined', ]
