from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login')
# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'main_app/index.html')