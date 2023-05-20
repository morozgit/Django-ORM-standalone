import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit
from django.utils import timezone
import datetime



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
    
    visits = Visit.objects.all()
    # print(visits)
    print('Кто не вышел', visits.filter(leaved_at=None))
    print('Текущее время', timezone.localtime())
    # for visit in visits:
        # if visit.leaved_at is not None:
            # delta = timezone.localtime() - timezone.localtime(visit.entered_at)
            # print(visit)
            # print('Зашёл в хранилище, время по Москве:\n{0}'.format(timezone.localtime(visit.entered_at)), '\nНаходится в хранилище:\n{0}'.format(visit.get_duration(visit)))
    # print(len(visits), len(visits.filter(leaved_at=None)))
    print('Кто в хранилище:')
    for visit in visits:
        if visit.leaved_at is None:
            print(visit.passcard.owner_name,end='\n')

    
    p = passcards.get(passcode=passcards[0].passcode)
    one_person_visit = visits.filter(passcard=p)
    print(one_person_visit)
    # for one_visit in one_person_visit:
    #     if one_visit.is_visit_long(one_visit,10):
    #         print('Визиты дольше 10 мин', one_visit)
    #     elif one_visit.is_visit_long(one_visit,10):
    #         print('Визиты дольше 1000 мин', one_visit)
    #     elif(one_visit.leaved_at is None):
    #         print('Еще в хранилище')
    
    