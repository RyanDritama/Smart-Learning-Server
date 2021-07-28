from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from account.models import Account


from rest_framework.authtoken.views import ObtainAuthToken


@api_view(['POST'])
def registration_view(request):
	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['id'] = account.id
			data['nim'] = account.nim
			data['username'] = account.username
			data['nama'] = account.nama
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)
