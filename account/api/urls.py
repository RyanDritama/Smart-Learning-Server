from django.urls import path
from account.api.views import(
	registration_view,
)
from account.views import CustomAuthToken
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),
	path('login', CustomAuthToken.as_view(), name="login"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
