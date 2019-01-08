from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class RegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('blog:index')
    template_name = 'users/register.html'
    success_message = f" was created successfully!"

    def get_success_message(self, cleaned_data):
        username = cleaned_data['username']
        return f'{ username } has been registered!'


class ProfileView(LoginRequiredMixin, generic.View):
    """Form to edit a user profile. It uses generic.View because it contains two forms."""
    template_name = 'users/profile.html'

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {'u_form': u_form, 'p_form': p_form}
        return render(request, 'users/profile.html', context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'The user has been updated.')
        else:
            messages.warning(request, 'The profile has not been updated')

        return redirect('users:profile')
