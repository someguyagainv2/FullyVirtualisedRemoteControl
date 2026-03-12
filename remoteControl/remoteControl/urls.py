"""
URL configuration for remoteControl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("api/createServer/<str:server_id>/", views.createServer),
    path("api/sendChatToClient/<str:server_id>/", views.sendChatToClient),
    path("api/recieveChatClient/<str:server_id>/", views.recieveChatClient),
    path("api/sendChatToServer/<str:server_id>/", views.sendChatToServer),
    path("api/recieveChatServer/<str:server_id>/", views.recieveChatServer),
    path("api/recievePositionToClient/<str:server_id>/", views.recievePositionToClient),
    path("api/sendPositionToClient/<str:server_id>/", views.sendPositionToClient),
    path("api/recievePositionToServer/<str:server_id>/", views.recievePositionToServer),
    path("api/sendPositionToServer/<str:server_id>/", views.sendPositionToServer),
    path("api/setPlayerName/<str:server_id>/", views.setPlayerName),
    path("api/lightSet/<str:server_id>/", views.setTime),
    path("api/recieveLight/<str:server_id>/", views.getTime),
]
