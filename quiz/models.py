from django.db import models
from website.models import *
 
# Create your models here.
Quiz_CHOICES =[
    ("option1", "option1"), 
    ("option2", "option2"), 
    ("option3", "option3"), 
    ("option4", "option4"),  
]

class QuesModel(models.Model):
    course = models.ForeignKey(Subject,blank=True,null=True,on_delete=models.SET_NULL)
    course_subtitle = models.ForeignKey(Sub_Category,null=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=100, choices=Quiz_CHOICES)
    
    def __str__(self):
        return self.course.name + " - "+ self.question