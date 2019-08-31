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
from .models import Course, Text


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
    context = {
        'course': course
    }
    return render(request, 'course_detail.html', context)

