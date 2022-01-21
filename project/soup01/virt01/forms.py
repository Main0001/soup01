from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)
