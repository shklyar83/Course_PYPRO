import logging

logger = logging.getLogger('order_processing') #створюємо логер
logger.setLevel(logging.DEBUG) # присвоюємо логеру рівень

file_handler = logging.FileHandler('log_orders.log') # створюємо нендлер (запис у файл)
file_handler.setLevel(logging.INFO) # присвоюємо хендлеру рівень

console_handler = logging.StreamHandler() # створюємо нендлер (запис у консоль)
console_handler.setLevel(logging.DEBUG) # присвоюємо хендлеру рівень

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') # створюємо форматор (код запису у документації)
file_handler.setFormatter(formatter) # присвоюємо хендлеру форматор
console_handler.setFormatter(formatter) # присвоюємо хендлеру форматор

logger.addHandler(file_handler) # зв'язуємо логер і хендлер
logger.addHandler(console_handler) # зв'язуємо логер і хендлер

# далі працюємо тільки з логером

import uuid

class Order:
    def __init__(self, order_type, customer_name):
        self.id = uuid.uuid4()
        self.order_type = order_type
        self.customer_name = customer_name

    def process(self):
        if self.order_type == 'delivery':
            logger.info(f'delivery: {self.id}; {self.customer_name}')
        elif self.order_type == 'in':
            logger.info(f'in: {self.id}; {self.customer_name}')
        elif self.order_type == 'to-go':
            logger.info(f'to-go: {self.id}; {self.customer_name}')
        else:
            logger.debug(f'unknown order type : {self.id}; {self.customer_name}')


if __name__ == '__main__':
    order_1 = Order('delivery', 'Petro')
    order_2 = Order('in', 'Ivan')
    order_3 = Order('to-go', 'Oleh')
    order_4 = Order('out', 'Max')

    order_1.process()
    order_2.process()
    order_3.process()
    order_4.process()