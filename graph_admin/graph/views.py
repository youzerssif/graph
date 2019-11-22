from django.shortcuts import render

# Create your views here.

from .models import EmailSubscriber
from django.utils import timezone
from datetime import timedelta
import random


def home(request):

    
    data={}
    return render(request, 'index.html',data)