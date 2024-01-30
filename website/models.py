from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    course = models.ForeignKey(Course, null=True, blank=True,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    subject = models.ForeignKey(Subject, null=True, blank=True,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    
class Sub_Category(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    more_sub = models.TextField(blank=True)
    details = models.TextField(null=True, blank=True)
    image_upload = models.ImageField(blank=True,upload_to = "images/")

    def __str__(self):
        return self.name
    
    
class Quiz(models.Model):
    course = models.ForeignKey(Course, null=True, blank=True,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    public =  models.BooleanField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    