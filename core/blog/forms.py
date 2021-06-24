from django import forms
from django.forms import widgets
from .models import Comment


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        label = {'content': 'Comment'}
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-sm outline-none text-gray-700 py-0.5 px-2 leading-8 transition-colors duration-200 ease-in-out'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-sm outline-none text-gray-700 py-0.5 px-2 leading-8 transition-colors duration-200 ease-in-out'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-sm outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'
                }
            )
        }
