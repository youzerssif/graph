from django.shortcuts import render
from django.db.models import Avg,Max,FloatField
# Create your views here.

from .models import *
from django.utils import timezone
from datetime import timedelta
import random



def home(request):

    livre = Book.objects.all()
    # Total number of books with publisher=BaloneyPress
    livre_BaloneyPress = Book.objects.filter(publisher__name='Fear report yet glass million. Evening beyond evening paper I.').count()
    # Average price across all books.
    moyenne = Book.objects.all().aggregate(Max('price'))
    # Difference between the highest priced book and the average price of all books.
    difference = Book.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
    data={
        'livre':livre,
        'livre':livre,
        'difference':difference,
        'livre_BaloneyPress':livre_BaloneyPress,
    }
    return render(request, 'index.html',data)