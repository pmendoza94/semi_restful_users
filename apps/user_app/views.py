from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'user_app/index.html', context)

def new(request):
    return render(request, 'user_app/new.html')

def create(request):
    results = User.objects.userVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request,error)
    else:
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        messages.success(request, 'New user has been created!')

    return redirect('/new')

def show(request, user_id):
    context = {
        'users': User.objects.get(id = user_id),
    }
    return render(request, 'user_app/show.html', context)

def edit(request, user_id):
    context = {
        'users': User.objects.get(id = user_id),
    }
    return render(request, 'user_app/edit.html', context)

def update(request, user_id):
    results = User.objects.userVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request,error)
        return redirect('/edit/{}'.format(user_id))

    update_user = User.objects.get(id = user_id)
    update_user.first_name = request.POST['first_name']
    update_user.last_name = request.POST['last_name']
    update_user.email = request.POST['email']
    update_user.save()
    return redirect('/')

def destroy(request, user_id):
    User.objects.get(id = user_id).delete()
    return redirect('/')
