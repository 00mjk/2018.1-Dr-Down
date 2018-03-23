from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .models import User
from .forms import UserForm


def list_users(request):
    users = User.objects.all()
    return render(request, 'user/users.html', {'users': users})


def create_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'user/users-form.html', {'form': form})


class UpdateUserView(UpdateView):
    model = User
    template_name = 'user/users-form.html'
    form_class = UserForm
    success_url = '/'
