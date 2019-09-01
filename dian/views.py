from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response,render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from service import *

room = 0
i=1

@csrf_exempt
def custumer(request):
    if request.method =='GET':
        data = {}
        dishes = DishService.get_all_dishes()
        data['dishes'] = dishes
        return render_to_response('custumer.html',data)
    elif request.method=='POST':
        data={}
        custumer_dishs=request.POST.get("name")
        custumer_sum=request.POST.get("price")
        if custumer_dishs!=None:
            custumer_room = room
            CustomerSefvice.create(custumer_room,custumer_dishs,custumer_sum)
        print('hellp')
        custumer_room = room
        dishes = DishService.get_all_dishes()
        data['dishes'] = dishes
        custumer=CustomerSefvice.get_one_room(custumer_room)
        data['customer'] = custumer

        return render_to_response('custumer.html',data)



@csrf_exempt
def submite(request):
    data = {}
    get_by_time=CustomerSefvice.get_by_time()
    data['customer_by_time']=get_by_time
    return render_to_response('submit.html',data)

@csrf_exempt
def login(request):
    sum = 0
    if request.method=='GET':
        global i
        i=1
        CustomerSefvice.delet_room(room)
        return render_to_response('login.html')
    elif request.method=='POST':
        data={}
        global room,i
        if i>0:
            room=request.POST.get('room')
            i=0
        custumer_dishs=request.POST.get("name")
        custumer_sum=request.POST.get("price")
        if custumer_dishs!=None:
            custumer_room = room
            CustomerSefvice.create(custumer_room,custumer_dishs,custumer_sum)
        print(room)
        data['room']=room
        custumer_room = room
        dishes = DishService.get_all_dishes()
        cai=DishService.get_cai()
        zhu=DishService.get_zhu()
        sh=DishService.get_sh()
        data['dishes'] = dishes
        data['cai']=cai
        data['zhu']=zhu
        data['sh']=sh
        custumer=CustomerSefvice.get_one_room(custumer_room)
        for c in custumer:
            sum+=c.customer_sum
        data['sum']=sum
        data['customer']=custumer


        return render_to_response('custumer.html',data)

@csrf_exempt
def denglu(request):

    if request.method=='GET':
        return render_to_response('denglu.html')

    elif request.method=='POST':
        user=request.POST.get('username')
        pas=request.POST.get('password')
        cook=Cookservice.get_by(user,pas)
        if cook:
            data={}
            customer=CustomerSefvice.get_by_time()

            data['customer']=customer

            return render_to_response('xianshi.html',data)
        else:
            return render_to_response('denglu.html')

@csrf_exempt
def xianshi(request):

    if request.method=='GET':
        return render_to_response('xianshi.html')
    elif request.method=='POST':
        id=request.POST.get('id')
        CustomerSefvice.change(id)
        data={}
        customer=CustomerSefvice.get_by_time()
        data['customer']=customer
        return render_to_response('xianshi.html',data)

