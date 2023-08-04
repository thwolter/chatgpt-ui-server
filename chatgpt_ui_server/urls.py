from django.contrib import admin
from django.urls import path, include
from chat.views import conversation, gen_title, upload_conversations

urlpatterns = [
    path('api/chat/', include('chat.urls')),
    path('api/conversation/', conversation, name='conversation'),
    path('api/upload_conversations/', upload_conversations, name='upload_conversations'),
    path('api/gen_title/', gen_title, name='gen_title'),
    path('api/account/', include('account.urls')),
    path('admin/', admin.site.urls),
]
