from django.shortcuts import render

# Create your views here.
def donate(request):
    context = {}
    return render(request, 'donate/donate.html', context)