import os
from core.settings import FIXTURE_DIRS
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = 'Create load init data to database'

    @staticmethod
    def do_handler():
        errors = []
        init_files = _get_folder_files()
        print(f"Start load data to db from files: {','.join(init_files)}")
        for file in init_files:
            try:
                call_command("loaddata", file)
                print(f"Successfully loaded data from {file}!")
            except Exception as e:
                errors.append(f"Error[{file}]: {e.__str__()}")

        if len(errors) > 0:
            print(f"There was a problem in places like this: {''.join(errors)}")

        print(f"Data loading finished!")

    def handle(self, *args, **options):
        Command.do_handler()


def _get_folder_files():
    res = []
    try:
        for path in FIXTURE_DIRS:
            for (p, f, f_list) in os.walk(path):
                for f_name in f_list:
                    res.append(f"{p}/{f_name}")
    except Exception as e:
        print(f"Error run os.walk() for read all files in directory! Error: {e.__str__()}")
    return res
