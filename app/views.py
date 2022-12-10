from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
# Create your views here.


def Home(request):
    if 'make' not in request.session:
        request.session['count'] = 1
        policy = Policy.objects.all()
    else:
        request.session['count'] = 2
        policy = Policy.objects.filter(model = request.session['model'])
    if len(policy) == 0:
        n = 0
    else:
        n = 1
    cars = Company.objects.all()
    print(n, policy)
    return render(request, "app/index.html", {'cars': cars, 'policy': policy, 'n': n})

def Error_404(request, exception):
    return render(request, "app/404.html")




def getDataAjax(request):
    if request.method == 'POST':
        make = request.POST['make']
        companyName = Company.objects.get(name = make)
        request.session['make'] = make
        # data = Model.objects.filter(make = companyName).values("model", "engine_hp").distinct()
        data = Model.objects.filter(make = companyName).values("model").distinct()
        data = [x for x in data]
        return JsonResponse({'data': data})


def getPolicy(request, pk):
    if request.method == "POST":
        if pk == 1:
            request.session['make'] = 'Chrysler'
            request.session['model'] = 'Accadia'
            request.session['no'] = request.POST['RegNoInput']
        else:
            request.session['model'] = request.POST['modelName']
        return redirect("home")

def changeModel(request):
    if 'no' in request.session:
        del request.session['no']
    del request.session['make']
    del request.session['model']
    request.session['count'] = 1
    return redirect("home")