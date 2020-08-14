from rest_framework_api_key.permissions import BaseHasAPIKey
from rest_framework.permissions import BasePermission
from apps.users.models import UserAPIKey


# Override rest_framework_api_key permissions with a custom UserAPIKey
class HasAPIKey(BaseHasAPIKey):
    model = UserAPIKey


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
