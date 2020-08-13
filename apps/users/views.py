from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.common.permissions import HasAPIKey
from apps.users.models import Profile, Target, UserAPIKey
from apps.users.serializers import UserSerializer, UserCreateSerializer, ProfileSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema


class APIKeyView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    operation_post = "Create a user/profile and grant a new APIKey, returned with the response body only a single time."
    operation_put = "Revoke current APIKey and grant a new one."
    operation_delete = "Revoke APIKey access to the current user."

    @swagger_auto_schema(request_body=UserCreateSerializer, operation_description=operation_post)
    def post(self, request):

        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            new_user = User.objects.create(
                username=serializer.validated_data['username']
            )
            Profile.objects.create(user=new_user)
            Target.objects.create(user=new_user)
            api_key, key = UserAPIKey.objects.create_key(user=new_user, name="generic-user-apikey")
            return Response(
                f"Please store it somewhere safe: you will not be able to see it again. The APIkey is: {key}"
            )
        return Response(serializer.errors)

    @swagger_auto_schema(operation_description=operation_put)
    def put(self, request):
        key = request.META['HTTP_X_API_KEY']
        api_key = UserAPIKey.objects.get_from_key(key)
        revoke = api_key.revoke()
        api_key, key = UserAPIKey.objects.create_key(user=api_key.user, name="generic-user-apikey")
        return Response(
            f"{revoke} The new APIkey is: {key}"
        )

    @swagger_auto_schema(operation_description=operation_delete)
    def delete(self, request):
        key = request.META['HTTP_X_API_KEY']
        api_key = UserAPIKey.objects.get_from_key(key)
        revoke = api_key.revoke()
        return Response(revoke)


class FullUserView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = UserSerializer

    operation_get = "Base full info overview of the user/profile/targets."
    operation_put = "Update full info, all fields are optional."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        key = request.META['HTTP_X_API_KEY']
        api_key = UserAPIKey.objects.get_from_key(key)
        serializer = UserSerializer(api_key.user)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description=operation_put)
    def put(self, request):
        key = request.META['HTTP_X_API_KEY']
        api_key = UserAPIKey.objects.get_from_key(key)
        pass


class DetailUserView(APIView):
    pass


class DetailProfileView(APIView):
    pass


class DetailTargetView(APIView):
    pass