import sys, pygame
import math
import random
from screeninfo import get_monitors

def process_keyboard():
    pressed = pygame.key.get_pressed()
    pass

def main():
    pygame.init()


    speed = [2,2]
    black = 0,0,0
    displayInfo = pygame.display.Info()
    size = width, height = displayInfo.current_w, displayInfo.current_h
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    center = width / 2, height / 2



    r = 100
    angle = 0
    angle_increment = math.pi / 100
    previous_point, current_point = (0, 0)
    points = []
    clock_thing = pygame.time.Clock()
    while True:
        clock_thing.tick(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        screen.fill(black)
        #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(center[0] - 10, center[1] - 1, 20, 20), 1)
        while True:
            #previous_point = current_point
            #current_point = (int(r * math.cos(angle) + center[0]), int(r * math.sin(angle) + center[1]))
            tmp_r = r + random.gauss(r * 0.3, random.gauss(1, 4))

            points.append((int(tmp_r * math.cos(angle) + center[0]),
                           int(tmp_r * math.sin(angle) + center[1])))
            #screen.set_at(current_point, (0, 255, 0))
            angle = (angle + angle_increment)
            if angle > 2 * math.pi:
                angle = 0
                break
        pygame.draw.lines(screen, (255,0,0), True, points)
        points = []

        pygame.display.flip()
        process_keyboard()

if __name__ == '__main__': main()