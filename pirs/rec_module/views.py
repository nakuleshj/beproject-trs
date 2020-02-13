from django.shortcuts import render,get_object_or_404
from rec_module.recommender_module import rec_main
from django.http import JsonResponse

import json
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template import loader

def chat(request):
    '''q=["Enter season:","Going with?\n1.Family\n2.Friends\n3.Romantic\n4.Solo\nEnter option number:\n",""]
    going_with = ['family', 'friends', 'romantic', 'solo']
    bm = ['beaches', 'mountains']
    interest = ['adventure', 'sightseeing']'''
    return render(request, 'rec_module/chatbot.html')
def rec(request):
    l=[]
    s=request.GET.get('season')
    l.append(s)
    g=request.GET.get('going_with')
    l.append(g)
    p=request.GET.get('pref')
    l.append(p)
    i=request.GET.get('interest')
    l.append(i)
    usr_tags = ','.join(l)
    print(usr_tags)
    lst=rec_main(usr_tags)
    r = {'rec1': lst[0], 'rec2': lst[1], 'rec3': lst[2]}
    return JsonResponse(r)
    #return HttpResponse(json.dumps(lst), content_type="application/json")
    """context={'lst':lst}
    return render(request, 'rec_module/rec_page.html',context)"""
