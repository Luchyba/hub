from django.shortcuts import render
from django.http import HttpResponse
from  django.core.mail import send_mail


# Create your views here.
def Home(request):
    return render(request, 'home.html', )


def event(request):
    return render(request, 'coc.html', )


def community(request):
    return render(request, 'services.html', )


def team(request):
    return render(request, 'pricing.html', )


def about(request):
    return render(request, 'about.html', )


def camp(request):
    return render(request, 'blog.html', )


def volunteer(request):
    return render(request, 'volunteer.html', )


def project(request):
    return render(request, 'project.html', )


def incubate(request):
    return render(request, 'incubator.html', )


def it4gh(request):
    return render(request, 'it4gh.html', )

def ccoc(request):
    return render(request, 'ccoc.html',)
    
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        # send mail
        send_mail(
            message_name, # subject
            message, # message
            message_email, #from
            ['techneggh@gmail.com'] #to Email
            )

        return render(request, 'contact.html', {'message_name': message_name } )
    else:
        return render(request, 'contact.html',{} )
