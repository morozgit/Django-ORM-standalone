import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    passcards = Passcard.objects.all()
    print(passcards[0].owner_name, passcards[0].passcode, passcards[0].created_at, passcards[0].is_active)
    # active_passcards = []
    # for passcard in passcards:
    #     if passcard.is_active:
    #         active_passcards.append(passcard)
    print('Активных пропусков', len(passcards.filter(is_active=True)))
    