from msilib import text
from urllib.request import Request
from django.shortcuts import render, redirect
from django.views import View
from todo.models import Task, Note
from todo.forms import TaskForm, NoteForm


class TodoListView(View):
    def get(self, request):
        '''GET the todo list homepage, listing all tasks in reverse order that they were created'''
        tasks = Task.objects.filter(completed = False)
        completed_tasks = Task.objects.filter(completed = True)
        notes = Note.objects.all().order_by('-created')
        form = TaskForm()
        form2 = NoteForm()

        return render(
            request=request, template_name = 'list.html', context = {
                'tasks': tasks, 
                'completed_tasks': completed_tasks, 
                'form': form, 
                'form2': form2, 
                'notes': notes}
        )

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new task in the todo list'''
        form=TaskForm(request.POST)
        if form.is_valid():
            task_description = form.cleaned_data['description']
            Task.objects.create(description=task_description)

        # "redirect" to the todo homepage
        return redirect('todo_list')


class TodoDetailView(View):
    def get(self, request, task_id):
        '''GET the detail view of a single task on the todo list'''
        task = Task.objects.get(id=task_id)
        form = TaskForm(initial={'description': task.description})
        return render(
            request=request, template_name='task_detail.html', context={'form':form, 'id': task_id}
        )

    def post(self, request, task_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        task = Task.objects.filter(id=task_id)
        if 'save' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                task_description = form.cleaned_data['description']
                task.update(description=task_description)
        elif 'delete' in request.POST:
            task.delete()
        elif 'completed' in request.POST:
            task.update(completed=True)

        # "redirect" to the todo homepage
        return redirect('todo_list')

class NoteListView(View):
    def get(self, request):
        '''GET the note list homepage, listing all notes in the order that they were created. '''
        note_list = Note.objects.all().order_by('id')
        note_form = NoteForm()
        
        return render(
            request=request, template_name='list.html', context={'note_list': note_list, 'note_form': note_form}
        )

    def post(self, request):
        '''POST the data in the form submitted by the user, creating  a new task in the todo list. '''
        form = NoteForm(request.POST)
        if form.is_valid():
            note_description = form.cleaned_data['text']
            note = Note.objects.create(text = note_description)
            note.save()

        # "redirect" to the todo homepage
        return redirect('todo_list')

class NoteDetailView(View):
    def get(self, request, note_id):
        '''GET the detailed view of a single note on the note list. '''
        note = Note.objects.get(id = note_id)
        note_form = NoteForm(initial = {'text': note.text})
        
        return render(
            request=request, template_name='note_detail.html', context={'form': note_form, 'id': note_id}
        )

    def post(self, request, note_id):
        '''Update or delete the specific task, based on what the user submitted in the form. '''
        note = Note.objects.filter(id = note_id)
       
        if 'save' in request.POST:
           form = NoteForm(request.POST)
           if form.is_valid():
                text = form.cleaned_data['text']
                note.update(text = text)
        elif 'delete' in request.POST:
            note.delete()
        
        # "redirect" to the todo homepage
        return redirect('todo_list')

