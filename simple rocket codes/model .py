# first installl opengl useing pip install pygame PyOpenGL

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Rotating Rocket")

# Initialize OpenGL
glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (800 / 600), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -5)

# Initialize rotation variables
rotation_speed = 1
rotation_angle = 0

def draw_earth():
    glPushMatrix()
    glColor3f(0.0, 0.5, 1.0)  # Blue Earth
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

def draw_rocket(rotation_angle):
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)  # Red Rocket
    glRotatef(rotation_angle, 0, 0, 1)
    glTranslatef(2, 0, 0)
    glutSolidCone(0.2, 1, 20, 20)
    glPopMatrix()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_earth()
    draw_rocket(rotation_angle)

    pygame.display.flip()
    pygame.time.wait(10)

    rotation_angle += rotation_speed
    if rotation_angle >= 360:
        rotation_angle = 0

pygame.quit()
