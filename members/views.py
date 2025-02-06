from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def members(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": myMembers
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myMember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": myMember,
    }
    return HttpResponse(template.render(context, request))