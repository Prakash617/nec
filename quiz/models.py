from django.db import models
 
# Create your models here.
Quiz_CHOICES =[
    ("option1", "option1"), 
    ("option2", "option2"), 
    ("option3", "option3"), 
    ("option4", "option4"),  
]

class QuesModel(models.Model):
    course = models.CharField(default='Nec',blank=True,max_length=200, null=True)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=100, choices=Quiz_CHOICES)
    
    def __str__(self):
        return self.question