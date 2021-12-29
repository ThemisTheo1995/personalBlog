from django.urls import path
from .views import SignUpView, UpdateUserView

app_name = "account"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user-details/', UpdateUserView.as_view(), name='update-user'),
]