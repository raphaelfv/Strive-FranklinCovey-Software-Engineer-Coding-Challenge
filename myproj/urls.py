"""myproj URL Configuration

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
import myproj.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myproj.views.first, name='first'),
    path('answered/<int:collection_id>/', myproj.views.AnsweredListView.as_view(), name='answered'),
    path('answer/<int:collection_id>/<int:step>/', myproj.views.NewAnswerView.as_view(), name='answer'),
]
