from wsgiref.util import request_uri
from django.shortcuts import render

# Create your views here.

def v_login(request):
  if request.method == 'post':
    txt_uname = request.get['txt_login_username']
    txt_pwd = request.get['pwd_login']

  else:
    code="Login"
    return render(request,'auth.html',{'code':code})

def v_signin(request):
  if request.method == 'post':
    txt_uname = request.get['txt_r_fname']
  else:
    code="Signin"
    return render(request,'auth.html',{'code':code})

