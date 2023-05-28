import datetime

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Review
from .forms import ReviewForm
from .services import kmp_search


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('reviews:review_list')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user  # Привязываем отзыв к текущему пользователю
        text = form.cleaned_data['content']
        censored_words = ['Плохо', 'Ужасно', 'Отвратительно', 'Не нравится', 'Абоба']

        for word in censored_words:
            if kmp_search(word.lower(), text.lower()):
                messages.error(self.request, f'Текст содержит недопустимые выражения ("{word}").')
                return super().form_invalid(form)

        review.save()
        return super().form_valid(form)


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('reviews:review_list')

    def form_valid(self, form):
        review = form.instance
        text = form.cleaned_data['content']
        censored_words = ['Плохо', 'Ужасно', 'Отвратительно', 'Не нравится', 'Абоба']

        for word in censored_words:
            if kmp_search(word.lower(), text.lower()):
                messages.error(self.request, f'Текст содержит недопустимые выражения ("{word}").')
                return super().form_invalid(form)

        review.created_at = datetime.datetime.now()
        return super().form_valid(form)


class ReviewDeleteView(View):
    def post(self, request, *args, **kwargs):
        review_id = request.POST.get('review_id')
        try:
            review = Review.objects.get(id=review_id, user=request.user)
            review.delete()
            return JsonResponse({'success': True})
        except Review.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Review not found or you are not the author.'})