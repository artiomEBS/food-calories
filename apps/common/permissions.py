from rest_framework_api_key.permissions import BaseHasAPIKey
from apps.users.models import UserAPIKey


# Override rest_framework_api_key permissions with a custom UserAPIKey
class HasAPIKey(BaseHasAPIKey):
    model = UserAPIKey
