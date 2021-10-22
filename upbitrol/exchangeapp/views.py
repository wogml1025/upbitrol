from django.shortcuts import render

def exchange(request):
    if request.method == 'GET':
        return render(request, 'exchangeapp/exchange.html')