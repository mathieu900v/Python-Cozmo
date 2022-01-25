from django.shortcuts import render, redirect, HttpResponseRedirect
from website_cozmo.models import Game
from website_cozmo.models import Member
import sys
import sqlite3
import cozmo
import random
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import radians, degrees, distance_mm, speed_mmps


def on_cube_tapped(event, *, obj, tap_count, tap_duration, **kw): 
    global tapote
    global who_is_tapped


    tapote = True
    who_is_tapped = obj.object_id-1

def index(request):
    return render(request, 'website_cozmo/login.html')


def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'website_cozmo/home.html', {'user': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'website_cozmo/login.html', context)


def signout(request):
    return render(request, 'website_cozmo/login.html')

def inscription_page(request):
    return render(request, 'website_cozmo/signup.html')


def signup(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return render(request, 'website_cozmo/login.html')
    else:
        return render(request, 'signup.html')

 

def game(request):
    all_info = Game.objects.all()
    if request.method == 'POST':
        file_name = str(request.POST['file']) + '.py'
        file_path = "./game/" + file_name
        exec(open(file_path).read())


    return render(request, 'website_cozmo/game.html', {'games':all_info})


def libre(request):
    return render(request, 'website_cozmo/libre.html')

def histoire(request):
    return render(request, 'website_cozmo/histoire.html')

def createprogram(request):
    if(request.POST['content'] != ""):
            handle1=open('freeprogram.py','w+')
            handle1.write(request.POST['content'])
            handle1.close()
            saveout = sys.stdout                                   
            fsock = open('out.log', 'w')                             
            sys.stdout = fsock
            try:
                exec(open("freeprogram.py").read())
            except Exception as error:
                print(error)
            sys.stdout = saveout                                     
            fsock.close() 
            fsockR = open('out.log', 'r')
            return render(request, 'website_cozmo/libre.html', {'log':fsockR.read()})