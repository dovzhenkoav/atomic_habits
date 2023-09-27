from rest_framework import serializers

from habits.models import Habit
from habits.validators import *


class HabitSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            DurationValidator(field='duration'),
        ]
