from django.shortcuts import render
from djoser import utils
from djoser.conf import settings

# Create your views here.
from djoser.utils import login_user
from djoser.views import UserViewSet
from rest_framework import status, generics, views
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response



class TokenCreateView(utils.ActionViewMixin, generics.GenericAPIView):
    serializer_class = settings.SERIALIZERS.token_create
    permission_classes = settings.PERMISSIONS.token_create

    def _action(self, serializer):
        token = login_user(self.request, serializer.user)
        token_serializer_class = settings.SERIALIZERS.token
        return Response(
            {
                'message': 'User login successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': {
                    'count': 1,
                    'results': token_serializer_class(token).data
                }
            },
            status=status.HTTP_200_OK
        )


class TokenDestroyView(views.APIView):
    """
    Use this endpoint to logout user (remove user authentication token).

    **Example response**:


        {
            'message': 'User logout successfully',
            'success': true,
            'status': 200,
            'data': []
        }

    """

    permission_classes = settings.PERMISSIONS.token_destroy

    def post(self, request):
        utils.logout_user(request)
        return Response(
            {
                'message': 'User logout successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': []
            },
            status=status.HTTP_200_OK
        )
    #
    # def get_exception_handler(self):
    #     """
    #     Returns the exception handler that this view uses.
    #     """
    #     return ca_custom_exception_handler


class UsersViewSet(UserViewSet):
    parser_classes = [JSONParser, MultiPartParser, ]
    """
    Customized User ModelViewSet to accommodate customized response format

    **Example response**:


        {
            'message': 'Display message here',
            'success': true,
            'status': 200,
            'data': [
                'count': int,
                'results': {
                    'key': 'value',
                    'key': 'value',
                }
            ]
        }

    """

    def create(self, request, *args, **kwargs):
        """
        Customized response with message

        ** Response **:

            {
                "message": "User created successfully",
                "success": true,
                "status": 200,
                "data": {
                    "count": 1,
                    "results": {
                        "email": "dummy",
                        "username": "dummy",
                        "id": 999
                    }
                }
            }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'User created successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': {
                    'count': 1,
                    'results': serializer.data
                }
            },
            status=status.HTTP_200_OK,
            headers=headers
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        # if request.user.is_client:
        #     data.update(get_client_permissions())
        # if request.user.is_tenant:
        #     tenant = request.user.tenant
        #     if tenant.is_root:
        #         data.update(get_root_tenant_permissions())
        #     else:
        #         data.update(get_tenant_permissions())

        return Response(
            {
                'message': 'User profile details',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': {
                    'count': 1,
                    'results': data
                }
            },
            status=status.HTTP_200_OK,
        )
