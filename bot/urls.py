from django.urls import path
from . import views
app_name = "bot"
urlpatterns = [
    path('', views.index, name="index"),
    path('SaveQuestion/', views.Save_Question, name="SQ"),
    path('SaveAnswer/', views.Save_APIChatGPT, name="SA"),
]