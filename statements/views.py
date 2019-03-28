from django.shortcuts import render

def new(request, collection_id):
    return render(request, 'collecs/new.html',)

def edit(request, collection_id, statement_id):
    return render(request, 'collecs/new.html',)