from django.urls import path
from apps.chat import views

urlpatterns = [
    path('', views.chat_view, name='chat-view'),
    path('historial/', views.chats_view, name='chat-historial'),
    path('add-contacts/', views.add_contacts_view, name='add-contacts-view'),
    path('contacts/', views.contacts_view, name='contacts-view'),
    path('requests/', views.request_view, name='requests-view'),
    path('delete-request/<int:pk>', views.delete_request, name='delete-request-api'),
    path('accept-request/<int:pk>', views.accept_request, name='accept-request-api'),
    path('set_last_person_msg/', views.set_last_person_msg, name='set_last_person_msg_api')
]
