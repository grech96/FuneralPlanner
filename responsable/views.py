from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlannerForm
from .models import Planner
from django.http import QueryDict

# Create your views here.

def index(request): 
    if request.user.is_authenticated:
        user = request.user
        try:
            planner = user.planner
            return render(request, 'home.html', {'planner': planner})
        except:
            return render(request, 'home.html')
    return render(request, 'home.html')

def detail_planner(request, planner_id):
    user = request.user
    planner = Planner.objects.get(id= planner_id)
    context = {
        'planner' : planner
    }
    return render(request,'detail.html', context)

def create_planner(request):
    if request.user.is_authenticated:
        form = PlannerForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                planner = form.save(commit = False)
                return redirect('index') 
        return render (request,'planner_create.html',{'form': form})           
    else:
        return redirect('login')

def update_planner(request):
    if request.user.is_authenticated:
        form = PlannerForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                Planner = form.save(commit = False)
                return redirect('index') 
        return render (request,'planner_update.html',{'form': form})           
    else:
        return redirect('login')