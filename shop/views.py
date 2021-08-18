from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import RegisterForm, ItemCheckForm
from .models import Item, Purchase


class MainPage(TemplateView):
    template_name = 'index.html'

class Login(LoginView):
    success_url = '/'
    template_name = 'login.html'

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'

class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'

class Items(CreateView):
    form_class = ItemCheckForm
    template_name = 'add_items.html'
    success_url='/'

class ItemsListView(ListView):
    model = Item
    template_name = 'items.html'
    extra_context = {'create_form': ItemCheckForm()}

    def get_context_data(self, **kwargs):
         context = super(ItemsListView, self).get_context_data(**kwargs)
         context['Purchase'] = Purchase.objects.all()
         return context

class ItemsUpdateView(UpdateView):
    template_name = 'update_items.html'
    model = Item
    fields = ['name', 'description', 'price', 'in_stock']
    success_url='/'
