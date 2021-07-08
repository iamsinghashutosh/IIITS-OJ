from django.shortcuts import render
from .models import Review
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError


def send_email(request):
    subject = 'Query submitted'
    message = 'We received your query. We will get back to you soon.\n\nTeam IIITS-OJ'
    from_email = 'iiits.oj@gmail.com'
    try:
        send_mail(subject, message, from_email,[request.POST['email']])
    except BadHeaderError:
        return 
    return HttpResponse('')


def home(request):
    reviews=Review.objects.order_by('-id')
    length=len(reviews)
    if length>3:
        reviews=list(reviews[:3])
    return render(request,'home/frontpage.html',{'reviews':reviews})

def savereview(request):
    temp=Review.objects.create(user=request.user,content=request.POST['content'].replace("\n","<br>"))
    temp.save()
    return HttpResponse("")