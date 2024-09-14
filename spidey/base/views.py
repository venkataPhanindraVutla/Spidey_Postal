from django.shortcuts import render
from .models import Stamp
from django.db.models import Q

# Create your views here.

def home(request):
    recent_stamps = Stamp.objects.all().order_by('-year')[:4]
    popular_stamps = Stamp.objects.all().order_by('-price')[:8]
    return render(request, "index.html", {
        'recent_stamps': recent_stamps,
        'popular_stamps': popular_stamps
    })

def login(request):
    return render(request, 'login.html')

def stamps(request):
    q = request.GET.get('q', '')
    stamps = Stamp.objects.filter(
        Q(postal_circle__icontains=q) | Q(description__icontains=q) | Q(price__icontains=q) | Q(year__icontains=q)).order_by('-year')
    return render(request, "stamps.html", {'stamps': stamps})