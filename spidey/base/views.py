from django.shortcuts import render
from .models import Stamp

# Create your views here.

def home(request):
    recent_stamps = Stamp.objects.all().order_by('-year')[:4]
    popular_stamps = Stamp.objects.all().order_by('-price')[:8]
    return render(request, "index.html", {
        'recent_stamps': recent_stamps,
        'popular_stamps': popular_stamps
    })