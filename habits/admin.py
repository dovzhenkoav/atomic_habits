from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('place', 'time', 'action', 'is_nice', 'periodicity', 'reward', 'duration', 'created_by', 'is_public')
