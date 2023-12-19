from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ReceiptModel
from .forms import NewUserForm, UserLoginForm


class HomeView(TemplateView):
    template_name = 'base.html'


class ReceiptListView(LoginRequiredMixin, ListView):
    model = ReceiptModel
    template_name = 'receipt_list.html'
    context_object_name = 'receipts'

    def get_queryset(self):
        return ReceiptModel.objects.filter(user=self.request.user)


class ReceiptDetailView(LoginRequiredMixin, DetailView):
    model = ReceiptModel
    template_name = 'receipt_details.html'
    context_object_name = 'receipt'


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = ReceiptModel
    template_name = 'receipt_create.html'
    fields = ('store_name', 'item_list', 'description', 'total_amount')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReceiptUpdateView(LoginRequiredMixin, UpdateView):
    model = ReceiptModel
    template_name = 'receipt_update.html'
    fields = ('store_name', 'item_list', 'description', 'total_amount')  #


class ReceiptDeleteView(LoginRequiredMixin, DeleteView):
    model = ReceiptModel
    template_name = 'receipt_delete.html'
    success_url = reverse_lazy('receipt_list')


# Registration and Login views
class NewUserView(CreateView):
    template_name = 'register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# login view
class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class UserProfileView(TemplateView):
    template_name = 'profile.html'
