# encoding: UTF-8
# Autor: Dora Gabriela Lizarraga Gonzalez - A01229599
# Proyecto Final

# Librerias a importar
import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
# Datos para una animación
NUM_IMAGENES = 15 #Número de cuadros
TIEMPO_ENTRE_FRAMES = .1  #tiempo entre una imagen y otra
TIEMPO_TOTAL = NUM_IMAGENES*TIEMPO_ENTRE_FRAMES

#Funciones que definen lo que aparecerá en pantalla en los diferentes estados
def dibujarMenu(ventana, botonJugar, botonPun, botonIns, botonSalir):
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(botonPun.image,botonPun.rect)
    ventana.blit(botonIns.image, botonIns.rect)
    ventana.blit(botonSalir.image, botonSalir.rect)

def dibujarInstrucciones(ventana,botonMenu):
    ventana.blit(botonMenu.image,botonMenu.rect)

def dibujarNivel1(ventana, player, meta1, listaMeteoros,listaPuntosEx):
    ventana.blit(player.image,player.rect)
    ventana.blit(meta1.image,meta1.rect)

    # Varias impresiones a partir de una lista
    for nuevoMeteoro in listaMeteoros:
        ventana.blit(nuevoMeteoro.image, nuevoMeteoro.rect)
    for nuevoExtra in listaPuntosEx:
        ventana.blit(nuevoExtra.image,nuevoExtra.rect)

def dibujarNivel2(ventana,player,meta2,listaMeteoros,listaPuntosEx):
    ventana.blit(player.image,player.rect)
    ventana.blit(meta2.image,meta2.rect)

    for nuevoMeteoro in listaMeteoros:
        ventana.blit(nuevoMeteoro.image, nuevoMeteoro.rect)
    for nuevoExtra in listaPuntosEx:
        ventana.blit(nuevoExtra.image,nuevoExtra.rect)

def dibujarNivel3(ventana,player,listaMeteoros,listaPuntosEx):
    ventana.blit(player.image,player.rect)

    for nuevoMeteoro in listaMeteoros:
        ventana.blit(nuevoMeteoro.image, nuevoMeteoro.rect)
    for nuevoExtra in listaPuntosEx:
        ventana.blit(nuevoExtra.image,nuevoExtra.rect)

# Proporciona carácter dinámico a los elementos
def actualizarMeteoros(listaMeteoros, player, contador, efecto):
    for k in range(len(listaMeteoros)-1, -1,-1):
        if listaMeteoros[k].rect.top >= ALTO:
            listaMeteoros.remove(listaMeteoros[k])


    # Comando de reacción con el usuario
    for nuevoMeteoro in listaMeteoros:
        borrarMeteoro = False
        if nuevoMeteoro.rect.colliderect(player):
            listaMeteoros.remove(nuevoMeteoro)
            borrarMeteoro = True
            contador = contarVidas(contador)
            efecto.play()
            break   # Detener el ciclo for.
        if borrarMeteoro:
            listaMeteoros.remove(nuevoMeteoro)
    return contador #Regresa un parámetro global

def actualizarExtra(listaPuntosEx, player, puntaje, efecto2):
    for k in range(len(listaPuntosEx) - 1, -1, -1):
        puntoExtra = listaPuntosEx[k]
        for nuevoExtra in listaPuntosEx:
            borrarExtra = False
            if puntoExtra.rect.colliderect(player):
                listaPuntosEx.remove(puntoExtra)
                borrarExtra = True
                puntaje = contarPuntaje(puntaje)
                efecto2.play()
                break  # Detener el ciclo for.
            if borrarExtra:
                listaPuntosEx.remove(nuevoExtra)
    return puntaje

# Actualiza número de vidas
def contarVidas(contador):
    contadorNuevo = contador - 1
    return contadorNuevo

# Actualiza la puntuación
def contarPuntaje(puntaje):
    puntaje += 25
    return puntaje

# Generar los meteoritos y los añade a una lista
def generarMeteoros(listaMeteoros, imagenMeteoros):
    for x in range(2):
            for y in range(2):
                # Coordenadas
                xMeteoro = ANCHO
                yMeteoro = randint(0, ALTO)
                nuevoMeteoro= pygame.sprite.Sprite()
                nuevoMeteoro.image = imagenMeteoros
                nuevoMeteoro.rect = imagenMeteoros.get_rect()
                nuevoMeteoro.rect.left = xMeteoro
                nuevoMeteoro.rect.top = yMeteoro
                listaMeteoros.append(nuevoMeteoro)

def generarPuntosEx(listaPuntosEx,imgExtra):
    puntoExtra = pygame.sprite.Sprite()
    puntoExtra.image = imgExtra
    puntoExtra.rect = imgExtra.get_rect()
    puntoExtra.rect.left = randint(0,ANCHO - puntoExtra.rect.width)
    puntoExtra.rect.top = randint(puntoExtra.rect.height,ALTO)
    listaPuntosEx.append(puntoExtra)

# Cambia las coordenadas de los meteoritos
def moverMeteoros(listaMeteoros,velocidadMeteoros):
    for nuevoMeteoro in listaMeteoros:
        nuevoMeteoro.rect.left -= velocidadMeteoros

# Crea un gif
def crearListaSprites():
    lista=[]

    for i in range (NUM_IMAGENES):
        nombre= "recursosJuego/metaFin/planetaFin-"+str(i)+".png"
        imagen = pygame.image.load(nombre)
        sprAnimacion=pygame.sprite.Sprite()
        sprAnimacion.image=imagen
        sprAnimacion.rect=imagen.get_rect()
        sprAnimacion.rect.left=ANCHO//2-sprAnimacion.rect.width//2 #para centrar la imagen en ancho
        sprAnimacion.rect.top = ALTO // 2 - sprAnimacion.rect.height // 2 #para centrar en alto
        lista.append(sprAnimacion)
    return lista

def obtenerFrame(timerAnimacion, listaSprites):
    indice= int(timerAnimacion/TIEMPO_ENTRE_FRAMES)
    return listaSprites[indice]

# Más funciones que determinan el aspecto gráfico de los estados
def dibujarWin(ventana, botonMenu):
    ventana.blit(botonMenu.image, botonMenu.rect)

def dibujarLose(ventana, botonMenu):
    ventana.blit(botonMenu.image, botonMenu.rect)

# Función para generar texto
def dibujartexto(ventana, puntaje):
    fuente = pygame.font.SysFont("sf pixelate", 48)
    texto = fuente.render("Puntaje:"+str(puntaje), 1, BLANCO)
    ventana.blit(texto, (0, 10))

# Función donde se contiene lo que necesita ser actualizado constantemente
def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # Caracter que le da movimiento al gif
    listaSprites = crearListaSprites()
    timerAnimacion=0


    estado = "menu"    # Pantalla principal del juego y otros objetos

    # Cargar imágenes de los botones
    imgBtnJugar = pygame.image.load("recursosJuego/botonJugar.png")
    # Sprite
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO//3- botonJugar.rect.width+botonJugar.rect.width//3
    botonJugar.rect.top = 2*(ALTO//3) - botonJugar.rect.height//2

    imgBtnPun = pygame.image.load("recursosJuego/botonPun.png")
    # Sprite
    botonPun = pygame.sprite.Sprite()
    botonPun.image = imgBtnPun
    botonPun.rect = imgBtnPun.get_rect()
    botonPun.rect.left = ANCHO // 3 + botonPun.rect.width//2+botonPun.rect.width//8
    botonPun.rect.top = 2*(ALTO//3) + (botonPun.rect.height)

    imgBtnIns = pygame.image.load("recursosJuego/botonIns.png")
    # Sprite
    botonIns = pygame.sprite.Sprite()
    botonIns.image = imgBtnIns
    botonIns.rect = imgBtnIns.get_rect()
    botonIns.rect.left = ANCHO//3- botonJugar.rect.width+botonIns.rect.width//3- botonJugar.rect.width//5
    botonIns.rect.top = 2*(ALTO//3) + (botonIns.rect.height)


    imgBtnSalir = pygame.image.load("recursosJuego/botonSalir.png")
    # Sprite
    botonSalir = pygame.sprite.Sprite()
    botonSalir.image = imgBtnSalir
    botonSalir.rect = imgBtnSalir.get_rect()
    botonSalir.rect.left = 2*ANCHO//3- botonSalir.rect.width//2+botonSalir.rect.width//8
    botonSalir.rect.top = 2*(ALTO//3) - botonJugar.rect.height//2

    imgBtnMenu = pygame.image.load("recursosJuego/botonMenu.png")
    # Sprite
    botonMenu = pygame.sprite.Sprite()
    botonMenu.image = imgBtnMenu
    botonMenu.rect = imgBtnMenu.get_rect()
    botonMenu.rect.left = ANCHO // 2 - botonMenu.rect.width // 2
    botonMenu.rect.top = 2*ALTO // 3 + botonMenu.rect.height

    imgPlayer = pygame.image.load("recursosJuego/nave.png")
    player = pygame.sprite.Sprite()
    player.image = imgPlayer
    player.rect = imgPlayer.get_rect()
    dxPlayer = 20
    dyPlayer = 20
    yPlayer = ALTO // 2
    xPlayer = 0
    player.rect.left = xPlayer
    player.rect.top = yPlayer
    moverPlayer = False


    imgMeta1 = pygame.image.load("recursosJuego/meta1.png")
    meta1 = pygame.sprite.Sprite()
    yMeta1 = ALTO // 2
    xMeta1 = ANCHO // 2
    meta1.image = imgMeta1
    meta1.rect = imgMeta1.get_rect()
    meta1.rect.left = xMeta1
    meta1.rect.top = yMeta1

    imgMeta2 = pygame.image.load("recursosJuego/meta2.png")
    meta2 = pygame.sprite.Sprite()
    meta2.image = imgMeta2
    meta2.rect = imgMeta2.get_rect()
    yMeta2 = randint(2*meta2.rect.height, ALTO)
    xMeta2 = randint(ANCHO // 2, ANCHO - meta2.rect.width)
    meta2.rect.left = xMeta2
    meta2.rect.top = yMeta2



    imagenMeteoro = pygame.image.load("recursosJuego/meteoro.png")
    listaMeteoros = []

    timerMeteoros = 0
    timerExtra= 0
    generarMeteoros(listaMeteoros,imagenMeteoro)

    listaPuntosEx = []
    for i in range(4):
        imgExtra = pygame.image.load("recursosJuego/puntosExtra/extra-"+str(randint(0,3))+".png")
    generarPuntosEx(listaPuntosEx,imgExtra)



    contadorVidas = 3
    puntaje = 0

    # MUSICA de fondo
    pygame.mixer.init()
    pygame.mixer.music.load("recursosJuego/temaMenu.mp3")
    pygame.mixer.music.play(-1)

    efecto = pygame.mixer.Sound("recursosJuego/shoot.wav")
    efecto2= pygame.mixer.Sound("recursosJuego/ex.wav")

    # Imagenes de fondo
    imagenFondo = pygame.image.load("recursosJuego/fondoMenu.png")
    x = 0
    imagenFondoIns = pygame.image.load("recursosJuego/fondoIns.png")
    imagenN1 = pygame.image.load("recursosJuego/fondo1.gif")
    imagenN2 = pygame.image.load("recursosJuego/fondo2.gif")
    imagenN3 = pygame.image.load("recursosJuego/fondo3.png")
    imagenWin = pygame.image.load("recursosJuego/fondoGanar.png")
    imagenLose = pygame.image.load("recursosJuego/fondoLose.png")


    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN: # El usuario hizo click
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xbJ, ybJ, anchoBJ, altoBJ = botonJugar.rect
                    xbP, ybP, anchoBP, altoBP = botonPun.rect
                    xbI, ybI, anchoBI, altoBI = botonIns.rect
                    xbS, ybS, anchoBS, altoBS = botonSalir.rect
                    if xm>=xbJ and xm<=xbJ+anchoBJ:
                        if ym>=ybJ and ym<=ybJ+altoBJ:
                            # Cambiar de ventana
                            estado = "jugando"
                            yPlayer = ALTO // 2
                            xPlayer = 0
                            player.rect.left = xPlayer
                            player.rect.top = yPlayer
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("recursosJuego/musicaJuego.mp3")
                            pygame.mixer.music.play(-1)
                    if xm>=xbP and xm<=xbP+anchoBP:
                        if ym>=ybP and ym<=ybP+altoBP:
                            # Cambiar de ventana
                            estado = "puntuacion"
                    if xm>=xbI and xm<=xbI+anchoBI:
                        if ym>=ybI and ym<=ybI+altoBI:
                            # Cambiar de ventana
                            estado = "instrucciones"
                    if xm>=xbS and xm<=xbS+anchoBS:
                        if ym>=ybS and ym<=ybS+altoBS:
                            termina = True
                elif estado == "instrucciones"or estado=="puntuacion":
                    xbMn, ybMn, anchoBMn, altoBMn = botonMenu.rect
                    if xm >= xbMn and xm <= xbMn + anchoBMn:
                        if ym >= ybMn and ym <= ybMn + altoBMn:
                            estado = "menu"
                            contadorVidas = 3
                            puntaje = 0

                if estado == "win" or estado == "lose":
                    xbMn, ybMn, anchoBMn, altoBMn = botonMenu.rect
                    if xm >= xbMn and xm <= xbMn + anchoBMn:
                        if ym >= ybMn and ym <= ybMn + altoBMn:
                            estado = "menu"
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("recursosJuego/temaMenu.mp3")
                            pygame.mixer.music.play(-1)

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:  # Flecha hacia arriba
                    dyPlayer = -10
                    dxPlayer = 0
                    moverPlayer = True
                if evento.key == pygame.K_DOWN:  # Flecha hacia abajo
                    dyPlayer = 10
                    dxPlayer = 0
                    moverPlayer = True
                if evento.key == pygame.K_RIGHT:  # Flecha hacia la derecha
                    dxPlayer = 10
                    dyPlayer = 0
                    moverPlayer = True
                if evento.key == pygame.K_LEFT:  # Flecha hacia la derecha
                    dxPlayer = -10
                    dyPlayer = 0
                    moverPlayer = True
            if evento.type == pygame.KEYUP:
                moverPlayer = False

        # Borrar pantalla
        if estado == "menu":
            ventana.blit(imagenFondo, (x, 0))
            ventana.blit(imagenFondo, (ANCHO + x, 0))
        elif estado == "instrucciones":
            ventana.blit(imagenFondoIns,(0,0))
        elif estado == "jugando":
            ventana.blit(imagenN1,(0,0))
        elif estado == "nivel2":
            ventana.blit(imagenN2,(0,0))
        elif estado == "nivel3":
            ventana.blit(imagenN3,(0,0))
            frameActual = obtenerFrame(timerAnimacion, listaSprites)
            ventana.blit(frameActual.image, frameActual.rect)
        elif estado == "win":
            ventana.blit(imagenWin,(0,0))
        elif estado == "lose":
            ventana.blit(imagenLose,(0,0))

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            contadorVidas = 3
            puntaje = 0



            dibujarMenu(ventana, botonJugar, botonPun,botonIns, botonSalir)
            archivo = open('Puntaje.txt', 'w')
            archivo.close()

        elif estado == "instrucciones":
            dibujarInstrucciones(ventana,botonMenu)
        elif estado == "puntacion":
            dibujarInstrucciones(ventana, botonMenu)
        elif estado == "jugando":

            dibujartexto(ventana,puntaje)
            puntaje = actualizarExtra(listaPuntosEx, player, puntaje,efecto2)
            contadorVidas = actualizarMeteoros(listaMeteoros,player,contadorVidas,efecto)
            dibujarNivel1(ventana,player,meta1,listaMeteoros,listaPuntosEx)
            if contadorVidas == 0:
                estado = "lose"
            if moverPlayer:
                player.rect.left += dxPlayer
                player.rect.top += dyPlayer

            velocidadMeteoros = 7
            moverMeteoros(listaMeteoros,velocidadMeteoros)
            if player.rect.colliderect(meta1):
                puntaje += 50
                estado = "nivel2"
                yMeta2 = randint(2*meta2.rect.height, ALTO)
                xMeta2 = randint(ANCHO // 2, ANCHO - meta2.rect.height)
                meta2.rect.left = xMeta2
                meta2.rect.top = yMeta2
                yPlayer = ALTO - player.rect.height
                xPlayer = 0
                player.rect.x = xPlayer
                player.rect.y = yPlayer

        elif estado == "nivel2":
            dibujartexto(ventana, puntaje)
            puntaje = actualizarExtra(listaPuntosEx, player, puntaje,efecto2)
            contadorVidas = actualizarMeteoros(listaMeteoros, player, contadorVidas, efecto)
            if contadorVidas == 0:
                estado = "lose"
            dibujarNivel2(ventana,player,meta2,listaMeteoros,listaPuntosEx)
            velocidadMeteoros = 9

            moverMeteoros(listaMeteoros,velocidadMeteoros)
            if moverPlayer:
                player.rect.left += dxPlayer
                player.rect.top += dyPlayer

                if player.rect.colliderect(meta2):
                    puntaje += 50
                    estado = "nivel3"
                    xPlayer= randint(0,ANCHO-player.rect.width)
                    if xPlayer <= ANCHO//2:
                        yPlayer =  player.rect.height
                    elif xPlayer > ANCHO//2:
                        yPlayer = ALTO - player.rect.height
                    player.rect.x = xPlayer
                    player.rect.y = yPlayer
        elif estado == "nivel3":
            dibujartexto(ventana, puntaje)
            puntaje = actualizarExtra(listaPuntosEx, player, puntaje,efecto2)
            contadorVidas = actualizarMeteoros(listaMeteoros, player, contadorVidas, efecto)
            if contadorVidas == 0:
                estado = "lose"
            velocidadMeteoros = 15

            moverMeteoros(listaMeteoros,velocidadMeteoros)
            dibujarNivel3(ventana,player,listaMeteoros,listaPuntosEx)
            if moverPlayer:
                player.rect.left += dxPlayer
                player.rect.top += dyPlayer
                for sprite in listaSprites:
                    if player.rect.colliderect(sprite):
                        puntaje += 50
                        estado = "win"
        elif estado == "win":
            fuente = pygame.font.SysFont("sf pixelate", 48)
            texto = fuente.render("Puntaje:" + str(puntaje), 1, BLANCO)
            ventana.blit(texto, (ANCHO//2, (ALTO//2)-100))
            archivo = open('Puntaje.txt', 'a')
            archivo.write(str(puntaje)+ "\n")
            archivo.close()

            dibujarWin(ventana, botonMenu)
        elif estado == "lose":
            dibujarLose(ventana,botonMenu)




        pygame.display.flip()   # Actualiza trazos
        timerAnimacion+= reloj.tick(40)/1000   #regresa tiempo real dividido entre mil y se suma al timer de animacion
        if timerAnimacion>= TIEMPO_TOTAL:
            timerAnimacion=0       # 40 fps


        timerMeteoros += reloj.tick(40) / 1000  # Frecuencia con la que se generan los meteoros
        timerExtra += 1/40 # Frecuencia con la que se generan los extras
        if timerExtra >= 2:
            timerExtra = 0
            generarPuntosEx(listaPuntosEx, imgExtra)
        if timerMeteoros >= .5:
            timerMeteoros = 0
            generarMeteoros(listaMeteoros, imagenMeteoro)



    pygame.quit()   # termina pygame


def main():
    dibujar()


main()