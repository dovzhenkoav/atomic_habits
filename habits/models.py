from django.db import models
from users.models import User



class Habit(models.Model):
    PERIODICITY_CHOICES = [
        ('1', 'ежедневно'),
        ('2', 'через день'),
        ('3', 'раз в три дня'),
        ('4', 'раз в четыре дня'),
        ('5', 'раз в пять дня'),
        ('6', 'раз в шесть дней'),
        ('7', 'раз в семь дней'),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    place = models.CharField(max_length=128, verbose_name='место')
    time = models.TimeField(verbose_name='время выполнения')
    action = models.CharField(max_length=128, verbose_name='действие')
    is_nice = models.BooleanField(verbose_name='признак приятной привычки')
    related_habit = models.IntegerField(verbose_name='ид связанной привычки')
    periodicity = models.CharField(max_length=1, choices=PERIODICITY_CHOICES, verbose_name='перидочность')
    reward = models.CharField(max_length=128, verbose_name='награда')
    duration = models.CharField(max_length=128, verbose_name='продолжительность')
    is_public = models.BooleanField(verbose_name='признак публичной привычки')

    def __str__(self):
        return f'{self.place} {self.time} {self.action} {self.created_by}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
