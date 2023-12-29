from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required,user_passes_test



# Create your views here.
def home(request):
    template_path = 'home.html'
    context = {}
    
    return render(request, template_path, context)

    
@login_required(login_url='slogin')
def superuser(request):
    template_path = 'superuser/index.html'
    # template_path = 'index.html'
    # context = {}

    # return render(request, template_path, context)
    return render(request, template_path)

def superuser_login(request):
    template_path = 'superuser/superuser_login.html'
    context = {}
    
    if request.user.is_authenticated:
         return redirect("superuser")

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user.is_superuser | False:
            login(request, user)
            return redirect("superuser")
        
        else:
            return redirect("slogin")
            print('failed to login')

    return render(request, template_path, context)

def superuser_logout(request):
    logout(request)
    return redirect("slogin")

def course(request,course_name):
    template_path = 'index.html'
    context = {}
    
    # Query all categories and their related sub-categories
    categories = Category.objects.filter(course__name=course_name)
    
    sub_categories = Sub_Category.objects.all()
    # Loop through each category and retrieve its related sub-categories
    for category in categories:
        subcategories = Sub_Category.objects.filter(category=category)
        subcategory_list = [{'name': sub.name, 'more_sub': sub.more_sub, 'details': sub.details} for sub in subcategories]
        
        # Add the category and its subcategories to the dictionary
        context[category.name] = subcategory_list
        
    print(context)
        
    return render(request, template_path, {"context": context})

    
    
