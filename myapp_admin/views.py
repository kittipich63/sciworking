from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from myapp_admin.forms import *
from django.contrib.auth.decorators import login_required #ใส่เพื่อให้เข้าระบบก่อนถึงจะทำรายการแต่ละอย่างได้

def admin_dashboard(req):
    return render(req, 'pages/admin_dashboard.html')

def admin_user(req):
    return render(req, 'pages/admin_user.html')

def admin_profile(req):
    return render(req, 'pages/admin_profile.html')    

def admin_alerts(req):
    return render(req, 'pages/admin_alerts.html') 

#@login_required
def admin_room(req):
    if req.method == "POST":
        room_name = req.POST.get('room_name')
        status = req.POST.get('status')
        description = req.POST.get('description')
        obj = AddRoom(room_name=room_name, description=description)
        obj.save()
        return redirect('/admin_room')   
    else:
        obj = AddRoom()   
    obj = AddRoom.objects.all()   
    AllRoom = AddRoom.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRoom, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)        
    context = {
        "AllRoom": AddRoom.objects.all(),
        "page" : page,
    }
    return render(req, 'pages/admin_room.html', context)   

#@login_required
def delete_room(req, id):
    obj = AddRoom.objects.get(id=id)
    obj.delete()
    return redirect('/admin_room')

#@login_required
def edit_room(req,id):
    obj = AddRoom.objects.get(id=id)
    room_name = req.POST.get('room_name')
    status = req.POST.get('status')
    description = req.POST.get('description')
    obj.save()
    return redirect('/admin_room')

