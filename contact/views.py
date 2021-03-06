from django.shortcuts import render, redirect

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)