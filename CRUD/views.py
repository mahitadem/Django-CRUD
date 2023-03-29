from django.shortcuts import render

def Home(request):
    return render(request,'index.html')
def Edit(request):
    return render(request,'edit.html')
def Login(request):
    return render(request,'login.html')
def Sign(request):
    return render(request,'signup.html')