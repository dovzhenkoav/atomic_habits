from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from habits.permissions import IsOwner


class PersonalHabitsListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Habit.objects.all()
        return Habit.objects.filter(created_by=self.request.user)


class PublicHabitsListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    # queryset = Habit.objects.all()
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer



class HabitUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
