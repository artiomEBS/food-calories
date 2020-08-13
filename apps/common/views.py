from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    permission_classes = (AllowAny,)

    operation_get = "SWAGGER Groups Test view."

    @swagger_auto_schema(operation_description=operation_get)
    def get(self, request):
        return Response('test endpoint')
