from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
# from django.contrib.auth import login

# Create your views here.

#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

# --- User Creation
# class UserCreateView(CreateView):
#     template_name = 'registration/register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('register_done')
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            # login(request, new_user)
            return redirect('register_done')
        else:
            return alert('사용자명이 이미 존재합니다.')
    else:
        form = UserForm()
        return render(request, 'registration/register.html', {'form': form})



class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

#--- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
