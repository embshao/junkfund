from django.shortcuts import render, redirect
from .models import Candidate
from django.views.generic import TemplateView
from apply.forms import ApplicationForm
from datetime import datetime

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.date = datetime.now()
            form.save()
    else:
        form = ApplicationForm()
    args = {
        'form': form
    }
    return render(request, 'apply/apply.html', args)




