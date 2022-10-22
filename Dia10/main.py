import pygame
import random
import math
from pygame import mixer

pygame.init()  # ahora ya podemos usar los recursos de la libreria
pantalla = pygame.display.set_mode(
    (800, 600)
)  # se crea la pantalla y su tamaño alto y ancho

# Titulo de ventana- FLATICON para descargar iconocs 32 pixeles recomendados
pygame.display.set_caption("INVASION ESPACIAL")
icono = pygame.image.load(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\ovni.png"
)
# Asigna icono
pygame.display.set_icon(icono)
fondo = pygame.image.load(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\fondo.jpg"
)

# Agregar musica
mixer.music.load(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\MusicaFondo.mp3"
)
mixer.music.set_volume(1)  # volumen va de o a 1
mixer.music.play(-1)  # repetir cada vez que termina

# Jugador
ima_jugador = pygame.image.load(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\astronave.png"
)
jugador_x = 368
jugador_y = 500
jugador_cambioX = 0
jugador_cambioy = 0

# Enemigo
ima_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_cambioX = []
enemigo_cambioy = []
cantidad_enemigos = 10
for e in range(cantidad_enemigos):
    ima_enemigo.append(
        pygame.image.load(
            "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\nave-espacial.png"
        )
    )
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(0, 200))
    enemigo_cambioX.append(2)
    enemigo_cambioy.append(50)

# bala
ima_bala = pygame.image.load(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\bala.png"
)
bala_x = 0
bala_y = 500
bala_cambioX = 0
bala_cambioy = 5
bala_visible = False

# puntaje
puntaje = 0
fuente = pygame.font.Font(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\CollegiateOutlineFLF.ttf",
    30,
)  # fuente
# Descargar fuentes https://www.1001freefonts.com/
texto_x = 10
texto_y = 10

# texto final
fuente_final = pygame.font.Font(
    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\CollegiateFLF.ttf",
    40,
)


def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (68, 68, 68))
    pantalla.blit(mi_fuente_final, (200, 200))


# funcion que muestra el puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (68, 68, 68))
    pantalla.blit(texto, (x, y))


# Funcion que inicializa el movimiento
def jugador(x, y):
    pantalla.blit(ima_jugador, (x, y))


def enemigo(x, y, ene):
    pantalla.blit(ima_enemigo[ene], (x, y))


# funcion disparar bala
def bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(ima_bala, (x + 22, y + 10))


# Detectar colision
def hay_colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Este codigo muestra la pantalla y la mantiene hasta que la cerramos X =pygame.QUIT
se_ejecuta = True
while se_ejecuta == True:
    # pantalla.fill((9, 49, 118))  # RGB Color en pagina https://www.colorspire.com/rgb-color-wheel/
    # h www.freepik. para buscar fondos
    # Fondo de pantalla imagen
    pantalla.blit(fondo, (0, 0))  # imagen y ubicacion

    # Eventos iterar
    for evento in pygame.event.get():
        # Evento Cerrar
        if evento.type == pygame.QUIT:  # cierra la pantalla
            se_ejecuta = False

        # Evento de movimiento
        if evento.type == pygame.KEYDOWN:  # Presiona boton
            if evento.key == pygame.K_LEFT:
                jugador_cambioX = -0.6
            if evento.key == pygame.K_RIGHT:
                jugador_cambioX = +0.6
            if evento.key == pygame.K_SPACE:
                # sonido de disparo
                sonido_bala = mixer.Sound(
                    "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\disparo.mp3"
                )
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    bala(bala_x, bala_y)

        # detener movimiento
        if evento.type == pygame.KEYUP:  # Suelta el boton
            if evento.key == pygame.K_LEFT:
                jugador_cambioX = 0
            if evento.key == pygame.K_RIGHT:
                jugador_cambioX = 0

    # Actualizar jugador
    jugador_x += jugador_cambioX  # Asignar nuevo movimiento
    # Mantener dentro de los bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # jugador(jugador_x,jugador_y)
    # enemigo(enemigo_x[e],enemigo_y[e])

    # Actualizar enemigo
    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
                texto_final()
            break

        enemigo_x[e] += enemigo_cambioX[e]  # Asignar nuevo movimiento

        # Mantener dentro de los bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_cambioX[e] = 2
            enemigo_y[e] += enemigo_cambioy[e]
        elif enemigo_x[e] >= 736:
            enemigo_cambioX[e] = -2
            enemigo_y[e] += enemigo_cambioy[e]

        # Verificar colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision == True:
            sonido_colision = mixer.Sound(
                "C:\\Users\\julio\\OneDrive\\Documentos\\Cesar\\Cursopython\\Python\\Dia10\\Iconos\\mi_explosion_03_hpx.mp3"
            )
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(0, 200)
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        bala(bala_x, bala_y)
        bala_y -= bala_cambioy

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    # Actualiza la pantalla
    pygame.display.update()  # actualizamos diplayt
