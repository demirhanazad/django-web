from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
def giris(request):
    if request.user.is_authenticated:
        return redirect("home")
    context={
        "active_page":"login",
             }
    if request.method == "POST":
        username=request.POST["username"]
        password= request.POST["password"]
        
        kullanıcı = authenticate(request,username=username,password=password)
        
        if username and password :
            if kullanıcı is not None:
                login(request,kullanıcı)
                return redirect("home")
            else:
                return render(request,"hesaplar/login.html",{"error":"parola yanlış",})
        else:
            return render(request,"hesaplar/login.html",{"error":"boş alanları doldurunuz",})
    return render(request,"hesaplar/login.html",context)
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    context={
        "active_page":"register",
             }
    if request.method == "POST":
        name=request.POST["firstname"]
        lastname=request.POST["lastname"]
        username=request.POST["username"]
        gmail=request.POST["gmail"]
        password= request.POST["password"]
        repassword=request.POST["repassword"]
        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"hesaplar/register.html",
                {
                    "error":"Bu Kullanıcı Adı Daha Önce Alınmış",
                    "name":name,
                    "lastname":lastname,
                    "gmail":gmail,
                    "password":password,
                    "repassword":repassword,
                })
            else:
                if User.objects.filter(email=gmail).exists():
                    return render(request,"hesaplar/register.html",
                    {
                        "error":"gmail kullanılıyor",
                        "name":name,
                        "lastname":lastname,
                        "username":username,
                        "password":password,
                        "repassword":repassword,
                    })
                else:
                    if password and repassword:
                        user= User.objects.create_user(first_name=name,last_name=lastname, username=username, email=gmail, password=password)
                        user.save()
                        kullanıcı = authenticate(request,username=username,password=password)
                        if kullanıcı is not None:
                            login(request,kullanıcı)
                            return redirect("home")
                    else:
                        return render(request,"hesaplar/register.html",
                        {
                            "error":"password is emty",
                            "name":name,
                            "lastname":lastname,
                            "username":username,
                            "gmail":gmail,
                        })
        else:
            return render(request,"hesaplar/register.html",
            {
                "error":"incorrect password",
                "name":name,
                "lastname":lastname,
                "username":username,
                "gmail":gmail,
            })
    return render(request,"hesaplar/register.html",context)
def logout_request(request):
    logout(request)
    context={
        "active_page":"firstpage",
             }
    return render(request,"hesaplar/firstpage.html",context)
