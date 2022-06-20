from django.shortcuts import render , redirect
from .models import NewListModel
from .forms import NewListForm, NewItemForm
# Create your views here.

def home(response):
    return render(response,'base.html')


def showListItems(response, listName):
    # NewListModel.objects.get(name=listName, user=current_user)
    listN = response.user.newlistmodel_set.get(name=listName)
    
    if response.method == 'POST':
        form = NewItemForm(response.POST)
        if form.is_valid():
            new_item = form.cleaned_data['name'] # form ile gonderilen data
            listN.newitemmodel_set.create(text=new_item) # listN icinde bulundugun liste onun uzerine newitemmodel ile yeni data yarat
            form = NewItemForm()
            
    else:
        form = NewItemForm()
    
    items = listN.newitemmodel_set.all()
    return render(response, 'todoList/showitem.html', {'items': items, 'listName': listN, 'form': form})


def showList(request):
    current_user = request.user
    lists = NewListModel.objects.filter(user=current_user)
    return render(request, 'todoList/showlist.html', {'lists': lists})


def createList(response):
    if response.method == 'POST':
        form = NewListForm(response.POST)
        if form.is_valid():
            new_list_name = form.cleaned_data['name'] # from ile gonderilen namei aliyoruz
            if(NewListModel.objects.filter(name=new_list_name).exists()):
                return redirect('/main/show/')
            NewListModel(name=new_list_name,user=response.user).save() # newListModel data baseye saveliyoruz
            return redirect('/main/show/')
    else:
        form = NewListForm()
    
    return render(response, 'todoList/createlist.html', {'form': form})