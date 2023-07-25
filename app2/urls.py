from django.urls import path
from . import views
app_name ='app2'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new_conv'),
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
]
