from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from .utils import TokenGenerator, generate_token
# from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.views.generic import View
# Create your views here.
def signup(request):
    if request.method=="POST":
        Email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            messages.warning(request,'password is not matching')
            return redirect('signup')
        try:
            if User.objects.get(username=Email):
                messages.warning(request, "An account already exists..")
                return redirect('signup')              
        
        except Exception as identifier:
            pass
        user=User.objects.create_user(Email,Email,password)
        user.save()
        messages.success(request,'You have successfully registered')
        # email_subject="Acticate your Account"
        # message=render_to_string('auth/activate.html',{
        #     'user':user,
        #     'domain':'127.0.0.1:8000',
        #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token':generate_token.make_token(user)
        # })
        # email_message = EmailMessage(
        # email_subject,
        # message,
        # settings.EMAIL_HOST_USER,[Email])
        # email_message.send()
        # messages.success(request,'We have sent you verification Email, Please verify  your Account')
        # return redirect('Login')
    return render(request,'signup.html')

# class ActivateAccountView(View):
#     def get(self,request,uidb64,token):
#         try:
#             uid=force_str(urlsafe_base64_decode(uidb64))
#             user=User.objects.get(pk=uid)
#         except Exception as identifier:
#             user=None
#         if user is not None and generate_token.check_token(user,token):
#             user.is_active=True
#             user.save()
#             messages.success(request,'Account activated, please login')
#             return redirect('/auth/Login')
#         return render(request,'activatefail.html')
def handleLogin(request):
    if request.method=='POST':
        username=request.POST['email']
        psw=request.POST['password']
        myuser=authenticate(username=username, password=psw)
        if myuser is not None:
            login(request,myuser)
            return render(request, 'index.html')
        else:
            messages.info(request,'Invalid details')
    return render(request,'Login.html')

def handleLogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/auth/Login')

