# Django: forms.py
from django import forms
from .models import Lesson, LessonContent, ContentBlock

class LessonCreateForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'max_score']

class LessonContentForm(forms.ModelForm):
    class Meta:
        model = LessonContent
        fields = ['total_blocks']

class ContentBlockForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = ['order', 'block_type', 'title', 'text', 'media_url', 'task_type', 'data']
