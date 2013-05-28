from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from django_countries.countries import COUNTRIES

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)

	email = forms.EmailField()
	confirm_email = forms.EmailField()

	country = forms.ChoiceField(choices=COUNTRIES)

	class Meta:
		model = User
		fields = ['username', 'password', 'confirm_password', 'email', 'confirm_email', 'first_name', 'last_name']		

	def clean(self):
		email = self.cleaned_data.get('email')
		confirm_email= self.cleaned_data.get('confirm_email')
		
		if email and confirm_email and email != confirm_email:
			raise forms.ValidationError('Emails do not match.')

		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		
		if password and confirm_password and password != confirm_password:
			raise forms.ValidationError('Passwords do not match.')

		self.cleaned_data['password'] = make_password(self.cleaned_data.get('password'))

		return self.cleaned_data