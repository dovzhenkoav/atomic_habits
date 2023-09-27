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
            RelatedOrRewardValidator(related='related_habit', reward='reward'),
            RelatedIsNiceHabitValidator(related='related_habit'),
            NoRewardOrRelatedOnNiceHabitValidator(is_nice='is_nice', related='related_habit', reward='reward'),
            FrequencyValidator(periodicity='periodicity'),
        ]
