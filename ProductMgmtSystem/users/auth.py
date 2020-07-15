from django.contrib.auth.backends import ModelBackend


class UserAuthenticationBackend(ModelBackend):

    from django.contrib.auth import get_user_model

    user_model = get_user_model()

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = self.user_model.objects.get(username=username)
        except self.user_model.DoesNotExist:
            return None
        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            user = self.user_model.objects.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None

