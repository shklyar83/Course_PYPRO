import time
from decimal import Decimal
from datetime import datetime

print('Як Вас звати?\n')
name = input()

time.sleep(1)
print('Доброго дня, ' + name + '!')

time.sleep(1)
print('Ви хотіли б застрахувати своє авто?')

answer_1 = input()
while answer_1.lower() not in ['так', 'ні']:
    print('Будь ласка, введіть "так" або "ні".')
    answer_1 = input()

if answer_1 == 'ні':
    time.sleep(1)
    print('Добре, ми зателефонуємо Вам наступного місяця. Гарного дня!')
else:
    time.sleep(1)
    print('Добре, тоді я маю поставити Вам декілька питань')

    time.sleep(1)
    print('Введіть будь-ласка марку вашого автомобіля')
    car_name = input()

    time.sleep(1)
    print('Введіть будь-ласка назву моделі')
    car_model = input()

    time.sleep(1)
    print("Який об'єм двигуна у вашого " + car_name + " " + car_model + "?" + " Введіть значення у куб.см")
    v_engine = int(input())
    while v_engine < 50 or v_engine > 10000:
        print('Введіть значення від 50 до 10000')
        v_engine = int(input())

    time.sleep(1)
    print("Введіть рік випуску Вашого автомобіля ?")
    car_age = int(input())
    while car_age < (datetime.now().year - 35) or car_age > datetime.now().year:
        print('Рік випуску може бути від ' + str((datetime.now().year - 35)) + ' до ' + str(datetime.now().year))
        car_age = int(input())

    time.sleep(1)
    print("Вкажіть будь-ласка рік видачі водійського посвідчення")
    drive_age = int(input())
    while drive_age < (datetime.now().year - 50) or drive_age > datetime.now().year:
        print('Рік видачі може бути від ' + str((datetime.now().year - 50)) + ' до ' + str(datetime.now().year))
        drive_age = int(input())

    time.sleep(1)
    print("Чи використовується Ваш " + car_name + " " + car_model + " в таксі ?")
    car_taxi = input()
    while car_taxi.lower() not in ['так', 'ні']:
        print('Будь ласка, введіть "так" або "ні".')
        car_taxi = input()

    time.sleep(1)
    print("Ваш автомобіль переважно використовується у місті ?")
    city_mln = input()
    while city_mln.lower() not in ['так', 'ні']:
        print('Будь ласка, введіть "так" або "ні".')
        city_mln = input()

    BASE_TARIFF = Decimal('2000')
    BASE_V_ENGINE = Decimal('1600')
    BASE_CAR_AGE = Decimal('5')
    BASE_DRIVE_AGE = Decimal('5')

    res_v_engine = \
        Decimal('0.8') if v_engine <= BASE_V_ENGINE * Decimal('0.625') else\
        Decimal('0.9') if v_engine <= BASE_V_ENGINE else\
        Decimal('1') if v_engine <= BASE_V_ENGINE * Decimal('1.376') else\
        Decimal('1.2')

    # res_car_age = \
    #     Decimal('1') if car_age <= BASE_CAR_AGE else \
    #     Decimal('1.05') if car_age <= BASE_CAR_AGE * Decimal('2') else \
    #     Decimal('1.1') if car_age <= BASE_CAR_AGE * Decimal('3') else \
    #     Decimal('1.2')

    res_car_age = \
        Decimal('1') if datetime.now().year - car_age <= BASE_CAR_AGE else \
        Decimal('1.1') if (datetime.now().year - car_age) * Decimal('2') else \
        Decimal('1.2') if (datetime.now().year - car_age) * Decimal('3') else \
        Decimal('1.3')

    res_car_taxi = Decimal('1') if car_taxi == 'ні' else Decimal('1.3')

    res_city_mln = Decimal('0.9') if city_mln == 'ні' else Decimal('1')

    res_drive_age = \
        Decimal('1.2') if drive_age <= BASE_DRIVE_AGE else \
        Decimal('1') if car_age <= BASE_DRIVE_AGE * Decimal('2') else \
        Decimal('0.9') if car_age <= BASE_DRIVE_AGE * Decimal('3') else \
        Decimal('0.8')

    res_polis_sum = BASE_TARIFF * \
        res_v_engine * \
        res_car_age * \
        res_car_taxi * \
        res_city_mln * \
        res_drive_age

    time.sleep(1)
    print(name + ', ми порахували вартість полісу страхування на Ваш' + ' ' + car_name + ' ' + car_model +\
          ', з урахуванням даних, які Ви надали')

    time.sleep(2)
    print('Вартість полісу складає ' + str(res_polis_sum) + 'грн.')

    time.sleep(2)
    print("Ви бажаєте оформити поліс?")
    answer_3 = input()
    while answer_3.lower() not in ['так', 'ні']:
        print('Будь ласка, введіть "так" або "ні".')
        answer_3 = input()

    if answer_3 == 'так':
        time.sleep(1)
        print('Вкажіть будь ласка адресу електронної пошти')
        user_email = input()

        time.sleep(1)
        print('Ми відправили на Вашу ел. скриньку поліс та рахунок на оплату ' + str(res_polis_sum) + ' грн.')

        time.sleep(2)
        print('Дякуємо, що скористались послугами нашої СК, Гарного дня!')
    else:
        print('Дякуємо, що звернулись до нашої СК, ми зателефонуємо Вам наступного місяця')