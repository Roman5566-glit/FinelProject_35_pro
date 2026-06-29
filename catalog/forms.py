from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form for product reviews"""

    class Meta:
        """Meta options for ReviewForm"""
        model = Review
        fields = ('rating', 'text')
        widgets = {
            'rating': forms.Select(
                choices=[
                    (5, '⭐⭐⭐⭐⭐'),
                    (4, '⭐⭐⭐⭐'),
                    (3, '⭐⭐⭐'),
                    (2, '⭐⭐'),
                    (1, '⭐'),
                ],
                attrs={'class': 'form-select'}
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Напишите ваш отзыв...'
                }
            ),
        }
        labels = {
            'rating': 'Оценка',
            'text': 'Отзыв',
        }
