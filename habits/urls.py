from django.urls import path

from habits.apps import HabitsConfig
from habits import views

app_name = HabitsConfig.name


urlpatterns = [
    path('my/', views.PersonalHabitsListAPIView.as_view(), name='my-habits-list'),
    path('public/', views.PublicHabitsListAPIView.as_view(), name='public-habits-list'),
    path('create/', views.HabitCreateAPIView.as_view(), name='create-habit'),
    path('update/<int:pk>', views.PublicHabitsListAPIView.as_view(), name='update-habit'),
    path('delete/<int:pk>', views.PublicHabitsListAPIView.as_view(), name='delete-habit'),
]
