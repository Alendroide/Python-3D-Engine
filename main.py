import pygame
import numpy
import math
pygame.init()
WIDTH = 1280
HEIGTH = 720
midX = WIDTH // 2
midY = HEIGTH // 2
FOV = 1280

screen = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("3D Engine")

clock = pygame.time.Clock()
run = True

#Figuras
vertices = [[-1, -1, 1], [-1, -1, 3], [1, -1, 1], [1, -1, 3], [-1, 1, 1], [-1, 1, 3], [1, 1, 1], [1, 1, 3]]
lineas = [[0,1],[0,2],[0,4],[3,1],[3,2],[3,7],[5,1],[5,4],[5,7],[6,2],[6,4],[6,7]]
triangulos = [[0,4,6,'red'],[0,2,6,'red'],[1,5,7,'blue'],[1,3,7,'blue'],[0,1,2,'green'],[1,2,3,'green'],[4,5,6,'yellow'],[5,6,7,'yellow'],[0,4,5,'white'],[0,1,5,'white'],[2,3,6,'orange'],[3,6,7,'orange']]
list_pf = []
list_org_pf = []

#Funciones
def multiplicar(vert,tabl):
    for i in vert:
        if tabl == tras:
            coor = [
                [i[0]],
                [i[1]],
                [i[2]],
                [1]
            ]
        else:
            coor = [
                [i[0]],
                [i[1]],
                [i[2]]
            ]
        mult = numpy.dot(tabl,coor)
        vert[vert.index(i)][0] = mult[0][0]
        vert[vert.index(i)][1] = mult[1][0]
        vert[vert.index(i)][2] = mult[2][0]

#Valores traslación
tX = 0
tY = 0
tZ = 0

#Valores rotación
rX = 0
rY = 0
rZ = 0

while run:
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Fondo
    screen.fill((0,0,0))
    #Definición de controles
    keys = pygame.key.get_pressed()
    arriba = keys[pygame.K_LSHIFT]
    abajo = keys[pygame.K_LCTRL]
    adelante = keys[pygame.K_w]
    atras = keys[pygame.K_s]
    derecha = keys[pygame.K_d]
    izquierda = keys[pygame.K_a]
    up = keys[pygame.K_UP]
    down = keys[pygame.K_DOWN]
    left = keys[pygame.K_LEFT]
    right = keys[pygame.K_RIGHT]

    #Controles
        #Movimiento
    if adelante: tZ = -0.1
    elif atras: tZ = 0.1
    else: tZ = 0
    if derecha: tX = -0.1
    elif izquierda: tX = 0.1
    else: tX = 0
    if arriba: tY = 0.1
    elif abajo: tY = -0.1
    else: tY = 0
        #Rotación
    if up: rX = -0.03
    elif down: rX = 0.03
    else: rX = 0
    if left: rY = 0.03
    elif right: rY = -0.03
    else: rY = 0
    #Matrices
        #Traslación
    tras = [
        [1,0,0,tX],
        [0,1,0,tY],
        [0,0,1,tZ],
        [0,0,0,1],
    ]
        #Rotación
    maX = [
        [1,0,0],
        [0,math.cos(rX),-math.sin(rX)],
        [0,math.sin(rX),math.cos(rX)]
    ]
    maY = [
        [math.cos(rY),0,math.sin(rY)],
        [0,1,0],
        [-math.sin(rY),0,math.cos(rY)]
    ]
    maZ = [
        [math.cos(rZ),-math.sin(rZ),0],
        [math.sin(rZ),math.cos(rZ),0],
        [0,0,1]
    ]
    #Multiplicaciones
    multiplicar(vertices,tras)
    multiplicar(vertices,maX)
    multiplicar(vertices,maY)
    multiplicar(vertices,maZ)

    #Creación de triángulos
    tmp_triangles = ["" for i in triangulos]
    cnt = 0
    for i in triangulos:
        cnt += 0.000000000001
        pf = ((vertices[i[0]][2]+vertices[i[1]][2]+vertices[i[2]][2])/3) + cnt
        list_pf.append(pf)
        list_org_pf.append(pf)
    list_org_pf.sort(reverse=True)

    for i in list_pf:
        indexO = list_org_pf.index(i)
        indexU = list_pf.index(i)
        tmp_triangles[indexO] = triangulos[indexU]

    #Dibujado

    for i in tmp_triangles:
        indexver1 = i[0]
        indexver2 = i[1]
        indexver3 = i[2]
        ver1 = ((((vertices[indexver1][0]*FOV))/vertices[indexver1][2])+midX,(((vertices[indexver1][1]*FOV))/vertices[indexver1][2])+midY)
        ver2 = ((((vertices[indexver2][0]*FOV))/vertices[indexver2][2])+midX,(((vertices[indexver2][1]*FOV))/vertices[indexver2][2])+midY)
        ver3 = ((((vertices[indexver3][0]*FOV))/vertices[indexver3][2])+midX,(((vertices[indexver3][1]*FOV))/vertices[indexver3][2])+midY)
        if vertices[indexver1][2] > 0 and vertices[indexver2][2] > 0 and vertices[indexver3][2] > 0:
            pygame.draw.polygon(screen,i[3],(ver1,ver2,ver3))

    list_pf.clear()
    list_org_pf.clear()
    #Actualizado
    pygame.display.update()
    clock.tick(60)
pygame.quit()