from rest_framework import serializers

from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['nim', 'username', 'nama','password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					nim=self.validated_data['nim'],
					username=self.validated_data['username'],
					nama=self.validated_data['nama']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()
		return account

