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

    def __set_high(self):
        GPIO.output(self.pin_bell, True)

    def __set_low(self):
        GPIO.output(self.pin_bell, False)

    def ring_once(self):
        self.__set_high()
        time.sleep(self.ring_time)
        self.__set_low()

    def ring_times(self, times=1):
        for i in xrange(0, times):
            self.ring_once()
            time.sleep(self.ring_interval)

    def ring(self, second):
        times = int(second / (self.ring_time + self.ring_interval))
        self.ring_times(times)
