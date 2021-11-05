from django import forms
from django.http import HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse

import tasks





class Newtaskform(forms.Form):
    task = forms.CharField(label= "New Task ")
    

# Create your views here.
# The tasks variable on the right is for the above python variable
# And on the left is for html template will have access to
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []    #if the user doesnot have tasks give empty

    return render(request,"tasks/index.html",{
        "tasks": request.session["tasks"]  #if he has gives all tasks
    })


def add(request):
    if request.method == "POST":  #checks if user is posting
        form = Newtaskform(request.POST) #save all the data in variable
        if form.is_valid():  # check validity
            task = form.cleaned_data["task"] #Adds all the tasks posted and shows the reults
            request.session["tasks"] += [task]  #appends the session
            return HttpResponseRedirect(reverse("tasks:index"))   #no space between task and index
        else:
            return render(request, "task/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html",{    #if he doesn't post anything brings backs to the og website
        "form": Newtaskform()
    })