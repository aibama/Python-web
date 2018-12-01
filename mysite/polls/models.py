from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Goods(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=20)
    url=models.CharField(max_length=500)
    picture=models.CharField(max_length=300)
    source=models.CharField(max_length=20)
    keyword=models.CharField(max_length=50,default='')
    def __str__(self):
        return self.keyword