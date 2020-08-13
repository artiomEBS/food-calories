from django.urls import re_path
from apps.users import views

urlpatterns = [
    re_path(r'user/apikey/', views.APIKeyView.as_view(), name='user_register_new_user_apikey'),
    re_path(r'user/apikey/', views.APIKeyView.as_view(), name='user_revoke_and_get_new_apikey'),
    re_path(r'user/apikey/', views.APIKeyView.as_view(), name='user_revoke_apikey'),
    re_path(r'user/full/', views.FullUserView.as_view(), name='user_get_full_info'),
    re_path(r'user/full/', views.FullUserView.as_view(), name='user_update_full_info'),
    re_path(r'user/detail/', views.DetailUserView.as_view(), name='user_get'),
    re_path(r'user/detail/', views.DetailUserView.as_view(), name='user_update'),
    re_path(r'user/profile/', views.DetailProfileView.as_view(), name='user_get_profile'),
    re_path(r'user/profile/', views.DetailProfileView.as_view(), name='user_update_profile'),
    re_path(r'user/target/', views.DetailTargetView.as_view(), name='user_get_target'),
    re_path(r'user/target/', views.DetailTargetView.as_view(), name='user_update_target'),
    re_path(r'user/close/', views.DetailUserView.as_view(), name='user_close_account'),
]
