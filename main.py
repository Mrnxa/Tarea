import pygame
import sys
import random

pygame.init()

ANCHO, ALTO = 800, 600
RADIO = 20
PADDLE_ANCHO, PADDLE_ALTO = 10, 100
FPS = 60

font = pygame.font.Font(None, 74)

Puntaje1 = 0
Puntaje2 = 0

COLOR_BOLA = (255, 0, 0)
COLOR_PADDLE = (0, 0, 255)
FONDO = (0, 0, 0)
COLOR_TEXTO = (255, 255, 255)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

ball = pygame.Surface((RADIO, RADIO))
ball.fill(COLOR_BOLA)
Bola_pos = [ANCHO // 2, ALTO // 2]
Bola_vel = [7, 7]

paddle1 = pygame.Surface((PADDLE_ANCHO, PADDLE_ALTO))
paddle1.fill(COLOR_PADDLE)
paddle1_pos = [10, ALTO // 2 - PADDLE_ALTO // 2]

paddle2 = pygame.Surface((PADDLE_ANCHO, PADDLE_ALTO))
paddle2.fill(COLOR_PADDLE)
paddle2_pos = [ANCHO - 20, ALTO // 2 - PADDLE_ALTO // 2]

clock = pygame.time.Clock()

def mostrar_menu_inicio():
    pantalla.fill(FONDO)
    Texto(pantalla, "¡Ping Pong!", font, COLOR_TEXTO, ANCHO // 2, ALTO // 2 - 100)
    Texto(pantalla, " ESPACIO para jugar", font, COLOR_TEXTO, ANCHO // 2, ALTO // 2)
    pygame.display.flip()
    esperar_tecla()

def esperar_tecla():
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    esperando = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def mostrar_menu_final(ganador):
    pantalla.fill(FONDO)
    Texto(pantalla, f"¡Jugador {ganador} ha ganado!", font, COLOR_TEXTO, ANCHO // 2, ALTO // 2 - 100)
    Texto(pantalla, "ESPACIO para jugar de nuevo", font, COLOR_TEXTO, ANCHO // 2, ALTO // 2)
    Texto(pantalla, " ESC para salir", font, COLOR_TEXTO, ANCHO // 2, ALTO // 2 + 100)
    pygame.display.flip()
    esperar_tecla()

def Texto(surface, texto, font, color, x, y):
    textobj = font.render(texto, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def FueraDeLimites(pos_x):
    if pos_x >= ANCHO:
        return 1
    elif pos_x <= 0:
        return 2
    else:
        return 0

boolSigueEnJuego = True
mostrar_menu_inicio()

Ejecutando = True
while Ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Ejecutando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_pos[1] >= 10:
        paddle1_pos[1] -= 7
    if keys[pygame.K_s] and paddle1_pos[1] <= 500:
        paddle1_pos[1] += 7
    if keys[pygame.K_UP] and paddle2_pos[1] >= 10:
        paddle2_pos[1] -= 7
    if keys[pygame.K_DOWN] and paddle2_pos[1] <= 500:
        paddle2_pos[1] += 7

    if boolSigueEnJuego:
        Bola_pos[0] += Bola_vel[0]
        Bola_pos[1] += Bola_vel[1]

    punto = FueraDeLimites(Bola_pos[0])
    if punto != 0:
        if punto == 1:
            Puntaje1 += 1
        elif punto == 2:
            Puntaje2 += 1
        Bola_pos = [ANCHO // 2, ALTO // 2]
        Bola_vel[0] *= random.choice([-1, 1])
        Bola_vel[1] *= random.choice([-1, 1])

    if Bola_pos[1] < 0 or Bola_pos[1] > ALTO - RADIO:
        Bola_vel[1] = -Bola_vel[1]

    if Bola_pos[0] + 1 < PADDLE_ANCHO and paddle1_pos[1] < Bola_pos[1] < paddle1_pos[1] + PADDLE_ALTO:
        Bola_vel[0] = -Bola_vel[0]
    elif Bola_pos[0] > ANCHO - PADDLE_ANCHO - RADIO * 2 and paddle2_pos[1] < Bola_pos[1] < paddle2_pos[1] + PADDLE_ALTO:
        Bola_vel[0]
        Bola_vel[0] = -Bola_vel[0]

    pantalla.fill(FONDO)
    pantalla.blit(ball, Bola_pos)
    pantalla.blit(paddle1, paddle1_pos)
    pantalla.blit(paddle2, paddle2_pos)
    Texto(pantalla, str(Puntaje1), font, (150, 200, 50), 200, 50)
    Texto(pantalla, str(Puntaje2), font, (150, 200, 50), 600, 50)

    if Puntaje1 == 3:
        mostrar_menu_final(1)
        Puntaje1 = 0
        Puntaje2 = 0
        boolSigueEnJuego = True
        mostrar_menu_inicio()
    elif Puntaje2 == 3:
        mostrar_menu_final(2)
        Puntaje1 = 0
        Puntaje2 = 0
        boolSigueEnJuego = True
        mostrar_menu_inicio()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()