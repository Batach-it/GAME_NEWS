from django.urls import path
from .views import register_view, CustomLoginView, home_view, profile
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from main import views



urlpatterns = [
    path('register/', register_view, name='register'),           # URL для реєстрації
    path('login/', CustomLoginView.as_view(), name='login'),     # URL для логіну
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # URL для виходу
    path('profile/', profile, name='profile'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)