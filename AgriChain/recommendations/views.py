from django.shortcuts import render

# Create your views here.

def recommend(request):
    return render(request,'recommend/recommend.html')

def result(request):
    return render(request,'recommend/result.html')
