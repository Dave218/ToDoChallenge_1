from django import forms
from .models import Note

class TaskForm(forms.Form):
    description = forms.CharField(label = 'Add a task', max_length = 255)

class NoteForm(forms.Form):
    text = forms.CharField(label = 'Add a note', max_length = 255)
    # class Meta: 
    #     model = Note 
    #     fields = ['text']
    #     widgets = {
    #         'text': forms.CharField(label = 'Add a Note', max_length = 255),
    #     }
    # def __init__(self, *args, **kwargs):
    #     super(NoteForm, self).__init__(*args, **kwargs)
    #     self.fields[0].widget = forms.CharField(label = 'Add a Note', max_length = 255)
        