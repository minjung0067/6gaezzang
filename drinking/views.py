from django.shortcuts import render
from django.views.generic import DetailView
from user.models import Fuser

# Create your views here.
"""
def mypage(request):
    return render(request, 'mypage.html')"""

def developer(request):
    return render(request, 'developer.html')

def recommend(request):
    return render(request, 'recommend.html')

def weather(request):
    return render(request, 'weather.html')

class MemberDetailView(DetailView): 
    template_name = 'mypage.html' 
    model = Fuser