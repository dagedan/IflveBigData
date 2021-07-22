from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password
from django.forms.utils import ErrorDict
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.db import DatabaseError
from apps.users.forms import RegisterForm, LoginForm
from .models import User


class RegisterView(View):
	def get(self, request):
		return render(request, 'register.html')

	def post(self, request):
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			mobile = request.POST.get('mobile')
			password = request.POST.get('password')
			invitationCode = request.POST.get('invitationCode')
			try:
				user = User.objects.create_user(username=mobile, mobile=mobile, password=password, invitationCode=invitationCode)
			except DatabaseError as e:
				return render(request, 'register.html', {'error', '注册失败-1'})
			login(request, user)
			# return redirect(reverse('contents:index'))
			return JsonResponse({'success': 1, 'msg': '注册成功', 'data': None})
		else:
			content = {
				'errors': register_form.errors.get_json_data(),
			}
			return JsonResponse(content)

	def is_unique(self, request):
		pass


class UsernameCountView(View):
	def get(self, request, username):
		count = User.objects.filter(username=username).count()
		msg = '用户已被注册' if count == 1 else None
		return JsonResponse({'success': 1, 'msg': msg, 'data': count})

	def post(self, request):
		pass


class LoginView(View):
	"""用户登录"""

	def get(self, request):
		return render(request, 'login.html')

	def post(self, request):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			if not all([username, password]):
				return HttpResponseForbidden('缺少登陆参数')
			user = authenticate(username=username, password=password)
			if user is None:
				return JsonResponse(data={'register_err_msg': '用户名或密码错误'}, content_type="application/json")
			login(request, user)
			# 状态保持默认为2周， 0：则关闭浏览器结束会话
			request.session.set_expiry(None)
			return JsonResponse(data={'success': 1, 'register_err_msg': '登陆成功'}, content_type="application/json")
		else:
			content = {
				'form_errors': login_form.errors
			}
			return render(request, 'login.html', context=content)