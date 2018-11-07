# import RPi.GPIO as GPIO

import time
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, GPIO.OUT)


def blinkshort():
    print('.',end='')


def blinklong():
    print('-', end='')


def blink(type):
    if type == 1:
        blinkshort()
    elif type == 2:
        blinklong()
    elif type == 7:
        blinklong()
        blinklong()
        blinkshort()


def space_letter():
    blink(2)


def space_word():
    blink(7)

def A():
    blinks = [1, 2]
    for x in range(len(blinks)):
        blink(blinks[x])


def B():
    blinks = [2,1,1,1]
    for x in range(len(blinks)):
        blink(blinks[x])


def C():
    blinks = [2,1,2,1]
    for x in range(len(blinks)):
        blink(blinks[x])

def D():
    blinks = [2,1,1]
    for x in range(len(blinks)):
        blink(blinks[x])

def E():
    blinks = [1]
    for x in range(len(blinks)):
        blink(blinks[x])

def F():
    blinks = [1,1,2,1]
    for x in range(len(blinks)):
        blink(blinks[x])

def G():
    blinks = [2,2,1]
    for x in range(len(blinks)):
        blink(blinks[x])
def H():
    blinks = [1,1,1,1]
    for x in range(len(blinks)):
        blink(blinks[x])

def I():
    blinks = [1,1]
    for x in range(len(blinks)):
        blink(blinks[x])
def J():
    blinks = [1,2,2,2]
    for x in range(len(blinks)):
        blink(blinks[x])

def K():
    blinks = [2,1,2]
    for x in range(len(blinks)):
        blink(blinks[x])
def L():
    blinks = [1,2,1,1]
    for x in range(len(blinks)):
        blink(blinks[x])
def M():
    blinks = [2,2]
    for x in range(len(blinks)):
        blink(blinks[x])
def N():
    blinks = [2,1]
    for x in range(len(blinks)):
        blink(blinks[x])
def O():
    blinks = [2,2,2]
    for x in range(len(blinks)):
        blink(blinks[x])
def P():
    blinks = [1,2,2,1]
    for x in range(len(blinks)):
        blink(blinks[x])
def Q():
    blinks = [2,2,1,2]
    for x in range(len(blinks)):
        blink(blinks[x])
def R():
    blinks = [1,2,1]
    for x in range(len(blinks)):
        blink(blinks[x])
def S():
    blinks = [1,1,1]
    for x in range(len(blinks)):
        blink(blinks[x])
def T():
    blinks = [2]
    for x in range(len(blinks)):
        blink(blinks[x])
def U():
    blinks = [1,1,2]
    for x in range(len(blinks)):
        blink(blinks[x])
def V():
    blinks = [1, 1, 1, 2]
    for x in range(len(blinks)):
        blink(blinks[x])
def W():
    blinks = [1, 2, 2]
    for x in range(len(blinks)):
        blink(blinks[x])
def X():
    blinks = [2,1, 1, 2]
    for x in range(len(blinks)):
        blink(blinks[x])

def Y():
    blinks = [2,1,2,2]
    for x in range(len(blinks)):
        blink(blinks[x])
def Z():
    blinks = [2,2,1,1]
    for x in range(len(blinks)):
        blink(blinks[x])


S()
space_letter()
O()
space_letter()
S()
space_word()