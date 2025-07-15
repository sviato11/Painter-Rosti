from django.shortcuts import render
from .models import WorkVideo, WorkPhoto

def index(request):
    photos = WorkPhoto.objects.order_by('-created_at')
    return render(request, 'main/index.html', {'photos': photos})

def video_gallery(request):
    videos = WorkVideo.objects.order_by('-uploaded_at')
    return render(request, 'main/videos.html', {'videos': videos})