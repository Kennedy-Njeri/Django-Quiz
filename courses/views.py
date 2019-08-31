from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from .forms import SuggestionForm
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Course, Text, Quiz
from itertools import chain


class Account(TemplateView):
    template_name = 'account.html'


def suggestion_view(request):
    form = SuggestionForm()
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']),
                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['mistakenz@gmail.com']
            )
            messages.success(request, f'Thank you')
            return redirect('suggest')
    return render(request, 'suggestion_form.html', {'form': form})


def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, "course_list.html", context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()), key=lambda step: step.order)
    context = {
        'course': course,
        'steps': steps
    }
    return render(request, 'course_detail.html', context)


def text_detail(request, pk):
    step = get_object_or_404(Text, pk=pk)
    context = {
        'step': step
    }
    return render(request, 'step_detail.html', context)


def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(Quiz, course_id=course_pk, step_id=step_pk)
    context = {
        'step': step
    }
    return render(request, 'quiz_detail.html', context)
