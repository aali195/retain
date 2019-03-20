from django.shortcuts import render

def learn(request):
    return render(request, 'progress/learn.html')

def review(request):
    return render(request, 'progress/review.html')