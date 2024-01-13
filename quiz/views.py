from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.db import transaction
from .models import QuesModel
from website.models import *

def populate_questions():
    # List of Nec MCQs (replace this with your own set of questions)
    computer_engineering_questions = [
    {
        'course': 'Nec',
        'question': 'What does CPU stand for?',
        'op1': 'Central Processing Unit',
        'op2': 'Central Process Unit',
        'op3': 'Computer Personal Unit',
        'op4': 'None of the above',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'Which one of these is not a programming language?',
        'op1': 'Python',
        'op2': 'Java',
        'op3': 'HTML',
        'op4': 'C++',
        'ans': 'option3'
    },
    {
        'course': 'Nec',
        'question': 'What is the binary equivalent of 15?',
        'op1': '1010',
        'op2': '1101',
        'op3': '1111',
        'op4': '1001',
        'ans': 'option3'
    },
    {
        'course': 'Nec',
        'question': 'Which type of memory is volatile?',
        'op1': 'RAM',
        'op2': 'ROM',
        'op3': 'Cache Memory',
        'op4': 'Hard Disk',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'What is the full form of HTML?',
        'op1': 'Hyper Text Markup Language',
        'op2': 'High Tech Markup Language',
        'op3': 'Hyperlink Text Markup Language',
        'op4': 'None of the above',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'Which sorting algorithm has the worst time complexity in most cases?',
        'op1': 'Bubble Sort',
        'op2': 'Quick Sort',
        'op3': 'Merge Sort',
        'op4': 'Insertion Sort',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'What is the purpose of an IP address?',
        'op1': 'To uniquely identify a device on a network',
        'op2': 'To identify the brand of a device',
        'op3': 'To determine the location of a device',
        'op4': 'To find the device owner',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'What is the purpose of a firewall?',
        'op1': 'To block unauthorized access to a network',
        'op2': 'To boost internet speed',
        'op3': 'To amplify Wi-Fi signals',
        'op4': 'To improve device performance',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'Which of the following is a high-level programming language?',
        'op1': 'Assembly language',
        'op2': 'Machine language',
        'op3': 'Python',
        'op4': 'Binary code',
        'ans': 'option3'
    },
    {
        'course': 'Nec',
        'question': 'What is the purpose of a compiler?',
        'op1': 'To convert high-level language to machine code',
        'op2': 'To execute code',
        'op3': 'To store data',
        'op4': 'To design user interfaces',
        'ans': 'option1'
    },
     {
        'course': 'Nec',
        'question': 'Which of the following is a hardware component?',
        'op1': 'Operating System',
        'op2': 'RAM',
        'op3': 'Compiler',
        'op4': 'Web Browser',
        'ans': 'option2'
    },
    {
        'course': 'Nec',
        'question': 'What does LAN stand for?',
        'op1': 'Large Area Network',
        'op2': 'Local Area Network',
        'op3': 'Long Antenna Network',
        'op4': 'Low-level Authentication Network',
        'ans': 'option2'
    },
    {
        'course': 'Nec',
        'question': 'What is the role of a router in a network?',
        'op1': 'To connect multiple networks and forward data packets',
        'op2': 'To protect against viruses',
        'op3': 'To manage power supply',
        'op4': 'To enhance the screen resolution',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'Which programming language is known as a "scripting language"?',
        'op1': 'C',
        'op2': 'Java',
        'op3': 'Python',
        'op4': 'C++',
        'ans': 'option3'
    },
    {
        'course': 'Nec',
        'question': 'What is the primary function of an operating system?',
        'op1': 'To manage hardware resources and provide services for application software',
        'op2': 'To create presentations',
        'op3': 'To perform complex mathematical calculations',
        'op4': 'To secure a network',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'Which of the following is NOT a type of computer memory?',
        'op1': 'RAM',
        'op2': 'ROM',
        'op3': 'CPU',
        'op4': 'Cache Memory',
        'ans': 'option3'
    },
    {
        'course': 'Nec',
        'question': 'What is the function of a compiler?',
        'op1': 'Translates high-level programming language into machine language',
        'op2': 'Manages memory allocation',
        'op3': 'Connects devices in a network',
        'op4': 'Performs calculations',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'Which of the following is an example of a secondary storage device?',
        'op1': 'RAM',
        'op2': 'CPU',
        'op3': 'Hard Disk Drive',
        'op4': 'Cache Memory',
        'ans': 'option3'
    },
    {
        'course': 'Nec',
        'question': 'What is the purpose of an IP address?',
        'op1': 'To uniquely identify a device on a network',
        'op2': 'To connect peripherals to a computer',
        'op3': 'To increase processing speed',
        'op4': 'To measure battery power',
        'ans': 'option1'
    },
    {
        'course': 'Nec',
        'question': 'Which one of the following is an example of an input device?',
        'op1': 'Printer',
        'op2': 'Keyboard',
        'op3': 'Monitor',
        'op4': 'Speakers',
        'ans': 'option2'
    },
]
    
    try:
        with transaction.atomic():
            for question_data in computer_engineering_questions:
                ques = QuesModel.objects.create(**question_data)
                ques.save()
            print('succes')
    except Exception as e:
        print(f"Error occurred: {str(e)}")


# Create your views here.
def quiz_home(request):
    if request.method == 'POST':
        # print(request.POST)
        # questions=QuesModel.objects.all()
        questions=QuesModel.objects.order_by('?')[100]
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print('request.POST.get(q.question)',request.POST.get(q.question))
            print("q.ans",q.ans)
            print("q.ans",request.POST.get(q.ans))
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/quiz_home.html',context)

def addQuestion(request):    
    template_path = 'Quiz/AddQuestion.html'
    # populate_questions()
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,template_path,context)
    else: 
        return redirect('home') 
    
def sub_title_quiz(request,sub_category=None):
    template_path = 'Quiz/quiz_home.html'
    
    
    if request.method == 'POST':
        # print(request.POST)
        # questions=QuesModel.objects.all()
        # questions=QuesModel.objects.order_by('?')[100]
        course_subtitle = Sub_Category.objects.filter(name=sub_category).first()
        questions = QuesModel.objects.filter(course_subtitle = course_subtitle )[:100]
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print('request.POST.get(q.question)',request.POST.get(q.question))
            print("q.ans",q.ans)
            print("q.ans",request.POST.get(q.ans))
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        course_subtitle = Sub_Category.objects.filter(name=sub_category).first()
        questions = QuesModel.objects.filter(course_subtitle = course_subtitle )[:100]

        # questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/quiz_home.html',context)
    
    
 
    
    return render(request,template_path,context)