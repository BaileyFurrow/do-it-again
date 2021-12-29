from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('list_and_instances')
    return render(request, 'index.html')

@login_required
def list_and_instances(request):
    pass

@login_required
def new_list(request):
    pass

@login_required
def new_instance(request):
    pass

@login_required
def current(request):
    pass