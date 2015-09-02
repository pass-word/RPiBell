#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import RPi.GPIO as GPIO
import time


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class RPiBell(object):
    __metaclass__ = Singleton
    pin_bell = 0
    ring_time = 0.5
    ring_interval = 0.5

    def __init__(self, pin_bell=18):
        GPIO.setmode(GPIO.BCM)
        self.pinBell = pin_bell
        GPIO.setup(self.pin_bell, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def __setHigh(self):
        GPIO.output(self.pin_bell, True)

    def __setLow(self):
        GPIO.output(self.pin_bell, False)

    def ringOnce(self):
        self.__setHigh()
        time.sleep(self.ring_time)
        self.__setLow()

    def ring(self, second):
        times = second / (self.ring_time + self.ring_interval)
        for i in range(0, times):
            self.ringOnce()
            time.sleep(self.ring_interval)
