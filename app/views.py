from django.shortcuts import render, redirect

# Create your views here.


def Home(request):
    return render(request, "app/index.html")

def Error_404(request, exception):
    return render(request, "app/404.html")