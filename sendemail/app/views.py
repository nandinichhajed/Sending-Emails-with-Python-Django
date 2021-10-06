from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
    )
    return render(request,'home.html')