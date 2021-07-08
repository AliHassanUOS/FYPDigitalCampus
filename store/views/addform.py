from store.forms import Notes , FreeNotes
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from store.models import Product
from store.models import Category
from django.contrib import messages
# from django.views.generic import UpdateView




def Notes_Create(request):
    form = Notes(request.POST , request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Your Formchas Added Successfully')
    
 
    context = {
        "form" : form,
    }
    return render(request, 'notes_form.html',context)

def free_notes(request):
    form = FreeNotes(request.POST , request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Your Formchas Added Successfully')
    
 
    context = {
        "form" : form,
    }
    return render(request, 'free_notes.html',context)



# class UpdateNotesView(UpdateView):
#     model = Product
#     template_name = "update_notes.html"
#     fields =  ['name ', 'semester','Teacher']

