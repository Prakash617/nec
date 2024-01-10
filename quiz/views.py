from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.
def quiz_home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
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