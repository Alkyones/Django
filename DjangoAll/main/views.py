from django.shortcuts import render,redirect
from .forms import  CreateNewListForm
from .models import TodoList,Item
# Create your views here.

def ListDesc(response, id):
    ls= TodoList.objects.get(id=id)

    if ls in response.user.todolist.all():
        if response.method == 'POST':
            if response.POST.get('save'):
                for item in ls.item_set.all():
                    if response.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get('add'):
                    txt = response.POST.get('item')
                    if len(txt) > 2 :
                        ls.item_set.create(text = txt , complete=False)
        return render(response, 'listIn.html', { 'element': ls,})
    else:
        return render(response, 'base.html')

def home(response):
    return render(response, 'base.html')

def create(response):
    if response.method == 'POST':
        form = CreateNewListForm(response.POST)
        if form.is_valid():
            new_data = form.cleaned_data['name']
            data = TodoList(name=new_data)
            data.save()
            response.user.todolist.add(data)
            

    else:    form = CreateNewListForm()
    return render(response, 'create.html', {'form': form})
  
def lists(response):
    
    return render(response, 'lists.html', {})