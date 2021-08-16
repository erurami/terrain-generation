import pygame
import random

def subdivision_mountain(moutain_vertexes):
    global MOUNTAIN_HEIGHT
    global time
    subdivided_mountain_vertexes = []
    noise_scale = MOUNTAIN_HEIGHT / 2
    for i in range(time):
        noise_scale /= 1.8
        noise_scale = int(noise_scale)
    
    for vertex_index in range(len(mountain_vertexes)):
        if vertex_index + 1 >= len(mountain_vertexes):
            subdivided_mountain_vertexes.append(mountain_vertexes[vertex_index])
            break
        
        vertex1 = mountain_vertexes[vertex_index]
        vertex2 = mountain_vertexes[vertex_index + 1]
        
        subdivided_mountain_vertexes.append(vertex1)
        
        subdivided_mountain_vertexes.append([int((vertex1[0] + vertex2[0]) / 2), int((vertex2[1] + vertex1[1]) / 2 + random.randint(-noise_scale, noise_scale))])
    return subdivided_mountain_vertexes

MOUNTAIN_HEIGHT = int(input("height?"))
LOOP_TIMES = int(input("loop_time?"))

pygame.init()
state = "normal"

while state != "end":
    mountain_vertexes = [[0, 300], [400, 300], [800, 300]]
    
    screen = pygame.display.set_mode((800,600))
    myclock = pygame.time.Clock()
    time = 0
    state = "normal"
    
    while state == "normal":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = "end"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state = "reset"
        screen.fill((0,0,0))
        if time <= LOOP_TIMES:
            mountain_vertexes = subdivision_mountain(mountain_vertexes)
            time += 1
        pygame.draw.polygon(screen, (255, 255, 255), mountain_vertexes)
        pygame.display.flip()
        myclock.tick(60)

pygame.quit()

