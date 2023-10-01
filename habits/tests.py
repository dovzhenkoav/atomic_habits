from rest_framework.test import APITestCase
from rest_framework import status
import requests

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='admin@ya.ru')
        self.user.set_password('1q2w3e')
        self.user.save()

        response = self.client.post('/users/token/', {'email': 'admin@ya.ru', 'password': '1q2w3e'})
        token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        # add data
        data = {
                "place": "кухня",
                "time": "11:30",
                "action": "заварить чай",
                "periodicity": "4",
                "duration": 120,
                "is_public": False,
                "notification_tgid": 980431310
            }
        self.client.post('/habits/create/', data=data)


    def test_create_habit(self):
        data = {
                "place": "кухня",
                "time": "11:30",
                "action": "заварить чай",
                "periodicity": "4",
                "duration": 120,
                "is_public": False,
                "notification_tgid": 980431310
            }

        response = self.client.post('/habits/create/', data=data)
        response = response.json()


        self.assertEqual(response,
                         {
                             "id": 2,
                             "place": "кухня",
                             "time": "11:30:00",
                             "action": "заварить чай",
                             "is_nice": False,
                             "related_habit": None,
                             "periodicity": "4",
                             "reward": None,
                             "duration": 120,
                             "is_public": False,
                             "notification_tgid": 980431310
                         })

    def test_get_my_habits(self):
        response = self.client.get('/habits/my/')
        response = response.json()
        self.assertEqual(response,
                          {'count': 1,
                              'next': None,
                              'previous': None,
                              'results': [{'action': 'заварить чай',
                                                           'duration': 120,
                                                           'id': 3,
                                                           'is_nice': False,
                                                           'is_public': False,
                                                           'notification_tgid': 980431310,
                                                           'periodicity': '4',
                                                           'place': 'кухня',
                                                           'related_habit': None,
                                                           'reward': None,
                                                           'time': '11:30:00'}]}

                         )

    def test_get_public_habits(self):
        response = self.client.get('/habits/public/')
        response = response.json()
        self.assertEqual(response, {'count': 0, 'next': None, 'previous': None, 'results': []})

    def test_update_habit(self):
        data = {
                "place": "кухня",
                "time": "11:30",
                "action": "заварить чай",
                "periodicity": "4",
                "duration": 120,
                "is_public": True,
                "notification_tgid": 980431310
            }

        response = self.client.put('/habits/update/5/', data=data)
        response = response.json()

        self.assertEqual(response, {'action': 'заварить чай',
                                    'duration': 120,
                                    'id': 5,
                                    'is_nice': False,
                                    'is_public': True,
                                    'notification_tgid': 980431310,
                                    'periodicity': '4',
                                    'place': 'кухня',
                                    'related_habit': None,
                                    'reward': None,
                                    'time': '11:30:00'})

    def test_xdelete_habit(self):
        response = self.client.delete('/habits/delete/6/')
        response = response.status_code

        self.assertEqual(response, 204)
