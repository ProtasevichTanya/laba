import pygame
from pygame.draw import *

pygame.init()

#функция рисования кота
def cat(x1, y1, x2, y2, colorc, colory):
    '''
    Функция рисует кота на экране
    Ориентация кота зависит от того, как расположена точка (x2, y2) относительно (x1,y1).
    Если справа - кот как бы смотрит влево. Если слева - кот смотрит вправо.
    x1 и y1 - координаты верхнего левого угла, если кот смотрит влево, правого - если вправо
    x2 и y2 - координаты правого нижнего угла (если смотрит влево), левого - если вправо
    colorc - цвет кота
    colory - цвет глаз

    ВАЖНО!!!
    координата y2 обязательно должна быть больше y1
    '''
    a = y2 - y1
    b = x2 - x1
    if b >= 0:
        # нога за головой
        ellipse(sc, colorc,
            (x1 + b / 20, y1 + a / 2, b / 8, a / 2))  
        ellipse(sc, WHITE,
            (x1 + b / 20, y1 + a / 2, b / 8, a / 2), 2)
        # хвост
        ellipse(sc, colorc,
            (x1 + b * 7 / 8, y1 + a / 2, b / 3, a / 3))  
        ellipse(sc, WHITE,
            (x1 + b * 7 / 8, y1 + a / 2, b / 3, a / 3), 2)
        # тело
        ellipse(sc, colorc,
            (x1 + b / 8, y1 + 1 / 5 * a, 5 * b / 6, a * 4 / 5))  
        ellipse(sc, WHITE,
            (x1 + b / 8, y1 + 1 / 5 * a, 5 * b / 6, a * 4 / 5), 2)
        # голова 
        circle(sc, colorc,
           (x1 + b / 6, y1 + a / 2), a / 3) 
        circle(sc, WHITE,
           (x1 + b / 6, y1 + a / 2), a / 3, 2)
        # передняя нога вторая
        ellipse(sc, colorc,
            (x1 + b / 6, y1 + a * 6 / 7, b / 5, a / 5))  
        ellipse(sc, WHITE,
            (x1 + b / 6, y1 + a * 6 / 7, b / 5, a / 5), 2)
        # круг задней ноги
        circle(sc, colorc,
           (x1 + 5 * b / 6, y1 + 4 / 5 * a), a / 4)  
        circle(sc, WHITE,
           (x1 + 5 * b / 6, y1 + 4 / 5 * a), a / 4, 2)
        # стопа задней ноги
        ellipse(sc, colorc,
            (x1 + b * 7 / 8, y1 + a * 7 / 8, b / 8, a / 3))
        ellipse(sc, WHITE,
            (x1 + b * 7 / 8, y1 + a * 7 / 8, b / 8, a / 3), 2)  
        # глаза
        for i in (-1, 1):
            circle(sc, colory,
               (x1 + b / 6 + i * b / 15, y1 + a / 2 - a / 10), a / 14)  
            circle(sc, BLACK,
               (x1 + b / 6 + i * b / 15, y1 + a / 2 - a / 10), a / 14, 1)
            ellipse(sc, BLACK,
                (x1 + b / 6 + i * b / 15 + b / 100, y1 + a / 2 - a / 10 - a / 20, b / 100, a / 10))
    else:
        # нога за головой
        ellipse(sc, colorc,
            (x1 + b / 20, y1 + a / 2, b / 8, a / 2))  
        ellipse(sc, WHITE,
            (x1 + b / 20 + b / 8, y1 + a / 2, - b / 8 + 1, a / 2), 2)
        # хвост
        ellipse(sc, colorc,
            (x1 + b * 7 / 8, y1 + a / 2, b / 3, a / 3)) 
        ellipse(sc, WHITE,
            (x1 + b * 7 / 8 + b / 3, y1 + a / 2, - b / 3 + 1, a / 3), 2)
        # тело
        ellipse(sc, colorc,
            (x1 + b / 8, y1 + 1 / 5 * a, 5 * b / 6, a * 4 / 5))  
        ellipse(sc, WHITE,
            (x1 + b / 8 + 5 * b / 6, y1 + 1 / 5 * a, - 5 * b / 6, a * 4 / 5), 2)
        # голова
        circle(sc, colorc,
           (x1 + b / 6, y1 + a / 2), a / 3)  
        circle(sc, WHITE,
           (x1 + b / 6, y1 + a / 2), a / 3, 2)
        # передняя нога вторая
        ellipse(sc, colorc,
            (x1 + b / 6, y1 + a * 6 / 7, b / 5, a / 5))  
        ellipse(sc, WHITE,
            (x1 + b / 6 + b / 5, y1 + a * 6 / 7, - b / 5 + 1, a / 5), 2)
        # круг задней ноги
        circle(sc, colorc,
           (x1 + 5 * b / 6, y1 + 4 / 5 * a), a / 4)  
        circle(sc, WHITE,
           (x1 + 5 * b / 6, y1 + 4 / 5 * a), a / 4, 2)
        # стопа задней ноги
        ellipse(sc, colorc,
            (x1 + b * 7 / 8, y1 + a * 7 / 8, b / 8, a / 3)) 
        ellipse(sc, WHITE,
            (x1 + b * 7 / 8 + b / 8, y1 + a * 7 / 8, - b / 8 + 1, a / 3), 2)
        # глаза
        for i in (-1, 1):
            circle(sc, colory,
               (x1 + b / 6 + i * b / 15, y1 + a / 2 - a / 10), a / 14)  
            circle(sc, BLACK,
               (x1 + b / 6 + i * b / 15, y1 + a / 2 - a / 10), a / 14, 1)
            ellipse(sc, BLACK,
                (x1 + b / 6 + i * b / 15 + b / 100, y1 + a / 2 - a / 10 - a / 20, b / 100, a / 10))
            
    # рисуем уши 
    polygon(sc, WHITE,
                        [(x1 + (0.316 * b) * 2 / 3, y1 + 0.19 * a), (x1 + (0.44 * b) * 2 / 3, y1 + 0.314 * a),
                         (x1 + (0.45 * b) * 2 / 3, y1 + 0.1 * a)], 4)  
    polygon(sc, colorc,
                        [(x1 + (0.316 * b) * 2 / 3, y1 + 0.19 * a), (x1 + (0.44 * b) * 2 / 3, y1 + 0.314 * a),
                         (x1 + (0.45 * b) * 2 / 3, y1 + 0.1 * a)])
    polygon(sc, WHITE,
                        [(x1 + b / 10, y1 + 0.19 * a), (x1 - (0.12 * b) * 2 / 3 + b / 10, y1 + 0.314 * a),
                         (x1 - (0.17 * b) * 2 / 3 + b / 10, y1 + 0.1 * a)], 5)
    polygon(sc, colorc,
                        [(x1 + b / 10, y1 + 0.19 * a), (x1 - (0.12 * b) * 2 / 3 + b / 10, y1 + 0.314 * a),
                         (x1 - (0.17 * b) * 2 / 3 + b / 10, y1 + 0.1 * a)])
    # рисуем нос
    polygon(sc, WHITE,
                        [(x1 + b / 6 + b / 50, y1 + a / 2 - a / 50), (x1 + b / 6 - b / 50, y1 + a / 2 - a / 50),
                         (x1 + b / 6, y1 + a / 2)], 2)
    # рисуем усы
    for i in range(5):
        line(sc, WHITE, [x1 + b / 6 + b / 30, y1 + a / 2 + a / 20 + a / 50 * i],
                        [x1 + b / 6 + b / 4, y1 + a / 2 - a / 30 + a / 20 + a / 35 * i], 1)  
        line(sc, WHITE, (x1 + b / 6 - b / 30, y1 + a / 2 + a / 20 + a / 50 * i),
                        [x1 + b / 6 - b / 4, y1 + a / 2 - a / 30 + a / 20 + a / 35 * i], 1)
        ellipse(sc, WHITE,
                (x1 + b / 6, y1 + a / 2, 2, a / 8), 2)

# функция рисования клубка
def klu(x1, y1, colk, r, napr):
    '''
    Функция рисует клубок с нитками.
    x1, y1 - координаты центра клубка
    colk - цвет клубка
    r - радиус клубка
    napr - ориентация клубка: 1 - нитка вправо; -1 - нитка влево
    '''
    circle(sc, colk, (x1, y1), r)
    circle(sc, WHITE, (x1, y1), r, 2)
    for i in range(3):
        line(sc, WHITE, (x1, y1 - 4 / 5 * r + i * r / 4), (x1 + napr * (r / 4 + i * r / 4), y1 - r / 2 + i * r / 4))
        line(sc, WHITE, (x1 - (r / 2) * napr, y1 + r / 2 - r / 4 * i), (x1 + (r / 3) * napr, y1 + r * 2 / 3 - r / 5 * i))
    lines(sc, WHITE, False, [[x1 + 1.41 / 2 * r * napr, y1 + 1.41 / 2 * r], [x1 + r * napr, y1 + r],
                                         [x1 + (1.41 / 2 + 1) * r * napr, y1 + 1.41 / 2 * r],
                                         [x1 + 2 * r * napr, y1 + r]])

# функция рисования окна
def wn(x1, y1, a, b):
    '''
    Данная функция рисует окно.
    x1, y1 - координаты левого верхнего угла окна
    a, b - длина (изменение x) и ширина (изменение y) окна соответственно
    '''
    polygon(sc, LIGHT_BLUE, [(x1, y1), (x1, y1 + b), (x1 + a, y1 + b), (x1 + a, y1)])
    polygon(sc, BLUE, [(x1 + 1 / 13 * a, y1 + 1 / 13 * b), (x1 + 1 / 13 * a, y1 + 1 / 13 * b + 3 / 13 * b),
                                   (x1 + 1 / 13 * a + a * 5 / 13, y1 + 1 / 13 * b + 3 / 13 * b),
                                   (x1 + 1 / 13 * a + a * 5 / 13, y1 + 1 / 13 * b)])
    polygon(sc, BLUE, [(x1 + 7 / 13 * a, y1 + 1 / 13 * b), (x1 + 7 / 13 * a, y1 + 1 / 13 * b + 3 / 13 * b),
                                   (x1 + 7 / 13 * a + a * 5 / 13, y1 + 1 / 13 * b + 3 / 13 * b),
                                   (x1 + 7 / 13 * a + a * 5 / 13, y1 + 1 / 13 * b)])
    polygon(sc, BLUE, [(x1 + 1 / 13 * a, y1 + 5 / 13 * b), (x1 + 1 / 13 * a, y1 + 5 / 13 * b + 7 / 13 * b),
                                   (x1 + 1 / 13 * a + a * 5 / 13, y1 + 5 / 13 * b + 7 / 13 * b),
                                   (x1 + 1 / 13 * a + a * 5 / 13, y1 + 5 / 13 * b)])
    polygon(sc, BLUE, [(x1 + 7 / 13 * a, y1 + 5 / 13 * b), (x1 + 7 / 13 * a, y1 + 5 / 13 * b + 7 / 13 * b),
                                   (x1 + 7 / 13 * a + a * 5 / 13, y1 + 5 / 13 * b + 7 / 13 * b),
                                   (x1 + 7 / 13 * a + a * 5 / 13, y1 + 5 / 13 * b)])

# задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (204, 229, 252)
BLUE = (50, 148, 240)
GREEN = (72, 150, 64)
YELLOW = (225, 225, 0)
PINK = (242, 107, 138)
RED = (255, 0, 0)
STENA = (255, 193, 163)
POL = (219, 155, 112)
ORANGE = (254,102,13)

# начинаем рисовать

FPS = 30
sc = pygame.display.set_mode((700, 700)) # размеры окна

#рисуем стену и пол
polygon(sc, STENA, [(0, 0), (0, 300), (700, 300), (700, 0)])
polygon(sc, POL, [(0, 300), (0, 700), (700, 700), (700, 300)])

# задаем положение, размер и цвет котов
cat(300, 300, 500, 400, GRAY, BLUE)
cat(500, 300, 600, 350, ORANGE, GREEN)
cat(100, 500, 300, 600, GRAY, BLUE)
cat(250, 250, 50, 350, ORANGE, GREEN)
cat(500, 500, 400, 550, ORANGE, GREEN)

# рисуем клубки
klu(400, 400, PINK, 30, -1)
klu(650, 400, GRAY, 20, 1)
klu(200, 450, GRAY, 30, -1)
klu(100, 650, PINK, 30, 1)
klu(600, 600, PINK, 60, -1)

# рисуем окна
wn(100, 50, -200, 200)
wn(400, 50, -200, 200)
wn(650, 50, -200, 200)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
