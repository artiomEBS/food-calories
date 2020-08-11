from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.common.permissions import HasAPIKey
from apps.users.models import Profile, Target, UserAPIKey
from apps.users.serializers import UserSerializer, UserCreateSerializer, ProfileSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema


class GenerateApikey(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = User.objects.create(
                username=serializer.validated_data['username']
            )
            Profile.objects.create(user=new_user)
            Target.objects.create(user=new_user)
            api_key, key = UserAPIKey.objects.create_key(user=new_user, name="generic-user-apikey")
            return Response(
                f"Please store it somewhere safe: you will not be able to see it again. The API key is: {key}"
            )


class ProfileListView(APIView):
    permission_classes = (HasAPIKey,)
    serializer_class = UserSerializer

    def get(self, request):
        key = request.META['HTTP_X_API_KEY']
        api_key = UserAPIKey.objects.get_from_key(key)
        serializer = UserSerializer(api_key.user)
        return Response(serializer.data)
