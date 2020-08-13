from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.core.exceptions import ObjectDoesNotExist


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, AuthenticationFailed):
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)

    if isinstance(exc, ObjectDoesNotExist):
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    return response
