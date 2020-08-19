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
                                    SWAGGERTargetPUTSerializer,
                                    UserRecoverSerializer)
from rest_framework.response import Response
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from apps.common.tasks import mail_sender


class APIKeyView(APIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    operation_post = "Create a user/profile and grant a new APIKey, returned with the response body only a single time."

    @swagger_auto_schema(request_body=UserCreateSerializer, operation_description=operation_post)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            new_user = User.objects.create(
                username=username
            )
            if "@" in username:
                new_user.email = username
                new_user.save()
            Profile.objects.create(user=new_user)
            Target.objects.create(user=new_user)
            api_key, key = UserAPIKey.objects.create_key(user=new_user, name="generic-user-apikey")
            return Response({
                "message": f"Please store it somewhere safe: you will not be able to see it again.",
                "api_key": f"{key}"
            })
        return Response(serializer.errors)


class APIKeyDetailView(APIView):
    serializer_class = UserSerializer
    permission_classes = (HasAPIKey,)

    operation_put = "Revoke current APIKey and grant a new one."
    operation_delete = "Revoke APIKey access to the current user."

    @swagger_auto_schema(operation_description=operation_put)
    def put(self, request):
        api_key = request.apikey
        revoke = api_key.revoke()
        api_key, key = UserAPIKey.objects.create_key(user=request.user, name="generic-user-apikey")
        return Response({
            "message": f"{revoke}",
            "api_key": f"{key}"
        })

    @swagger_auto_schema(operation_description=operation_delete)
    def delete(self, request):
        api_key = request.apikey
        revoke = api_key.revoke()
        return Response(revoke)


class FullUserView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = UserFullSerializer

    operation_get = "Base full info overview of the user/profile/targets."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        serializer = UserFullSerializer(request.user)
        return Response(serializer.data)


class DetailUserView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = UserSerializer

    operation_get = "User object info overview."
    operation_put = "Update user info, all fields are optional."
    operation_delete = "Close current account."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserPUTSerializer, operation_description=operation_put)
    def put(self, request):
        serializer = UserPUTSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description=operation_delete)
    def delete(self, request):
        api_key = request.apikey
        user = request.user
        api_key.revoke()
        user.is_active = False
        user.save()
        return Response({"message": "Your account has been disabled."})


class DetailProfileView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = ProfileSerializer

    operation_get = "Profile object info overview."
    operation_put = "Update user profile info, all fields are optional."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SWAGGERProfilePUTSerializer, qoperation_description=operation_put)
    def put(self, request):
        profile = Profile.objects.get(user=request.user)
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
        target = Target.objects.get(user=request.user)
        serializer = TargetSerializer(target)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SWAGGERTargetPUTSerializer, operation_description=operation_put)
    def put(self, request):
        target = Target.objects.get(user=request.user)
        serializer = TargetPUTSerializer(target, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecoverAccessView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRecoverSerializer

    operation_post = "Recover user access, granting new APIKey."

    @swagger_auto_schema(request_body=UserRecoverSerializer, operation_description=operation_post)
    def post(self, request):
        serializer = UserRecoverSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            user = User.objects.get(username=username)
            api_key, key = UserAPIKey.objects.create_key(user=user, name="recovered-user-apikey")
            text = f"Please store it somewhere safe: you will not be able to see it again. The APIkey is: {key}"
            if user.email:
                mail_sender(user, text)
                return Response({"message": "You will receive a new APIKey on your email shortly."})
            return Response({
                "message": f"Please store it somewhere safe: you will not be able to see it again.",
                "api_key": f"{key}"
            })
        return Response(serializer.errors)
