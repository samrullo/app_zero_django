from tkinter import Widget
from django import forms
from .models import Status

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


class TaskForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    status=forms.CharField(widget=forms.Select(attrs={'class':'form-control'},choices=[(Status.NEW,Status.NEW),(Status.INPROGRESS,Status.INPROGRESS),(Status.COMPLETE,Status.COMPLETE)]))
    deadline=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    progress=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

class TaskProjectForm(forms.Form):
    client = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    project_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    status=forms.CharField(widget=forms.Select(attrs={'class':'form-control'},choices=[(Status.NEW,Status.NEW),(Status.INPROGRESS,Status.INPROGRESS),(Status.COMPLETE,Status.COMPLETE)]))
    deadline=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    progress=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
