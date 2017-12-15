from django import forms
from .models import Topic
from django.core import validators


# def check_validation(value):
#     if len(value)==0:
#         raise forms.ValidationError("Fill out this field")
#     return value


# class NewTopicForm(forms.Form):
#     subject = forms.CharField(max_length=200,help_text='The max length of the text is 200.')
#     message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
#         ), max_length=4000,help_text='The max length of the text is 4000.')
#
#     def check_validation(self):
#         subject=self.cleaned_data['subject']
#         message=self.cleaned_data['message']
#         if len(subject) == 0 or len(message)==0:
#             raise forms.ValidationError("Fill out this field""Fill out this field")

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ), max_length=4000,help_text='The max length of the text is 4000.')
    subject = forms.CharField(max_length=200,help_text='The max length of the text is 200.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']