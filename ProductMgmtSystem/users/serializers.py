from django.contrib.auth import authenticate
from djoser.compat import get_user_email_field_name, get_user_email
from djoser.conf import settings
from rest_framework import serializers
from .models import User


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("auth_token",)


class CustomUserSerializer(serializers.ModelSerializer):
    # role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):

        email_field = get_user_email_field_name(User)
        if settings.SEND_ACTIVATION_EMAIL and email_field in validated_data:
            instance_email = get_user_email(instance)
            if instance_email != validated_data[email_field]:
                instance.is_active = False
                instance.save(update_fields=["is_active"])
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        """
        Changes profile image's absolute URLs to Relative path only
        """
        response = super(CustomUserSerializer, self).to_representation(instance)
        if instance.profile_image:
            response['profile_image'] = instance.profile_image.url

        return response


class TokenCreateSerializer(serializers.Serializer):
    password = serializers.CharField(required=False, style={"input_type": "password"})

    default_error_messages = {
        "invalid_credentials": "Given Credentials are invalid",
        "inactive_account": "Your account is inactive"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields[settings.LOGIN_FIELD] = serializers.CharField(required=False)

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(**params, password=password)
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user and self.user.is_active:
            return attrs
        self.fail("invalid_credentials")
