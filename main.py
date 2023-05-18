import threading
import pygame
import time
import math
import random

ON = True
delay = 0.0250
deg_to_rad = math.pi / 180

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 500))
        self.polygons = []
        self.polygons.append(self.Polygon(self.screen, (100, 100, 100), [(100, 100), (100, 150), (150, 150), (150, 100)]))
        self.polygons.append(self.Polygon(self.screen, (255, 100, 100), [(400, 400), (400, 350), (350, 350), (350, 400)]))
        threading.Thread(target=self.update).start()

    def update(self):
        while ON:
            for polygon in self.polygons:
                polygon.rotate((250, 250), 5)
                polygon.draw()
            pygame.display.flip()
            time.sleep(delay)

    class Polygon:
        def __init__(self, screen, color, corners):
            self.screen = screen
            self.color = color
            self.corners = corners

        def draw(self):
            pygame.draw.polygon(self.screen, self.color, self.corners)

        def rotate(self, center, degree):
            for i in range(len(self.corners)):
                x, y = self.corners[i]
                radians = math.atan2((y - center[1]), (x - center[0])) + degree * math.pi / 180
                hypotenuse = math.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
                x = center[0] + hypotenuse * math.cos(radians)
                y = center[1] + hypotenuse * math.sin(radians)
                self.corners[i] = (x, y)

game = Game()


while ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ON = False
            pygame.quit()
            quit()

    time.sleep(delay)
            
