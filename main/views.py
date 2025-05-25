from django.shortcuts import render
from .models import WorkVideo

def index(request):
    return render(request, 'main/index.html')

def video_gallery(request):
    videos = WorkVideo.objects.all()
    return render(request, 'main/videos.html', {'videos': videos})