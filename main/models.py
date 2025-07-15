from django.db import models

class WorkVideo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
class WorkPhoto(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='work_photos/')    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}" or f"Photo {self.id}"