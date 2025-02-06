from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def members(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    randomDict = [{"key": 1}, {"key": 2}, {"key": 3}]
    context = {
        "mymembers": myMembers,
        "randomNumber": randomDict,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myMember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": myMember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
    }
    return HttpResponse(template.render(context, request))