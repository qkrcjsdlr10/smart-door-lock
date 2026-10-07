#import RPi.GPIO as GPIO
import time
from threading import Thread
class Buzzer:
    pin = 12
    # 도,레,미,파,솔,라,시,도 주파수 값
    scale = [261, 294, 329, 349, 440, 493, 523]
    list = [4, 4, 5, 5, 4]

    def __init__(self):
        print("--- Buzzer Init ---")
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(pin, GPIO.OUT)

    def Alarm(self):
        print("--- Buzzer Alaram ---")
        # try:
        #     buzzer = GPIO.PWM(pin, 100)
        #     buzzer.start(100)
        #     buzzer.ChangeDutyCycle(90)
        #
        #     for i in range(5):
        #         buzzer.ChangeDutyCycle(scale[list[i]])
        #         time.sleep(0.5)
        #
        #     buzzer.stop()
        # finally:
        #     GPIO.cleanup()

class ServoMotor:
    pin = 24

    def __init__(self):
        print("--- ServoMotor Init ---")
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(pin, GPIO.OUT)

    def OpenDoor(self):
        print("--- Door Open ---")
        # try:
        #     GPIO.output(pin, GPIO.HIGH)
        #     time.sleep(1)
        #     GPIO.output(pin, GPIO.LOW)
        # finally:
        #     GPIO.cleanup()

    def CloseDoor(self):
        print("--- Door Close ---")
        # try:
        #     GPIO.output(pin, GPIO.LOW)
        # finally:
        #     GPIO.cleanup()

class UltraSonic:
    trigPin = 13
    echoPin = 19
    def __init__(self):
        print("--- UltraSonic Init ---")
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(trigPin, GPIO.OUT)
        # GPIO.setup(echoPin, GPIO.IN

    def StartThread(self):
        print("--- Start Check Thread ---")


    def CheckDistance(self):
        print("--- UltraSonic CheckDistance ---")
        # try:
        #     GPIO.output(trigPin, False)
        #     time.sleep(0.5)
        #
        #     GPIO.output(trigPin, True)
        #     time.sleep(0.000001)
        #     GPIO.output(trigPin, False)
        #
        #     while GPIO.input(echoPin) == 0:
        #         pulse_start = time.time()
        #
        #     while GPIO.input(echoPin) == 1:
        #         pulse_end = time.time()
        #
        #     pulse_duration = pulse_end - pulse_start
        #     # 거리 = 시간 * 속도 --- 소리 340m/s = 34,000cm/s
        #     distance = pulse_duration * 17000
        #     distance = round(distance, 2)
        # if(distance <= 50):

        # finally:
        #     GPIO.cleanup()
        time.sleep(0.5)
        return True


class MainController:
    def __init__(self):
        Buzzer.__init__(self)
        ServoMotor.__init__(self)
        UltraSonic.__init__(self)