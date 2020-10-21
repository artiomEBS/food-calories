import json
import requests
import itertools
from django.core.management.base import BaseCommand

BASE_URL = 'https://www.tablicakalorijnosti.ru'
LIST_URL = '{BASE_URL}/foodstuff/filter-list?format=json&page={page_number}&limit={page_limit}'
FOOD_URL = '{BASE_URL}/user/foodstuff/add/form/{food_id}?format=json&default=true'


class Command(BaseCommand):
    help = 'Parse https://www.tablicakalorijnosti.ru product table into json dump'

    @staticmethod
    def _get_page_url(page_number, page_limit=1000):
        return LIST_URL.format(**{
            'BASE_URL': BASE_URL,
            'page_limit': page_limit,
            'page_number': page_number

        })

    def _log_status_code_error(self, status_code, page_number):
        self.stdout.write(self.style.ERROR(f'ERROR: Ended with status code: {status_code}'
                                           f'at page {page_number}'))

    def _log_parsing_notice(self, status_code, page_number, items_count):

        self.stdout.write(self.style.NOTICE(f'Status code: {status_code}'
                                            f' Page number: {str(page_number).zfill(4)}'
                                            f' Items count: {items_count}'))

    def _log_ended_successful(self):
        self.stdout.write((self.style.SUCCESS(f'Ended successful')))

    def handle(self, *args, **options):
        dump = list()

        for page_number in itertools.count():
            response = requests.get(self._get_page_url(page_number))

            if response.status_code != 200:
                self._log_status_code_error(response.status_code, page_number)
                break

            data = response.json()['data']

            if not len(data):
                self._log_ended_successful()
                break

            self._log_parsing_notice(response.status_code, page_number, len(data))

            dump.extend(data)

            with open('food_list.json', 'w') as fp:
                json.dump(dump, fp)
