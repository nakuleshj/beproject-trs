from django.shortcuts import render
from rec_module.recommender_module import rec_main
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse
from .models import Places
from .itnr_gen import itnr_main


def index(request):
    return render(request, 'rec_module/index.html')


"""def chat(request):
    return render(request, 'rec_module/browse.html',{'n':range(5)})"""


def rec(request):
    print(staticfiles_storage.path('rec_module/pirs_cbf.csv'))
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
    kn=['n1','n2','n3','n4','n5']
    ki=['i1','i2','i3','i4','i5']
    k1={}
    k2={}
    j=range(5)
    plc_name=[]
    plc_img=[]
    for x in lst:
        p=Places.objects.get(pk=x)
        plc_name.append(p.name)
        plc_img.append(p.pics.url)
    for i in j:
        k1[kn[i]]=plc_name[i].capitalize()
        k2[ki[i]]=plc_img[i]
    k1.update(k2)
    return JsonResponse(k1)


def itnr(request):
    tags=[]
    acts={}
    plc=request.GET.get('place').lower()
    i=request.GET.get('interest')
    tags.append(i)
    p=request.GET.get('pref')
    tags.append(p)
    tags = ','.join(tags)
    acts=itnr_main(plc)
    s=""
    for key in acts.keys():
        l=[]
        s=s+"<b>"+key+":</b><br>"
        l=acts[key]
        for x in l:
            s =s+ "-> " + str(x).capitalize() + "<br>"
        s=s + "<br>"
    #print(s)
    ''''r={}
    i=0
    for i in range(len(acts)):
        r[i]=acts[i]
    print(r)'''
    data_str=s
    data = {'d':data_str}
    return JsonResponse(data)