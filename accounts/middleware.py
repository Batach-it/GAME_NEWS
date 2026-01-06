from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.allowed_paths = [
            reverse('login'),
            reverse('register'),
            reverse('admin:index'),
        ]

    def __call__(self, request):
        path = request.path

        # якщо сторінка дозволена — пропускаємо
        if path in self.allowed_paths or path.startswith('/admin/'):
            return self.get_response(request)

        # якщо користувач НЕ залогінений — перекинути на логін
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={path}")

        return self.get_response(request)
