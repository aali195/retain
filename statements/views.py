from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import StatementForm

from .models import Statement
from collecs.models import Collection


def new(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    if collection.creator != request.user:
        messages.error(request, 'Statements can only be added by the collection creator')
        return redirect('dashboard')
    else:
        form = StatementForm(request.POST or None)
        context = {
            'form': form,
            'collection': collection,
        }
        if request.method == 'POST':
            if form.is_valid():
                statement = form.save(commit=False)
                statement.collection = collection
                statement.save()
                messages.success(request, 'Statement has been created successfully')
                form = StatementForm()
                context['form'] = form
                return render(request, 'statements/new.html', context)
            else:
                messages.error(request, 'Invalid details')
                return render(request, 'statements/new.html', context)
        else:
            return render(request, 'statements/new.html', context)


def edit(request, collection_id, statement_id):
    
    statement = get_object_or_404(Statement, pk=statement_id)
    if statement.collection.creator != request.user:
        messages.error(request, 'Statements can only be edited by the collection creator')
        return redirect('dashboard')
    else:
        form = StatementForm(request.POST or None, instance=statement)
        statements = Statement.objects.filter(collection=collection_id)
        context = {
            'form': form,
            'statement': statement,
            'statements': statements,
        }
        if request.method == 'POST':
            if form.is_valid():
                edited_statement = form.save(commit=False)
                edited_statement.save()
                messages.success(request, 'Statement has been edited successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid details')
                return render(request, 'statements/edit.html', context)
        else:
            return render(request, 'statements/edit.html', context)