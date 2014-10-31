from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from todo.models import Todo, importance_choices, status_choices


def todo_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    error_msg = ''

    if username and password:
        # check password, log user in+redirect if ok
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(todo_index))
            else:
                error_msg = "Your account has been disabled!"
        else:
            error_msg = "Your username and password were incorrect!"
            password = ''

    return render_to_response('todo_login.html', {'username': username, 'password': password, 'error_msg': error_msg, })


def todo_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(todo_login))


def todo_index(request):
    if request.user.id is None:
        return HttpResponseRedirect(reverse(todo_login))

    todos = Todo.objects.filter(owner=request.user).order_by('importance', 'title').exclude(status='B')
    return render_to_response('index.html', {'todos': todos, 'importance': importance_choices,
                                             'status': status_choices, 'user': request.user,
                                             'error_msg': request.GET.get('error_msg', ''), })


def add_todo(request):
    t = Todo(status=request.POST['status'],
             title=request.POST['title'],
             description=request.POST['description'],
             importance=request.POST['importance'],
             owner=request.user)
    t.save()
    return HttpResponseRedirect(reverse(todo_index))


def update_page(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if todo.owner.id != request.user.id:
        return HttpResponseRedirect(reverse(todo_index) + "?error_msg=That's not your todo!")
    return render_to_response('todo_form.html',
                              {'todo': todo, 'importance': importance_choices, 'status': status_choices})


def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if todo.owner.id != request.user.id:
        return HttpResponseRedirect(reverse(todo_index) + "?error_msg=That's not your todo!")
    todo.title = request.REQUEST['title']
    todo.importance = request.REQUEST['importance']
    todo.status = request.REQUEST['status']
    todo.description = request.REQUEST['description']
    todo.save()
    return HttpResponseRedirect(reverse(todo_index))


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if todo.owner.id != request.user.id:
        return HttpResponseRedirect(reverse(todo_index) + "?error_msg=That's not your todo!")
    todo.delete()
    return HttpResponseRedirect(reverse(todo_index))