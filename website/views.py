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
        '1.6 Amplifiers'
    ]

    context['2. Digital Logic and Microprocessor'] = [
        '2.1 Digital logic',
        '2.2 Combinational and arithmetic circuits',
        '2.3 Sequential logic circuit',
        '2.4 Microprocessor',
        '2.5 Microprocessor system',
        '2.6 Interrupt operations'
    ]

    context['3. Programming Language and Its Applications'] = [
        '3.1 Introduction to C programming',
        '3.2 Pointers, structure and data files in C programming',
        '3.3 C++ language constructs with objects and classes',
        '3.4 Features of object-oriented programming',
        '3.5 Pure virtual function and file handling'
        '3.6 Generic programming and exception handling'
    ]

    context['4. Computer Organization and Embedded System'] = [
        '4.1 Control and central processing units',
        '4.2 Control and central processing units',
        '4.3 Input-Output organization and multiprocessor',
        '4.4 Hardware-Software design issues on embedded system',
        '4.5 Real-Time operating and control system',
        '4.6 Hardware descripts language and IC technology',
        
    ]

    context['5. Concept of Computer Network and Network Security System'] = [
        '5.1  Introduction to computer networks and physical layer',
        '5.2 Data link layer',
        '5.3 Network layer',
        '5.4 Transport layer',
        '5.5 Application layer',
        '5.6 Network security',
    ]

    context['6. Theory of Computation and Computer Graphics'] = [
        '6.1 Introduction to finite automata',
        '6.2 Introduction to context free language',
        '6.3 Turing machine',
        '6.4 Introduction of computer graphics',
        '6.5 Two-dimensional transformation',
        '6.6 Three-dimensional transformation'
    ]

    context['7. Data Structures and Algorithm, Database System and Operating System'] = [
        '7.1 Introduction to data structure, list, linked lists and trees',
        '7.2 Sorting, searching, and graphs',
        '7.3 Introduction to data models, normalization, and SQL',
        '7.4 Transaction processing, concurrency control and crash recovery',
        '7.5 Introduction to Operating System and process management',
        '7.6 Memory management, file systems and system administration',
    ]

    context['8. Software Engineering and Object-Oriented Analysis & Design'] = [
        '8.1 Software process and requirements',
        '8.2 Software design',
        '8.3 Software testing, cost estimation, quality management, and configuration management',
        '8.4 Object-oriented fundamentals and analysis',
        '8.5 Object-oriented design',
        '8.6 Object-oriented design implementation',
    ]

    context['9. Artificial Intelligence and Neural Network'] = [
        '9.1 Introduction to AI and intelligent agent',
        '9.2 Problem solving and searching techniques',
        '9.3 Knowledge representation',
        '9.4 Expert system and natural language processing',
        '9.5 Machine learning',
        '9.6  Neural networks',
    ]

    context['10. Project Planning, Design and Implementation'] = [
        '10.1 Engineering drawings and its concepts',
        '10.2 Engineering Economics',
        '10.3 Project planning and scheduling',
        '10.4 Project management',
        '10.5 Engineering professional practice',
        '10.6 Engineering Regulatory Body',
    ]
    course_name = Course.objects.get(name = "Nec")

    for category_name, subcategory_list in context.items():
        category, created = Category.objects.get_or_create(name=category_name, course=course_name)

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
    
    populate_subcategories()    
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
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user.is_superuser | False:
            login(request, user)
            return redirect("superuser")
        
        else:
            return redirect("slogin")
            # print('failed to login')

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
        # print(sub_category.name)
    except:
        print('subjected course not found')

    

    
    return render(request, template_path, {"context": context,"sub_category_details":sub_category,"course_name": course_name})

def course_detail(request,course_name = None,sub_category=None):
    template_path = 'course_details.html'
    print('category',course_name,sub_category)
    # context = {}
    sub_category = Sub_Category.objects.get(name=sub_category)
    print('sub_category',sub_category.name)
    # context['sub_category_detail'] = sub_category.details
    context = get_courses_category(course_name)
  
    
    return render(request, template_path, {"context": context,"sub_category_details":sub_category,"course_name": course_name})
