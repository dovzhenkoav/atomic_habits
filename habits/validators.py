from rest_framework.serializers import ValidationError

from habits.models import Habit


class RelatedOrRewardValidator:
    def __init__(self, related, reward):
        self.related = related
        self.reward = reward

    def __call__(self, value):
        related = dict(value).get(self.related)
        reward = dict(value).get(self.reward)
        if related and reward:
            raise ValidationError('Не может быть у привычки И связанная привычка И награда.')


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        max_duration = 120
        duration = dict(value).get(self.field)

        if duration > max_duration:
            raise ValidationError(f'Длительность действия не должна составлять более {max_duration} секунд. Указано: {duration}')



class RelatedIsNiceHabitValidator:
    def __init__(self, related):
        self.related = related

    def __call__(self, value):
        related = dict(value).get(self.related)
        if related:
            rel_habit = Habit.objects.get(pk=related)
            if not rel_habit.is_nice:
                ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class NoRewardOrRelatedOnNiceHabitValidator:
    def __init__(self, is_nice, related, reward):
        self.is_nice = is_nice
        self.related = related
        self.reward = reward

    def __call__(self, value):
        is_nice = dict(value).get(self.is_nice)
        related = dict(value).get(self.related)
        reward = dict(value).get(self.reward)
        if is_nice:
            if related or reward:
                raise ValidationError('У приятной привычки не может быть связанной привычки или вознаграждения.')

class FrequencyValidator:
    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, value):
        periodicity = dict(value).get(self.periodicity)
        if int(periodicity) > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем раз в семь дней.')


