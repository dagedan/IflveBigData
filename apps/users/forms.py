import re

from django import forms


class RegisterForm(forms.Form):
	mobile = forms.CharField(max_length=11, min_length=11, required=True)
	password = forms.CharField(min_length=6, max_length=18, required=True)
	repeatPassword = forms.CharField(min_length=6, max_length=18, required=True)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password = cleaned_data.get('password')
		repeatPassword = cleaned_data.get('repeatPassword')
		if password != repeatPassword:
			raise forms.ValidationError('两次输入的密码不一致')
		return cleaned_data


class LoginForm(forms.Form):
	username = forms.CharField(max_length=11, min_length=11, required=True)
	password = forms.CharField(min_length=6, max_length=18, required=True)

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		username = cleaned_data.get('username')
		if not re.match(r'^1[3-9]\d{9}$', str(username)):
			raise forms.ValidationError('只能用中国大陆的手机号登陆')
		return cleaned_data
