from django.shortcuts import render

def home(request):
    return render(request, 'index.html')    

def leagues(request):
    return render(request, 'leagues.html')  

def teams(request):
    return render(request, 'teams.html')

def about(request):
    return render(request, 'about.html')
    