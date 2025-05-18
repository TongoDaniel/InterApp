from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'homePage.html')
def login_register(request):
    return render(request, 'login_register.html')
def housingCL_view(request):
    return render(request, 'client/housingPage.html')

def landCL_view(request):
    return render(request, 'client/landPage.html')
def housingMore_view(request):
    return render(request, 'client/housingMore.html')