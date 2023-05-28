from django import forms
from .models import Review
from .services import kmp_search


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content')

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        censored_words = ['Плохо', 'Ужасно', 'Отвратительно', 'Не нравится', 'Абоба']
        if content and kmp_search(content, censored_words):
            raise ValidationError('Отзыв содержит запрещенные слова.')

        return cleaned_data