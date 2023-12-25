from rest_framework import serializers

class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField(style={'placeholder': "Email or Phone Number"},
                                     help_text='Please enter your Email or Phone Number')
    password = serializers.CharField()
