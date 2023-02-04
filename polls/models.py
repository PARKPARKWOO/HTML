import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self): # 질문 출력
        return self.question_text

    def was_published_recently(self): # 전날 시간 빼고 출력
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question 함수에서 참조 같이 삭제
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self): # 선택 출력
        return self.choice_text


