import pymunk               # Import pymunk..
import pygame
import random

pygame.init()

display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
example1 = False
example2 = False
example3 = False
Intro_page = True
Examples_page = False
Intro = True
ex1 = True
ex2 = True
ex3 = True
Example = True
Font1 = pygame.font.Font(None, 100)

def Intro_page():
        FPS = 80
        global Intro
        while Intro == True:

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        Intro = False
                                
                        display.fill((0, 0, 0))
                        BodyText = "Fyzipek"
                        BodyGraphics = Font1.render(BodyText, True, [0, 255, 255])  #- create image of text (text, smoothing, color)

                        display.blit(BodyGraphics, [250, 200])
                        pygame.display.update()
                        clock.tick(FPS)
                        Keyboard = pygame.key.get_pressed()  #- check the keyboard status
                        if Keyboard[pygame.K_ESCAPE]:  #- if the right key is pressed
                                Examples_page()
                                Intro = False     

        pygame.quit()

def Examples_page():
        FPS = 80
        global Example
        while Example == True:

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        Example = False
                                
                        display.fill((0, 0, 0))
                        BodyText = "Press F1"
                        BodyGraphics = Font1.render(BodyText, True, [0, 255, 255])  #- create image of text (text, smoothing, color)
                        Keyboard = pygame.key.get_pressed()  #- check the keyboard status
                        if Keyboard[pygame.K_RIGHT]:  #- if the right key is pressed
                                print("a")
                        display.blit(BodyGraphics, [250, 200])
                        pygame.display.update()
                        clock.tick(FPS)
                        
                        if Keyboard[pygame.K_F1]:  #- if the right key is pressed
                                example1()
                                Example = False     

        pygame.quit()

def example1():
        space = pymunk.Space()
        space.gravity = 0, -127.79
        FPS = 80

        def convert_coordinates(point):
                return point[0], 800 - point[1]
        body = pymunk.Body()
        body.position = 400, 600

        shape = pymunk.Circle(body, 10)
        shape.density = 0.7
        shape.elasticity = 0.2
        shape.mass = 5
        space.add(body, shape)

        segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        segment_shape = pymunk.Segment(segment_body, (0, 50), (800, 50), 5)
        segment_shape.elasticity = 0.1
        space.add(segment_shape, segment_body)
        global ex1
        while ex1 == True:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        ex1 = False
                                
                        display.fill((0, 0, 0))
                        Keyboard = pygame.key.get_pressed()  #- check the keyboard status
                        if Keyboard[pygame.K_ESCAPE]:  #- if the right key is pressed
                                body.position = 400, 100
                        
                        if Keyboard[pygame.K_UP]:  # Right key applies thrust to the ball
                                thrust_force = 700  # The amount of force (adjust as needed)
                                direction = pymunk.Vec2d(0, 1)  # Apply thrust up (y-axis)
                                body.apply_force_at_world_point(direction * thrust_force, body.position)  # Apply force

                        x, y = convert_coordinates(body.position)
                        pygame.draw.circle(display, (255, 0, 0), (int(x), int(y)), 10)
                        pygame.draw.line(display, (255, 255, 0), (0, 750), (800, 750), 5)
                        pygame.display.update()
                        clock.tick(FPS)
                        space.step(1 / FPS)

        pygame.quit()

Intro_page()
