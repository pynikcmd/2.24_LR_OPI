#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Timer

if __name__ == "__main__":
    timer = Timer(interval=3, function=lambda: print("Message from Timer!"))
    timer.start()
