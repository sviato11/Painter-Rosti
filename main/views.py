from django.shortcuts import render, redirect
from .models import WorkPhoto, WorkVideo, Review
from .forms import ReviewForm

def index(request):
    photos = WorkPhoto.objects.order_by('-created_at')
    reviews = Review.objects.order_by('-created_at')[:10]
    return render(request, 'main/index.html', {'photos': photos, 'reviews': reviews})

def leave_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'main/leave_review.html', {'form': form})

def video_gallery(request):
    videos = WorkVideo.objects.order_by('-uploaded_at')
    return render(request, 'main/videos.html', {'videos': videos})