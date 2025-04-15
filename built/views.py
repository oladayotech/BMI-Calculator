from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def bmi(request):
    return render(request, 'bmi.html')