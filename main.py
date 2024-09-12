import pygame
from math import cos, sin
from numpy import dot
pygame.init()
HEIGHT = 720
WIDTH = 1280
TAM = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
triangles = [
    [[-1,1,-1],[-1,-1,-1],[1,-1,-1]],
    [[-1,1,-1],[1,-1,-1],[1,1,-1]],
    #[],
    #[],
    #[],
    #[],
    #[],
    #[],
    #[],
    #[],
    #[],
    #[],
]
run = True
while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0,0,0))

    traslation = [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,6],
        [0,0,0,1]
    ]
    rotationY = [
        [cos(0.01),0,sin(0.01)],
        [0,1,0],
        [-sin(0.01),0,cos(0.01)]
    ]
    print('Originales')
    print(triangles)
    #Rotacion de los triangulos
    rotatedTriangles = []
    for triangle in triangles:
        rotVertice = []
        for vertice in triangle:
            tmp = []
            for axis in vertice:
                tmp.append(axis)
            rotVertice.append(dot(rotationY,tmp))
        rotatedTriangles.append(rotVertice)
    triangles = rotatedTriangles
    print('Rotados')
    print(triangles)
    
    #Traslacion de triangulos
    transformedTriangles = []
    for triangle in triangles:
        trasVertice = []
        for vertice in triangle:
            tmp = []
            for axis in vertice:
                tmp.append(axis)
            tmp.append(1)
            trasVertice.append(dot(traslation,tmp))
        transformedTriangles.append(trasVertice)

    print('Trasladados:')
    print(transformedTriangles)

    #Proyección de triangulos
    projectedTriangles = []
    for triangle in transformedTriangles:
        projectedVertice = []
        for vertice in triangle:
            x = (vertice[0]*TAM / vertice[2])+(WIDTH/2)
            y = (vertice[1]*TAM / vertice[2])+(HEIGHT/2)
            projectedVertice.append((x,y))
        projectedTriangles.append(projectedVertice)

    print('Proyectados')
    print(projectedTriangles)

    #Dibujo de triangulos
    for triangle in projectedTriangles:
        pygame.draw.polygon(screen,(255,255,0),(
            triangle[0],
            triangle[1],
            triangle[2]
            ))
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()