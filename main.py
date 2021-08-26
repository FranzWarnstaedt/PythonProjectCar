import pygame
import gpio
import camera
import multiprocessing


pygame.init()

print("Nutze die Pfeiltasten um das Auto zu bewegen!")

optionButton = False
done = False
clock = pygame.time.Clock()
pygame.joystick.init()

while not done:
    clock.tick(20)
    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.JOYHATMOTION:
            if event.value == (0, -1):
                print("forward")
                p1.start()
            if event.value == (0, 1):
                print("backward")
                p2.start()
            if event.value == (-1, 0):
                print("steering left")
                p3.start()
            if event.value == (1, 0):
                print("steering right")
                p4.start()
            if event.value == (0, 0):
                gpio.stop()
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:
                if not optionButton:
                    p5.start()
                    optionButton = True
                if optionButton:
                    camera.stop()
                    optionButton = False

            if event.button == 3:  # Dreieck
                camera.photo()

        # if event.button == 0: #Viereck

        # if event.button == 2: #Kreis

pygame.quit()
