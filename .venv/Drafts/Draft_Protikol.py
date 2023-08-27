# #1
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    surname: str
    date_of_birth: str

from student import Student


class Group:

    def __init__(self, title: str):
        self.title = title
        self.__students = []

    def add(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError()

        self.__students.append(student)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__students[item]
        if isinstance(item, slice):
            return self.__students[item]
        raise TypeError()

    def __len__(self):
        return len(self.__students)

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.__students))

import student
import courses


if __name__ == '__main__':
    st_1 = student.Student('Ivan1', 'Ivanov', '12.01.2000')
    st_2 = student.Student('Ivan2', 'Ivanov', '12.01.2000')
    st_3 = student.Student('Ivan3', 'Ivanov', '12.01.2000')
    st_4 = student.Student('Ivan4', 'Ivanov', '12.01.2000')
    st_5 = student.Student('Ivan5', 'Ivanov', '12.01.2000')
    st_6 = student.Student('Ivan6', 'Ivanov', '12.01.2000')
    st_7 = student.Student('Ivan7', 'Ivanov', '12.01.2000')

    group = courses.Group('Python')
    group.add(st_1)
    group.add(st_2)
    group.add(st_3)
    group.add(st_4)
    group.add(st_5)
    group.add(st_6)
    group.add(st_7)

    for student in group:
        print(student)


# #2

class MySequence:

    def __init__(self, n):
        if not isinstance(n, int):
            raise TypeError()
        if n < 0:
            raise ValueError()
        self.n = n

    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 <= item < self.n:
                return item * 10
            raise IndexError()

        if isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or self.n
            step = item.step or 1

            if step < 0:
                raise IndexError()
            if stop > self.n:
                raise IndexError()

            tmp = []
            for i in range(start, stop, step):
                tmp.append(i * 10)
            return tmp

        raise TypeError()

    def __len__(self):
        return self.n


x = MySequence(10)
print(x[2:])


