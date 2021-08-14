from django.shortcuts import render
from registration.forms import ProfessionalForm
from registration.models import Professional
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):

    return render(request, 'registration/index.html', {'form':form})



# def registrations(request):
#
#     if request.method == "POST":
#         form= ProfessionalForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance= form.save();
#             instance.save()
#             return HttpResponseRedirect(reverse('landing'))
#         else:
#             print(form.errors)
#
#     else:
#         form= ProfessionalForm()
#     return render(request, 'registration/registration1.html', {'form':form})


def registration(request):
    form= ProfessionalForm()
    if request.method == "POST":
        print(request.POST)
        form= ProfessionalForm(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save();
            instance.save()
            return HttpResponseRedirect(reverse('landing'))


    return render(request, 'registration/registration.html', {'form':form})


def landing(request):
    return render(request, 'registration/landing.html')
