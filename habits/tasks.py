import requests
from celery import shared_task
import json
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.conf import settings


@shared_task
def send_tg_message(chat_id: int, message: str):
    endpoint = f'https://api.telegram.org/bot{settings.BOT_API_TOKEN}/sendMessage'

    params = {
        'chat_id': chat_id,
        'text': message,
    }
    response = requests.post(endpoint, params=params)


def set_schedule(chat_id: int, message: str, periodicity_days: int, *args, **kwargs):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=periodicity_days,
        period=IntervalSchedule.DAYS
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name='Send tg message',
        task='habits.tasks.send_tg_message',
        args=(chat_id, message),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=3)
    )

