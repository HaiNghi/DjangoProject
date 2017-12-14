from django import forms
from .models import Question,Choice
from django.core import validators


def check_for_z(value):
    if value[0].lower()>'z' or value[0].lower()<'a':
        raise forms.ValidationError("Question need to start with a letter")

class FormName(forms.Form):
    question_content = forms.CharField(max_length=200,validators=[check_for_z])
    text= forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_text(self):
        text=self.cleaned_data['question_content']
        if len(text)<0:
            raise forms.ValidationError("Invalidate input!")
        return text


class FormAddChoice(forms.Form):
    choice_content = forms.CharField(max_length=200)

class FormVote(forms.Form):
    # choice_content =forms.ModelChoiceField(queryset = Question.objects.all(),widget=forms.RadioSelect)


    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id')
        question_obj = Question.objects.get(id=question_id)
        super(FormVote, self).__init__(*args, **kwargs)
        self.fields['votes'] = forms.ModelChoiceField(queryset=Choice.objects.filter(question=question_obj),
                                                      widget=forms.RadioSelect(), empty_label=None,label='')