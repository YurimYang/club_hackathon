from django.shortcuts import redirect,  render
from .models import *
# Create your views here.
def main(request):
    return render(request, "Main.html")

def CircleInfo_Type(request):
    return render(request,"CircleInfo_Type.html")

def CircleInfo_TopField(request):
    return render(request,"CircleInfo_TopField.html")

def CircleInfo_LiberalArts(request):
    return render(request,"CircleInfo_LiberalArts.html")

def CircleInfo_NaturalScience(request):
    return render(request,"CircleInfo_NaturalScience.html")

def CircleInfo_EnterSports(request):
    return render(request,"CircleInfo_EnterSports.html")

def CircleInfo_Volunteer(request):
    return render(request,"CircleInfo_Volunteer.html")

def CircleInfo_List(request):
    club_list = Club.objects.all()       
    return render(request,"CircleInfo_List.html", {'club_list':club_list})



def CircleInfo_Detail(request , club_id):  
    club_detail = Club.objects.get(id = club_id) 
    return render(request,"CircleInfo_Detail.html" , {'club':club_detail})

def Register(request):
    club=Club()
    club.user_id = request.user
    club.title=request.GET.get('title')
    activity=request.GET.get('activity')
    
    if(activity =="교내"):
        club.activity = 0
    else:
        club.activity = 1
    
    clubfield=request.GET.get('Field')
    if(clubfield == "인문"):
        club.clubfield=0
    elif(clubfield=="자연"):
        club.clubfield=1
    elif(clubfield=="예체능"):
        club.clubfield=2
    elif(clubfield=="봉사"):
        club.clubfield=3    
    else:
        club.clubfield=4

    club.leader=request.GET.get('leader')
    club.phone=request.GET.get('phone')
    club.email=request.GET.get('email')
    club.body=request.GET.get('body')
    club.save()
    return redirect('/')

def Matching_Apply(request):
    return render(request,"Matching_Apply.html")

def new(request):
    return render(request,"Register.html")

def Search_Circle(request):       
    return render(request,"Search_Circle.html")

def Search_Uni(request):
    return render(request,"Search_Uni.html")
