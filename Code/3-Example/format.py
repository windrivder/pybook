#!/usr/bin/env python3
# -*- coding: utf-8 -*-

format_one = '{0}, {1}'.format('Windrivder', 21)

format_two = '{name}, {age}'.format(age=18, name='Windrivder')


class Person(object):
    """docstring for Person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'This guy is {self.name}, is {self.age} years old'.format(self=self)


format_three = '{:15} | {:^9} | {:^9}'.format('', 'lat', 'lng')

format_four = '{:15} | {:9.4f} | {:9.4f}'.format(
    'Tokyo', -23.547778, -46.635833)

format_five = '{:b}, {:d}, {:o}, {:x}'.format(17, 17, 17, 17)

format_six = '{:,}'.format(1234567890)

if __name__ == '__main__':
    print(format_one)
    print(format_two)
    print(format_three)
    print(format_four)
    print(format_five)
    print(format_six)
    print(str(Person('Windrivder', 22)))
