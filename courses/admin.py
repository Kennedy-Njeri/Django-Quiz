from django.contrib import admin
from .models import Course, Text, Quiz, Answer, Question, MultipleChoiceQuestion, TrueFalseQuestion

# class TextInline(admin.StackedInline):
#     model = Text
#
#
#
# class CourseAdmin(admin.ModelAdmin):
#     inlines = [TextInline,]




admin.site.register(Course)
admin.site.register(Text)
admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(TrueFalseQuestion)


