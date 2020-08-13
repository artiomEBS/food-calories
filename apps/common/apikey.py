from apps.users.models import UserAPIKey


def get_api_key(request):
    key = request.META['HTTP_X_API_KEY']
    api_key = UserAPIKey.objects.get_from_key(key)
    return api_key
