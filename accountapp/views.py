from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(req):
    if req.method == 'POST':
        temp = req.POST.get("input_text")
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello world'))

    else:
        new_hello_world_list = HelloWorld.objects.all()
        return render(req, 'accountapp/hello_world.html',
                      context={'new_hello_world_list': new_hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello world')
    template_name = 'accountapp/create.html'


# 회원정보
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


# 회원정보 업데이트
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello world')
    template_name = 'accountapp/update.html'


# 회원탈퇴
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
