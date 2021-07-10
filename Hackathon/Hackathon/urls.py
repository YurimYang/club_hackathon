"""Hackathon URL Configuration

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
import Project.views
import User.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Project.views.main, name = "main"),
    path('Signup/',User.views.signup,name="Signup"),
    path('Login/',User.views.login,name="Login"),
    path('Logout/',User.views.logout,name="Logout"),
    path('CircleInfo_Type/',Project.views.CircleInfo_Type,name="CircleInfo_Type"),
    path('CircleInfo_TopField/',Project.views.CircleInfo_TopField,name="CircleInfo_TopField"),
    path('CircleInfo_LiberalArts/',Project.views.CircleInfo_LiberalArts,name="CircleInfo_LiberalArts"),
    path('CircleInfo_NaturalScience/',Project.views.CircleInfo_NaturalScience,name="CircleInfo_NaturalScience"),
    path('CircleInfo_EnterSports/',Project.views.CircleInfo_EnterSports,name="CircleInfo_EnterSports"),
    path('CircleInfo_Volunteer/',Project.views.CircleInfo_Volunteer,name="CircleInfo_Volunteer"),
    path('CircleInfo_List/',Project.views.CircleInfo_List,name="CircleInfo_List"),
    path('CircleInfo_Detail/<int:club_id>',Project.views.CircleInfo_Detail,name="CircleInfo_Detail"),
    path('Register/',Project.views.Register,name="Register"),
    path('Matching_Apply/',Project.views.Matching_Apply,name="Matching_Apply"),
    path('myClub/',User.views.myClub,name="myClub"),
    path('myClubEdit/',User.views.myClubEdit,name="myClubEdit"),
    path('new/',Project.views.new,name="new"),
    path('SearchCircle/',Project.views.Search_Circle,name="Search_Circle"),
    path('SearchUni/',Project.views.Search_Uni,name="Search_Uni"),

]
