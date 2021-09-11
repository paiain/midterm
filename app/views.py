from django.shortcuts import render

# Create your views here.
def patient(request):
    return render(request,'patient.html')

def doctor(request):
    return render(request,'doctor.html')

def index(request):
    return render(request,'index.html')