from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def main_page(request):
    return render(request, 'main/html/home_page.html')

@login_required
def CS2_news(request):
    return render(request, 'main/html/CS2_news.html')

@login_required
def rust_news(request):
    return render(request, 'main/html/Rust_news.html')

@login_required
def minecraft_news(request):
    return render(request, 'main/html/Minecraft_news.html')

@login_required
def fortnite_news(request):
    return render(request, 'main/html/Fortnite_news.html')








@login_required
def cs2_chat1(request):
    return render(request, 'main/html/cs2_chat1.html')

@login_required
def cs2_chat2(request):
    return render(request, 'main/html/cs2_chat2.html')

@login_required
def cs2_chat3(request):
    return render(request, 'main/html/cs2_chat3.html')

@login_required
def cs2_chat4(request):
    return render(request, 'main/html/cs2_chat4.html')

@login_required
def cs2_chat5(request):
    return render(request, 'main/html/cs2_chat5.html')

@login_required
def cs2_chat6(request):
    return render(request, 'main/html/cs2_chat6.html')








@login_required
def rust_chat1(request):
    return render(request, 'main/html/rust_chat1.html')

@login_required
def rust_chat2(request):
    return render(request, 'main/html/rust_chat2.html')

@login_required
def rust_chat3(request):
    return render(request, 'main/html/rust_chat3.html')

@login_required
def rust_chat4(request):
    return render(request, 'main/html/rust_chat4.html')

@login_required
def rust_chat5(request):
    return render(request, 'main/html/rust_chat5.html')

@login_required
def rust_chat6(request):
    return render(request, 'main/html/rust_chat6.html')








@login_required
def minecraft_chat1(request):
    return render(request, 'main/html/minecraft_chat1.html')

@login_required
def minecraft_chat2(request):
    return render(request, 'main/html/minecraft_chat2.html')

@login_required
def minecraft_chat3(request):
    return render(request, 'main/html/minecraft_chat3.html')

@login_required
def minecraft_chat4(request):
    return render(request, 'main/html/minecraft_chat4.html')

@login_required
def minecraft_chat5(request):
    return render(request, 'main/html/minecraft_chat5.html')

@login_required
def minecraft_chat6(request):
    return render(request, 'main/html/minecraft_chat6.html')








@login_required
def fortnite_chat1(request):
    return render(request, 'main/html/fortnite_chat1.html')

@login_required
def fortnite_chat2(request):
    return render(request, 'main/html/fortnite_chat2.html')

@login_required
def fortnite_chat3(request):
    return render(request, 'main/html/fortnite_chat3.html')

@login_required
def fortnite_chat4(request):
    return render(request, 'main/html/fortnite_chat4.html')

@login_required
def fortnite_chat5(request):
    return render(request, 'main/html/fortnite_chat5.html')

@login_required
def fortnite_chat6(request):
    return render(request, 'main/html/fortnite_chat6.html')




@login_required
def portfolio(request):
    return render(request, 'main/html/index.html')