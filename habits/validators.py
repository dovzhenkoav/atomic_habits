from rest_framework.serializers import ValidationError

from habits.models import Habit


class RelatedOrRewardValidator:
    pass


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        max_duration = 120
        duration = dict(value).get(self.field)

        if duration > max_duration:
            raise ValidationError(f'Длительность действия не должна составлять более {max_duration} секунд. Указано: {duration}')



class RelatedIsNiceHabitValidator:
    pass


class NoRewardOrRelatedOnNiceHabitValidator:
    pass

class FrequencyValidator:
    pass

