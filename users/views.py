from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from users.forms import UserRegisterForm


class RegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('blog:index')
    template_name = 'users/register.html'
    success_message = f" was created successfully!"

    def get_success_message(self, cleaned_data):
        username = cleaned_data['username']
        return f'{ username } has been registered!'


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'users/profile.html'
    # login_url = '/users/login/'
