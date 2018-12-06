from django.shortcuts import render

# Create your views here.
def give(request):
    context = {}
    return render(request, 'donate/give_page.html', context)

def invest(request):
    context = {}
    return render(request, 'donate/invest_page.html', context)

def giveMonth(request):
    context = {}
    return render(request, 'donate/give_month.html', context)

def investMonth(request):
    context = {}
    return render(request, 'donate/invest_month.html', context)