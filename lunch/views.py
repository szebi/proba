from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Lunch
from .forms import LunchForm

def index(request):
    lunch_list = Lunch.objects.order_by('pk')
    form = LunchForm()
    context = {'lunch_list': lunch_list, 'form': form }
    return render(request, 'lunch/index.html', context)

def new(request):
    if request.method == 'POST':
        form = LunchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/lunch')
    else:
        form = LunchForm()

    return render(request, 'lunch/index.html', {'form': form})    

