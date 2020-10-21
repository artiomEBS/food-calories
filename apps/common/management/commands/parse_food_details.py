import json
import requests
from django.core.management.base import BaseCommand

BASE_URL = 'https://www.tablicakalorijnosti.ru'
LIST_URL = '{BASE_URL}/foodstuff/filter-list?format=json&page={page_number}&limit={page_limit}'
FOOD_URL = '{BASE_URL}/user/foodstuff/add/form/{food_id}?format=json&default=true'


class Command(BaseCommand):

    @staticmethod
    def _get_food_url(food_id):
        return FOOD_URL.format(**{
            'BASE_URL': BASE_URL,
            'food_id': food_id
        })

    def _log_status_code_error(self, status_code, food_id):
        self.stdout.write(self.style.ERROR(f'ERROR: Ended with status code: {status_code}'
                                           f' at food_id {food_id}'))

    def _log_parsing_notice(self, status_code, food_id, items_count):
        self.stdout.write(self.style.NOTICE(f'Status code: {status_code}'
                                            f' Food_id: {str(food_id).zfill(4)}'
                                            f' Items count: {items_count}'))

    def _log_ended_successful(self):
        self.stdout.write((self.style.SUCCESS(f'Ended successful')))

    def handle(self, *args, **options):
        dump = list()
        open_json = open('food_list.json')
        json_data = json.load(open_json)

        for food in json_data:
            food_id = food['id']
            try:
                response = requests.get(self._get_food_url(food_id))

                if response.status_code != 200:
                    self._log_status_code_error(response.status_code, food_id)
                    break

                data = response.json()['data']

                if not len(data):
                    self._log_ended_successful()
                    break

                self._log_parsing_notice(response.status_code, food_id, len(data))
                dump.append(data)

                with open('food_done_list.json', 'w') as fp:
                    json.dump(dump, fp)
            except:
                with open('food_list_error.json', 'w') as fp:
                    json.dump(dump, fp)
