from django.urls import re_path
from apps.users import views

urlpatterns = [
    re_path(r'apikey/new/', views.APIKeyView.as_view(), name='user_register_new_user_apikey'),
    re_path(r'apikey/update/', views.APIKeyDetailView.as_view(), name='user_revoke_and_get_new_apikey'),
    re_path(r'apikey/update/', views.APIKeyDetailView.as_view(), name='user_revoke_apikey'),
    re_path(r'full/', views.FullUserView.as_view(), name='user_get_full_info'),
    re_path(r'full/', views.FullUserView.as_view(), name='user_update_full_info'),
    re_path(r'detail/', views.DetailUserView.as_view(), name='user_get'),
    re_path(r'detail/', views.DetailUserView.as_view(), name='user_update'),
    re_path(r'detail/', views.DetailUserView.as_view(), name='user_close_account'),
    re_path(r'profile/', views.DetailProfileView.as_view(), name='user_get_profile'),
    re_path(r'profile/', views.DetailProfileView.as_view(), name='user_update_profile'),
    re_path(r'target/', views.DetailTargetView.as_view(), name='user_get_target'),
    re_path(r'target/', views.DetailTargetView.as_view(), name='user_update_target'),
    re_path(r'recovery/', views.RecoverAccessView.as_view(), name='user_recover_access'),
]
