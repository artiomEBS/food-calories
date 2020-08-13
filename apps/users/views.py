from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.common.permissions import HasAPIKey
from apps.users.models import Profile, Target, UserAPIKey
from apps.users.serializers import (UserSerializer,
                                    UserFullSerializer,
                                    UserPUTSerializer,
                                    UserCreateSerializer,
                                    ProfileSerializer,
                                    ProfilePUTSerializer,
                                    SWAGGERProfilePUTSerializer,
                                    TargetSerializer,
                                    TargetPUTSerializer,
                                    SWAGGERTargetPUTSerializer)
from rest_framework.response import Response
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from apps.common.apikey import get_api_key


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
        api_key = get_api_key(request)
        revoke = api_key.revoke()
        api_key, key = UserAPIKey.objects.create_key(user=api_key.user, name="generic-user-apikey")
        return Response(
            f"{revoke} The new APIkey is: {key}"
        )

    @swagger_auto_schema(operation_description=operation_delete)
    def delete(self, request):
        api_key = get_api_key(request)
        revoke = api_key.revoke()
        return Response(revoke)


class FullUserView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = UserFullSerializer

    operation_get = "Base full info overview of the user/profile/targets."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        api_key = get_api_key(request)
        serializer = UserFullSerializer(api_key.user)
        return Response(serializer.data)


class DetailUserView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = UserSerializer

    operation_get = "User object info overview."
    operation_put = "Update user info, all fields are optional."
    operation_delete = "Close current account."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        api_key = get_api_key(request)
        serializer = UserSerializer(api_key.user)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserPUTSerializer, operation_description=operation_put)
    def put(self, request):
        api_key = get_api_key(request)
        serializer = UserPUTSerializer(api_key.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description=operation_delete)
    def delete(self, request):
        api_key = get_api_key(request)
        user = api_key.user
        api_key.revoke()
        user.is_active = False
        user.save()
        return Response("Your account has been diabled.")


class DetailProfileView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = ProfileSerializer

    operation_get = "Profile object info overview."
    operation_put = "Update user profile info, all fields are optional."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        api_key = get_api_key(request)
        profile = Profile.objects.get(user=api_key.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SWAGGERProfilePUTSerializer, qoperation_description=operation_put)
    def put(self, request):
        api_key = get_api_key(request)
        profile = Profile.objects.get(user=api_key.user)
        serializer = ProfilePUTSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailTargetView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = TargetSerializer

    operation_get = "Target object info overview."
    operation_put = "Update target info, all fields are optional."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        api_key = get_api_key(request)
        target = Target.objects.get(user=api_key.user)
        serializer = TargetSerializer(target)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SWAGGERTargetPUTSerializer, operation_description=operation_put)
    def put(self, request):
        api_key = get_api_key(request)
        target = Target.objects.get(user=api_key.user)
        serializer = TargetPUTSerializer(target, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
