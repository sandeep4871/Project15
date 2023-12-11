from django.shortcuts import render
from django.views import View
from .forms import RegForm,LoginForm
from .models import RegModel
from django.http import HttpResponse
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        con_dict={"rf": RegForm()}
        return render(request,'reginput.html',context=con_dict)
class Register(View):
    def post(self,request):
        rf1=RegForm(request.POST)
        if rf1.is_valid():
            rm=RegModel(FirstName=rf1.cleaned_data["FirstName"],
                        LastName=rf1.cleaned_data["LastName"],
                        UserName=rf1.cleaned_data["UserName"],
                        Password=rf1.cleaned_data["Password"],
                        Cpassword=rf1.cleaned_data["Cpassword"],
                        Emailid=rf1.cleaned_data["Emailid"],
                        MobileNo=rf1.cleaned_data["MobileNo"])
            rm.save()
        return HttpResponse("Registration success")
class LoginInput(View):
    def get(self,request):
        con_dict={"lf": LoginForm()}
        return render(request,'loginput.html',context=con_dict)
class Login(View):
    def post(self,request):
        lf1=LoginForm(request.POST)
        if lf1.is_valid():
            qs=RegModel.objects.filter(UserName=lf1.cleaned_data["UserName"],
                                       Password=lf1.cleaned_data["Password"])
            if qs:
                return HttpResponse("login success")
            else:
                return HttpResponse("login failed")