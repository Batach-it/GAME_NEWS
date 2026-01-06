from django.urls import path
from .views import main_page, CS2_news, rust_news, minecraft_news, fortnite_news, cs2_chat1, cs2_chat2, cs2_chat3, cs2_chat4, cs2_chat5, cs2_chat6, rust_chat1, rust_chat2, rust_chat3, rust_chat4, rust_chat5, rust_chat6, minecraft_chat1, minecraft_chat2, minecraft_chat3, minecraft_chat4, minecraft_chat5, minecraft_chat6, fortnite_chat1, fortnite_chat2, fortnite_chat3, fortnite_chat4, fortnite_chat5, fortnite_chat6, portfolio

urlpatterns = [
    path('', main_page, name='main_page'),

    path('CS2_news/', CS2_news, name='CS2_news'),
    path('rust_news/', rust_news, name='rust_news'),
    path('minecraft_news/', minecraft_news, name='minecraft_news'),
    path('fortnite_news/', fortnite_news, name='fortnite_news'),




    path('cs2_chat1/', cs2_chat1, name='cs2_chat1'),
    path('cs2_chat2/', cs2_chat2, name='cs2_chat2'),
    path('cs2_chat3/', cs2_chat3, name='cs2_chat3'),
    path('cs2_chat4/', cs2_chat4, name='cs2_chat4'),
    path('cs2_chat5/', cs2_chat5, name='cs2_chat5'),
    path('cs2_chat6/', cs2_chat6, name='cs2_chat6'),




    path('rust_chat1/', rust_chat1, name='rust_chat1'),
    path('rust_chat2/', rust_chat2, name='rust_chat2'),
    path('rust_chat3/', rust_chat3, name='rust_chat3'),
    path('rust_chat4/', rust_chat4, name='rust_chat4'),
    path('rust_chat5/', rust_chat5, name='rust_chat5'),
    path('rust_chat6/', rust_chat6, name='rust_chat6'),




    path('minecraft_chat1/', minecraft_chat1, name='minecraft_chat1'),
    path('minecraft_chat2/', minecraft_chat2, name='minecraft_chat2'),
    path('minecraft_chat3/', minecraft_chat3, name='minecraft_chat3'),
    path('minecraft_chat4/', minecraft_chat4, name='minecraft_chat4'),
    path('minecraft_chat5/', minecraft_chat5, name='minecraft_chat5'),
    path('minecraft_chat6/', minecraft_chat6, name='minecraft_chat6'),




    path('fortnite_chat1/', fortnite_chat1, name='fortnite_chat1'),
    path('fortnite_chat2/', fortnite_chat2, name='fortnite_chat2'),
    path('fortnite_chat3/', fortnite_chat3, name='fortnite_chat3'),
    path('fortnite_chat4/', fortnite_chat4, name='fortnite_chat4'),
    path('fortnite_chat5/', fortnite_chat5, name='fortnite_chat5'),
    path('fortnite_chat6/', fortnite_chat6, name='fortnite_chat6'),


    path('portfolio/', portfolio, name='portfolio'),
]