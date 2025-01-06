
from django.urls import path
from . import views

app_name = 'cleanai'
urlpatterns = [
    path('', views.index, name='index'),
    path('image/proccess/', views.image_background_proccessor, name='image_background_processor'),
    path('subscription/plans/', views.subscription_plans, name='subscription'),
]
