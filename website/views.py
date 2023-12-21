from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.
def home(request):
    template_path = 'index.html'
    context = {}
    
    return render(request, template_path, context)

    

def admin_page(request):
    template_path = 'superuser/index.html'
    # template_path = 'index.html'
    context = {}

    # founder_data = BasicInfo.objects.all().first()
    # print('hello',founder_data.founder_image)
    # context["founder_data"] = founder_data

    # # homepage_button_data = HomepageButton.objects.all().first()
    # context["button_data"] = homepage_button_data

    # # testimonials_data = Testimonials.objects.all()
    # context["testimonials_data"] = testimonials_data

    # # resources_data = HomeResource.objects.all()
    # context["resources"] = resources_data

    # # Social Media Urls
    # # socials = Socials.objects.all().first()
    # context["socials"] = socials

    return render(request, template_path, context)
    # return render(request, template_path)

def superuser_login(request):
    template_path = 'superuser/superuser_login.html'
    context = {}
    
    if request.user.is_authenticated:
         return redirect("admin_page")

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user.is_superuser | False:
            login(request, user)
            return redirect("admin_page")
        
        else:
            print('failed to login')

    return render(request, template_path, context)

def superuser_logout(request):
    logout(request)
    return redirect("superuser_login")
