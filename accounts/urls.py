from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    # register user
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),

    # change user password
    path("password_change/", views.CustomPasswordChangeView.as_view(), name="change_password"),
    path("password_change/done/", views.CustomPasswordChangeDone.as_view(), name="password_change_done"),

    # reset user password
    path("password_reset/", views.CustomPasswordResetView.as_view(), name="password_reset"),

    path("password_reset/done/", views.CustomPasswordResetDone.as_view(), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", views.CustomPasswordResetConfirm.as_view(), name="password_reset_confirm"),

    path("reset/done/", views.CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # logout user
    path("logout/", views.logout_user, name="logout"),

    # edit profile
    path('edit_profile/',views.EditProfileView.as_view(), name='edit_profile')
]
