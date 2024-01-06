from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .utils import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required,user_passes_test



# Create your views here.
def home(request):
    template_path = 'index.html'
    context = {}
    
    
    
    return render(request, template_path, context)

def populate_subcategories():
    context = {}
    context['1. Concept of Basic Electrical and Electronics Engineering'] = [
        '1.1 Basic concept',
        '1.2 Network theorems',
        '1.3 Alternating current fundamentals',
        '1.4 Semiconductor devices',
        '1.5 Signal generator',
        '1.6 Amplifiers:',
    ]

    for category_name, subcategory_list in context.items():
        category, created = Category.objects.get_or_create(name=category_name)

        for subcategory_name in subcategory_list:
            subcategory, sub_created = Sub_Category.objects.get_or_create(
                category=category,
                name=subcategory_name,
                defaults={'more_sub': '', 'details': ''}
            )
            if sub_created:
                print(f"Created Sub-Category: {subcategory.name} for Category: {category.name}")
            else:
                print(f"Sub-Category: {subcategory.name} already exists for Category: {category.name}")

def feed(request):
    template_path = 'index.html'
    context = {}
    # print('heelo')
    # context['1. Concept of Basic Electrical and Electronics Engineering'] = ['1.1 Basic concept',
    #                                                                          '1.2 Network theorems',
    #                                                                          '1.3 Alternating current fundamentals',
    #                                                                          '1.4 Semiconductor devices',
    #                                                                          '1.5 Signal generator',
    #                                                                          '1.6 Amplifiers:',
    #                                                                          ]
    
    # # print(context.keys())
    # category = Category.objects.get(name=list(context.keys())[0])
    populate_subcategories()
    # print(category.name)
    
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
    template_path = 'course_details.html'
    # context = {}
    print('coursename', course_name,type(course_name))
    
    # --------# side bar-----
    context = get_courses_category(course_name)
    # context['course_name'] = course_name
    
    try:
        
        sub_category = Sub_Category.objects.filter(category__course__name=course_name).first()
        # sub_category = Sub_Category.objects.get(category__course__name=course_name).first()
        print(sub_category.name)
    except:
        print('subjected course not found')

    

    
    return render(request, template_path, {"context": context,"sub_category_details":sub_category,"course_name": course_name})

def course_detail(request,course_name = None,sub_category=None):
    template_path = 'course_details.html'
    print('category',course_name,sub_category)
    # context = {}
    sub_category = Sub_Category.objects.get(name=sub_category)
    # context['sub_category_detail'] = sub_category.details
    context = get_courses_category(course_name)
  
    
    return render(request, template_path, {"context": context,"sub_category_details":sub_category,"course_name": course_name})
