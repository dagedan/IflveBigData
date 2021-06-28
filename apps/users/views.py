from django.contrib.auth import login
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.db import DatabaseError
from apps.users.forms import RegisterForm
from .models import User


class RegisterView(View):
	def get(self, request):
		return render(request, 'register.html')

	def post(self, request):
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			mobile = request.POST.get('mobile')
			password = request.POST.get('password')
			# repeatPassword = request.POST.get('repeatPassword')
			# invitationCode = request.POST.get('invitationCode')
			try:
				user = User.objects.create_user(username=mobile, mobile=mobile, password=password)
			except DatabaseError as e:
				return render(request, 'register.html', {'error', '注册失败-1'})
			login(request, user)
			return redirect(reverse('contents:index'))
			# return redirect(reverse('users:login'))
		else:
			content = {
				'forms_errors': register_form.errors
			}
			return render(request, 'register.html', content=content)

	def is_unique(self, request):
		pass


class UsernameCountView(View):

	def get(self, request, username):
		count = User.objects.filter(username=username).count()
		return JsonResponse({'code': 200, 'err_msg': 'ok', 'count': count})

	def post(self, request):
		pass


class LoginView(View):
	"""用户登录"""

	def get(self, request):
		return render(request, 'login.html')

	def post(self, request):
		# username = request.POST.get('username')
		# password = request.POST.get('password')
		try:
			pass
		except DatabaseError:
			return JsonResponse(data={'register_err_msg': '登录失败'}, content_type="application/json")
		return redirect(reverse('contents:index'))
