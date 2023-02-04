"""python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # /polls/ 시 호출
    #path("", views.index, name="index"),
    # ex) /polls/5/ 5번 질문 호출
    # path("<int:question_id>/", views.detail, name="detail"),
    # ex) /polls/5/results/
    # path("<int:question_id>/result/", views.results, name="results"),
    # ex) /polls/5/vote/
    path("<int:qeustion_id>/vote/", views.vote, name="vote"),
    # 클래스로 호출 .as_view
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/result/", views.ResultView.as_view(), name="results"),
]
