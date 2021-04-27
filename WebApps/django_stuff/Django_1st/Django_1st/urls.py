"""Django_1st URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http import HttpResponse
import blog.views as views
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', lambda request: HttpResponse("<h1>How are you?</h1>")),
    # path('about/', views.about),
    path('add/', views.add),
    path('multiplicare/<int:a>/<int:b>/<int:c>', views.mul),
    path('', views.IndexPage.as_view()),
    path('about/', views.AboutPage.as_view()),
    path('blog/', views.BlogPage.as_view()),
    path('contact/', views.ContactPage.as_view()),
    path('proj1/', views.Proj1Page.as_view()),
    path('projects/', views.ProjectsPage.as_view()),
    path('singlepost/', views.SinglePage.as_view()),
    path('greet/<str:nume>', views.SalutPage.as_view())
]
