from django.http import HttpResponse
from . import forms
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['bamrah.basav@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/")
        
    else:
        form = forms.ContactForm()
    return render(request, "index.html", {'form': form})


    # return render(request, "index.html")

# def contact(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
    
