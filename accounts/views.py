from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from .models import Profile




from .forms import RegisterForm, LoginForm


# ---------- РЕЄСТРАЦІЯ ----------
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # автологін після реєстрації
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form, 'hide_logo': True})


# ---------- ЛОГІН ----------
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_logo'] = True
        return context

    def get_success_url(self):
        return '/'   # після логіну → на головну



# ---------- ГОЛОВНА (доступна тільки залогіненим) ----------
@login_required
def home_view(request):
    return render(request, 'home.html')



@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # редірект після успішного завантаження
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})