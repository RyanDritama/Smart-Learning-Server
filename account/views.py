from django.shortcuts import render
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from account.models import Account
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import datetime
import pytz


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        utc_now = datetime.datetime.utcnow()
        utc_now = utc_now.replace(tzinfo = pytz.utc)
        result = Token.objects.filter(user = user, created__lt = utc_now - datetime.timedelta(seconds=30)).delete()

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'nama': user.nama,
            'nim' : user.nim
        })
# Create your views here.
