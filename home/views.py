from django.shortcuts import render, redirect
from contact.forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'home/home_page.html', context)