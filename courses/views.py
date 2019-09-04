from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from .forms import SuggestionForm, QuizForm, TrueFalseQuestionForm, MultipleChoiceQuestionForm
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Course, Text, Quiz
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


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


def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(Text, course_id=course_pk, pk=step_pk)
    context = {
        'step': step
    }
    return render(request, 'step_detail.html', context)


def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(Quiz, course_id=course_pk, pk=step_pk)
    context = {
        'step': step
    }
    return render(request, 'quiz_detail.html', context)



def quiz_create(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    form = QuizForm()

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.course = course
            quiz.save()
            messages.success(request, f'Quiz Added')
            return HttpResponseRedirect(quiz.get_absolute_url())



    return render(request, 'quiz_form.html', {'form': form, 'course': course})


def quiz_edit(request, course_pk, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk, course_id=course_pk)
    form = QuizForm(instance=quiz)

    if request.method == 'POST':
        form = QuizForm(instance=quiz, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated {}".format(form.cleaned_data['title']))
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'quiz_form.html', {'form': form, 'course': quiz.course})


def create_question(request, quiz_pk, question_type):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    if question_type == 'tf':
        form_class = TrueFalseQuestionForm
    else:
        form_class = MultipleChoiceQuestionForm

    form = form_class()

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            messages.success(request, f'Question Added')
            return HttpResponseRedirect(quiz.get_absolute_url())

    return render(request, 'courses/question_form.html', {
        'form': form,
        'quiz': quiz
    })



