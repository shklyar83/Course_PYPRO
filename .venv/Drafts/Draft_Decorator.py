def bold_greetings(func):
    def inner(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    return inner


def italic_greetings(func):
    def inner(*args, **kwargs):
        return f'<i>{func(*args, **kwargs)}</i>'
    return inner

@italic_greetings
@bold_greetings
def greetings(name):
    return f'Hello, {name}'

@bold_greetings
@italic_greetings
def name_surname(name, surname):
    return f'{surname} {name[0]}.'

print(greetings('Oleh'))
print(name_surname('Oleh', 'Tymchuk'))