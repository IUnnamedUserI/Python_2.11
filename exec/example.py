#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def outer_func(a):
    def inner_func(b):
        return a + b
    
    return inner_func


if __name__ == "__main__":
    temp = outer_func(10)
    result = temp(5)
    print(f"Результат: {result}")
    