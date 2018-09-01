import sys, pygame
import math
import time
from smartmirror import pointshape, transfer
import random
from smartmirror.widgets import containerwidget, datetimewidget, weatherwidget

FPS = 60

def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Get display size
    display_info = pygame.display.Info()
    size = width, height = display_info.current_w, display_info.current_h
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    # Widget container
    container_size = container_width, container_height = 300, height
    container_anchor = transfer.Transfer(((width - container_width), 0), (width, 0), 0.2)

    w_container = containerwidget.WidgetContainer(container_size)
    w_container.fill(pygame.Color(255, 255, 255))
    w_container.add_widget(datetimewidget.TimeWidget((280, 100)))
    w_container.add_widget(weatherwidget.WeatherWidget((280, 50), _owm_api_key='asdf', ))

    # e = entity.Entity(width // 2, height // 2, 200, 100 * 0.3, 0, 2)
    radius_transfer = transfer.Transfer(1, 200, 10)
    e = pointshape.Circle(1, width / 2, height / 2, _points = 10)
    entity_last_refresh = 0
    entity_show = True
    red_green = transfer.Transfer((0, 255, 0), (255, 0, 0), 10)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    container_anchor.reverse()
                if event.key == pygame.K_e:
                    e._show = not e._show
                    radius_transfer.reverse()
                if event.key == pygame.K_r or event.key == pygame.K_g:
                    red_green.reverse()


        screen.fill(pygame.Color(0, 0, 0))
        r = radius_transfer.next
        if (time.time() - entity_last_refresh) > 0.01 and entity_show:
            entity_last_refresh = time.time()

            e.radius = r
            # e.point_distance = min(r, 10)
            points = e.calculate_points(random.uniform(0, 2*math.pi))
            if r == radius_transfer._end and e.num_points < 100:
                e.num_points += 1


        # if e._radius_current < e._radius_max:
        for p in points:
            f = lambda x : x+random.gauss(0,1)
            screen.set_at(tuple(map(int, map(f, p))), red_green.next)
        # else:
        #     pygame.draw.lines(screen, colors['green'], True, points)


        for widget in w_container.widgets:
            widget.update_widget()
        w_container.draw_widgets()
        screen.blit(w_container, container_anchor.next)
        pygame.display.flip()

if __name__ == '__main__': main()