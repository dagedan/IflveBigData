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
