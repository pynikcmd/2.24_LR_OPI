#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
from queue import Queue
from threading import Lock, Thread


def waiter():
    lock.acquire()  # Захватываем блокировку
    orders = []
    while not q.empty():  # Пока очередь не пуста
        order = q.get()  # Извлекаем заказ из очереди
        status = random.choice(["Готовится", "Готов", "Доставляется"])  # Случайным образом выбираем статус заказа
        print(f"Официант принял заказ: {order}, Состояние заказа: {status}")
        orders.append({
            "Заказ": order,
            "Состояние": status
        })

    for order in orders:
        if order["Состояние"] != "Готов":
            print(f"Заказ {order['Заказ']} ожидает доставку")

    lock.release()  # Освобождаем блокировку


def customer(menu):
    lock.acquire()  # Захватываем блокировку
    menu = menu
    for _ in range(5):
        order = random.choice(menu)  # Случайным образом выбираем заказ из меню
        q.put(order)  # Помещаем заказ в очередь
    lock.release()  # Освобождаем блокировку


if __name__ == "__main__":
    menu = ['Пицца', 'Салат', 'Суп', 'Стейк']
    lock = Lock()  # Создаем объект блокировки
    q = Queue()  # Создаем очередь

    # Запускаем поток
    Thread(target=customer, args=(menu,)).start()
    Thread(target=waiter).start()
