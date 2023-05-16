from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MatiCoffeeUserCreationForm, MatiCoffeeUserChangeForm
from .models import MatiCoffeeUser

class CreateUser(CreateView):

    """
    Register View

    In order to register, you need to enter an additional field to test this project.
    The special registration code is 'vivacristorey777'.
    """

    form_class = MatiCoffeeUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):

        friend_code = form.cleaned_data.get('friend_code')
        if friend_code != 'matidev':
            form.add_error('code', 'Código de amigos incorrecto')
            return self.form_invalid(form)

        response = super().form_valid(form)
        return response

class UpdateUser(LoginRequiredMixin, UpdateView):

    """
    Update View:

    View for update the name and img user
    
    """

    model = MatiCoffeeUser
    form_class = MatiCoffeeUserChangeForm
    success_url = reverse_lazy('update_user')
    template_name = 'pages/profile_page.html'

    def get_object(self):
        return self.request.user
    