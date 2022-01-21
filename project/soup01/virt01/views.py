from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
import json


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            name_input = form.cleaned_data['name']
            data = json.dumps(name_input, ensure_ascii=False)
            TaskModel.objects.create(data=data, field='name')

            for i in range(1, len(request.POST)-1):
                query = 'name' + str(i)
                input_value = request.POST[query]

                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    TaskModel.objects.create(data=data, field=field)
                i += 1
        return redirect('/task/')
    else:
        form = TaskForm()
    return render(request, 'index.html', {'form':form})


def task(request):
    query = TaskModel.objects.all().values('id', 'field', 'data')
    json_list = list(query)
    return render(request, 'task.html', {'json_list': json_list})
