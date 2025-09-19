from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email (only for feedback and spam protection)'
            }),
            'rating': forms.Select(choices=[(i, f"{i} ⭐") for i in range(1, 6)], attrs={'class': 'form-select'}),
        }