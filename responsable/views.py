from django.shortcuts import render, get_object_or_404, redirect
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
                planner.user = request.user 
                planner.save()
                return redirect('index') 
        return render (request,'planner_create.html',{'form': form})           
    else:
        return redirect('login')

def update_planner(request, planner_id):
    obj = get_object_or_404(Planner, id = planner_id)
    form = PlannerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "planner_update.html", context)