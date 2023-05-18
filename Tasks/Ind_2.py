#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Lock, Thread
from queue import Queue

EPSILON = 10 ** (-7)  # точность вычислений
q = Queue()
lock = Lock()


def sum(x):
    lock.acquire()
    n = 1
    sum = 1
    temp = x
    while abs(temp) >= EPSILON:
        sum += temp
        n += 1
        temp *= x
    q.put(sum)
    lock.release()


def check_res(res, check_res):
    print(f"Значение суммы для x = 0.7: {res}")
    print(f"Проверка: {check_res}")


def main():
    x = 0.7
    y = 1 / (1 - x)

    # Создаем потоки
    thread1 = Thread(target=sum, args=(x,)).start()
    thread2 = Thread(target=check_res, args=(q.get(), y)).start()


if __name__ == "__main__":
    main()
