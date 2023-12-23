#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def type_transform(selected_type):
    """
    Функция принимает строковое значение. Рекомендуется
    использовать значения 'tuple' или 'list'
    """

    def transform(numbers):
        """
        Функция принимает числовые значения и, в зависимости от
        указанного строкового значения внешней функции, преобразует
        введённые значения в кортеж или список. Возвращает преобразованный
        результат
        """

        collection = [int(value) for value in numbers]

        if selected_type == 'tuple':
            return tuple(collection)
        elif selected_type == 'list':
            return list(collection)
        
    return transform

if __name__ == "__main__":
    selected_type = type_transform(input("Введите тип (tuple/list): "))
    collection = selected_type(input("Введите числа через пробел: ").split())
    print(f"Результат: {collection}")
    print(f"Выбранный тип - {type(collection)}")
