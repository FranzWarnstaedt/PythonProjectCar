import pygame 
import RPi.GPIO as GPIO         

pygame.init()

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.OUT) #IN2
GPIO.setup(23,GPIO.OUT) #IN1
GPIO.setup(27,GPIO.OUT) #IN3
GPIO.setup(22,GPIO.OUT) #IN4
GPIO.setup(25,GPIO.OUT) #ENA
GPIO.setup(17,GPIO.OUT) #ENB

right1 = GPIO.PWM(24,100)
right2 = GPIO.PWM(23,100)
left1 = GPIO.PWM(27,100)
left2 = GPIO.PWM(22,100)
ena = GPIO.PWM(25,100)
enb = GPIO.PWM(17,100)

right1.start(0)
right2.start(0)
left1.start(0)
left2.start(0)
ena.start(100)
enb.start(100)

print("Drücke 'f' um vorwärts zu fahren \nDrücke 'b' um rückwarts (backwards) zu fahren \nDrücke 'r' um nach rechts zu lenken \nDrücke 'l' um nach links zu lenken \nDrücke 's' um zu stoppen")

done = False
pygame.joystick.init()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.QUIT
            pygame.quit()
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 11:
                print("forward")
                ena.ChangeDutyCycle(100)
                enb.ChangeDutyCycle(100)
                right1.ChangeDutyCycle(0)
                right2.ChangeDutyCycle(100)
                left1.ChangeDutyCycle(0)
                left2.ChangeDutyCycle(100)
            if event.button == 12:
                print("backward")
                ena.ChangeDutyCycle(100)
                enb.ChangeDutyCycle(100)
                right1.ChangeDutyCycle(100)
                right2.ChangeDutyCycle(0)
                left1.ChangeDutyCycle(100)
                left2.ChangeDutyCycle(0)
            if event.button == 13:
                print("steering left")
                ena.ChangeDutyCycle(100)
                enb.ChangeDutyCycle(100)
                right1.ChangeDutyCycle(0)
                right2.ChangeDutyCycle(100)
                left1.ChangeDutyCycle(100)
                left2.ChangeDutyCycle(0)
            if event.button == 14:
                print("steering right")
                ena.ChangeDutyCycle(100)
                enb.ChangeDutyCycle(100)
                right1.ChangeDutyCycle(100)
                right2.ChangeDutyCycle(0)
                left1.ChangeDutyCycle(0)
                left2.ChangeDutyCycle(100)                                    
        if event.type == pygame.JOYBUTTONUP:
            print("stop")
            ena.ChangeDutyCycle(0)
            enb.ChangeDutyCycle(0)   
