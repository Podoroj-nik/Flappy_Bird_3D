#  импорт всего, что только можно
import os
import pytest
import random
import sys
import pygame
import webbrowser

# скорость игры (выше 100 не ставить!)
FPS = 60

global state
global tubing

# инициализация переменных
pygame.init()
pygame.mixer.music.load('Data/Music/background_music.mp3')
sound1 = pygame.mixer.Sound('Data/Bird_dead.mp3')
sound1.set_volume(0.3)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
pygame.mixer.music.stop()

# размер окна
infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((width, height))
screen_rect = (0, 0, width, height)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

#  куча оочень выжных переменных <з
detect = 20
player_y, speed_player, acceleration = height // 2, 0, 0
player = pygame.Rect(width // 4, player_y, 136, 45)

state = "start"
tubing = []
birds = []
pipes = []
watermelons = []
kadr = 0
flag = False
sch = 0
pos = 0
vol = 1
maxim_score = 0
f_sp = []
wat_t = 0

#  узнаём адрес шрифта segoescript

f_ad = pygame.font.match_font('segoescript')


# обработка загрузки изображений


def load_image(name, colorkey=None):
    fullname = os.path.join('Data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

#  Генерация и построение уровня

def generation_level_step1():
    global level
    level = ''
    for i in range(100):
        level += str(random.randint(1, 5))
    f = open('Data/requirements.txt', 'w', encoding="utf8")
    print(level, end='', file=f)


#  второй этап генерации уровня

def generation_level_step2():
    f = open('Data/requirements.txt', 'r')
    level = f.readlines()[0]
    Pipes = {'1': image_pipe11, '2': image_pipe21, '3': image_pipe31,
             '4': image_pipe41, '5': image_pipe51}
    Pipes2 = {'1': image_pipe12, '2': image_pipe22, '3': image_pipe32,
             '4': image_pipe42, '5': image_pipe52}
    for el in range(len(level)):
        sim = level[el]
        pipe = Pipes[sim], Pipes2[sim]
        pipes.append(pipe)


def f_spis():
    f = open('Data/requirements.txt', 'r')
    return list(f.readlines()[0])


#  обновление труб

def level_update():
    for i in range(100):
        tubing.append(2000 + 600 * i)
        screen.blit((pipes[i])[1], (tubing[i], -110))


#  вывод труб на экран
def print_level():
    pip = {'1': 1300 - 817 - 50, '2': 1300 - 662 - 50, '3': 1300 - 525 - 50,
           '4': 1300 - 388 - 50, '5': 1300 - 252 - 50}
    if state == "play":
        for i in range(100):
            tubing[i] = tubing[i] - 4
            screen.blit((pipes[i])[0], (tubing[i], -110))
            s = pip[(level[i])]
            screen.blit((pipes[i])[1], (tubing[i], s))
        for i in range(len(watermelons)):
            watermelons[i] = watermelons[i] - 4
            screen.blit(image_watermelon, (watermelons[i], 490))


#  генерация и спавн арбузов
def watermelon():
    k = random.randint(0, 5)
    for i in range(k):
        kor = random.randint(0, 99)
        watermelons.append(1750 + 600 * kor)




# загрузка и редактирование изображений
image_background = load_image("F_sky.png")
image_background = pygame.transform.scale(image_background, (1920, 1080))

image_bird1 = load_image("Bird/F-Bird_1.png")
image_bird1 = pygame.transform.scale(image_bird1, (200, 200))
birds.append(image_bird1)
image_bird2 = load_image("Bird/F-Bird_2.png")
image_bird2 = pygame.transform.scale(image_bird2, (200, 200))
birds.append(image_bird2)
image_bird3 = load_image("Bird/F-Bird_3.png")
image_bird3 = pygame.transform.scale(image_bird3, (200, 200))
birds.append(image_bird3)
image_bird4 = load_image("Bird/F-Bird_4.png")
image_bird4 = pygame.transform.scale(image_bird4, (200, 200))
birds.append(image_bird4)


image_pipe11 = load_image("Pipes/Pipe_11.png")
mask_pipe11 = pygame.mask.from_surface(image_pipe11)

image_pipe21 = load_image("Pipes/Pipe_21.png")
mask_pipe21 = pygame.mask.from_surface(image_pipe21)

image_pipe31 = load_image("Pipes/Pipe_31.png")
mask_pipe31 = pygame.mask.from_surface(image_pipe31)

image_pipe41 = load_image("Pipes/Pipe_41.png")
mask_pipe41 = pygame.mask.from_surface(image_pipe41)

image_pipe51 = load_image("Pipes/Pipe_51.png")
mask_pipe51 = pygame.mask.from_surface(image_pipe51)


image_pipe12 = load_image("Pipes/Pipe_12.png")
mask_pipe12 = pygame.mask.from_surface(image_pipe12)

image_pipe22 = load_image("Pipes/Pipe_22.png")
mask_pipe22 = pygame.mask.from_surface(image_pipe22)

image_pipe32 = load_image("Pipes/Pipe_32.png")
mask_pipe32 = pygame.mask.from_surface(image_pipe32)

image_pipe42 = load_image("Pipes/Pipe_42.png")
mask_pipe42 = pygame.mask.from_surface(image_pipe42)

image_pipe52 = load_image("Pipes/Pipe_52.png")
mask_pipe52 = pygame.mask.from_surface(image_pipe52)


vol_zn = load_image("Play.png")
vol_zn = pygame.transform.scale(vol_zn, (150, 150))

mute = load_image("Mute.png")
mute = pygame.transform.scale(mute, (150, 150))

image_watermelon = load_image("Fruit.png")
image_watermelon = pygame.transform.scale(image_watermelon, (100, 100))

#  Стартовое окно игры(также финальное), состоящее из:
#  названия:

class Fb_title(pygame.sprite.Sprite):
    image = load_image("Title.png")

    def __init__(self, group):
        super().__init__(group)
        title = pygame.transform.scale(Fb_title.image, (1000 * 1.2, 280 * 1.2))
        self.image = title
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(750, 200)
        self.sh = 0
        self.dwig = False
        self.rew = False
        self.c = 0

    def update(self):
        if state == "play":
            self.dwig = True
        elif state == "fall":
            self.sh = 0
            self.rew = True
        if self.rew == True:
            if self.c < 2700:
                self.rect = self.rect.move(-60, 0)
                self.c += 60
            else:
                self.rew = False
                self.c = 0
        if self.dwig:
            if self.sh < 2700:
                self.rect = self.rect.move(60, 0)
                self.sh += 60
            else:
                self.dwig = False


#  и подсказки:

class Fb_title_2(pygame.sprite.Sprite):
    image = load_image("Title_2.png")

    def __init__(self, group):
        super().__init__(group)
        title = pygame.transform.scale(Fb_title_2.image, (700, 100))
        self.image = title
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(300, 810)
        self.sh = 0
        self.dwig = False
        self.rew = False
        self.c = 0

    def update(self):
        if state == "play":
            self.dwig = True
        elif state == "fall":
            self.sh = 0
            self.rew = True
        if self.rew == True:
            if self.c < 1500:
                self.rect = self.rect.move(50, 0)
                self.c += 50
            else:
                self.rew = False
                self.c = 0
        if self.dwig:
            if self.sh < 1500:
                self.rect = self.rect.move(-100, 0)
                self.sh += 100
            else:
                self.dwig = False


#  обновление положения громкости в игре
def sound_update(vol):
    if vol == 1:
        sound1.set_volume(0)
        pygame.mixer.music.set_volume(0)
        vol = 0
        return vol
    elif vol == 0:
        sound1.set_volume(0.3)
        pygame.mixer.music.set_volume(0.1)
        vol = 1
        return vol


#  обновление изображения громкости в игре

def print_vol():
    if vol == 1:
        screen.blit(vol_zn, (1750, 910))
    else:
        screen.blit(mute, (1750, 910))

# партиклы при смерти
class Particle(pygame.sprite.Sprite):
    fire = [load_image("blood.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)) and pygame.transform.rotate(fire[0], random.randint(0, 360)))

    for i in range(len(fire)):
        fire[i] = pygame.transform.rotate(fire[i], random.randint(0, 360))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]

        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 0.1

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity

        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 25
    # возможные скорости
    for _ in range(particle_count):
        Particle(position, random.randint(-15, 15), random.randint(-30, 15))


#  печать счётчика труб
def schet(screen):
    font = pygame.font.Font(None, 150)
    text = font.render(f'{sch}', True, (250, 250, 250))
    text_x = 100
    text_y = 50
    screen.blit(text, (text_x, text_y))


#  обновление счётчика труб

def sch_2(pos, sch):
    if state == "play":
        pos += 4
        sch = (pos - 900) // 600
        if sch < 0:
            sch = 0
        return pos, sch
    elif state == "fall":
        return pos, sch
    elif state == "start":
        return pos, sch
    else:
        return 0, 0


# отработанный тест счётчика очков
"""class Test_sch_2():
    def test_1(self):
        assert sch_2(3706, 4) == (3706, 4)

    def test_2(self):
        assert sch_2(1500, 1) == (1500, 1)

    def test_3(self):
        assert sch_2(1496, 0) == (1496, 0)

    def test_4(self):
        assert sch_2(12, 23) != (11, 23)

    def test_wrong_type(self):
        with pytest.raises(TypeError):
            sch_2({'32', 23})

    def test_list(self):
        with pytest.raises(TypeError):
            sch_2(['34', 'Hi ni...'])"""


#  печать максимального результата

def print_maxim_score(maxim):
    if maxim > 0:
        font = pygame.font.Font(f_ad, 120)
        text = font.render(f'Рекорд: {maxim}', True, (250, 250, 250))
        text_x = 900
        text_y = 600
        screen.blit(text, (text_x, text_y))


class Birds(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = image_bird1
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]


    def update(self):
        for el in pipes:
            if pygame.sprite.collide_mask(self, Truba(el[0])):
                fall()


def fall():
    state = "fall"
    tubing = []



class Truba(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height


#  украшение для пропадания арбуза
def watd(wat_t):
    if wat_t > 0:
        image_w = pygame.transform.scale(image_watermelon, (100 - (wat_t * 20), 100 - (wat_t * 20)))
        screen.blit(image_w, (100, 100))
        screen.blit(image_w, (wp + (20 * (5 - wat_t)), 490 + (20 * (5 - wat_t))))
        wat_t -= 1
        return wat_t
    else:
        return 0

def prov_pipes():
    pip = {'1': 1300 - 817 - 50, '2': 1300 - 662 - 50, '3': 1300 - 525 - 50,
           '4': 1300 - 388 - 50, '5': 1300 - 252 - 50}
    for i in range(200):
        posit = tubing[i // 2]
        pi = (pipes[i // 2])[i % 2]
        k = pi.get_rect()[2]
        l = pi.get_rect()[3]
        if i % 2 == 0:
            s = -110
        else:
            s_y = level[i // 2]
            s = pip[s_y]
        if player.colliderect(pygame.Rect(posit, s, k, l)):
            watermelon()
            return True




#  основной цикл программы

if __name__ == '__main__':
    pygame.mixer.music.stop()
    generation_level_step1()
    generation_level_step2()
    watermelons.append(1750 + 600 * 3)
    watermelon()

    #  Заставка игры
    screen.fill(pygame.Color(40, 40, 40))
    font = pygame.font.Font(f_ad, 180)
    text = font.render(f'Sad juniors', True, (250, 250, 250))
    text_x = 400
    text_y = 400
    screen.blit(text, (text_x, text_y))
    pygame.display.flip()
    clock.tick(0.6)


    f_sp = f_spis()
    Fb_title(all_sprites)
    Fb_title_2(all_sprites)
    pygame.display.set_caption('Flappy bird')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            #  проверка на изменение громкости музыки
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] > 1750 and event.pos[1] > 910:
                    vol = sound_update(vol)

        # обработка нажатий
        press = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        click = press[0] or keys[pygame.K_SPACE]

        # счётчик кадра для анимации птицы
        if kadr < 3 and flag:
            kadr += 0.1
        else:
            kadr = 0



        # проверка для антинажатия мышки(фикс бага)
        if detect > 0:
            detect -= 1

        # состояние начала игры
        if state == "start":
            level_update()

            # запуск фоновой музыки
            pygame.mixer.music.play()

            # проверка на нажатие и проверка на истечение времени ненажатия
            #  + обновление счётчика
            if click and detect == 0:
                state = "play"
                pos, sch = 0, 0
            # изменение координат птицы по y
            player_y += (height // 2 - player_y) * 0.15
            player.y = player_y
        # состояние игры после нажатия мыши
        elif state == "play":
            flag = True

            # регуляровка ускорения

            if click:
                acceleration = -2.1
            else:
                acceleration = 0
            player_y += speed_player
            speed_player = (speed_player + acceleration + 1.0) * 0.94  # если что можно сделать падение медленнее
            player.y = player_y

            # птица вышла за края экрана

            if player.top < 0 or player.bottom > height:
                state = "fall"
                tubing = []
                watermelons = []
                watermelon()

            wat_t = watd(wat_t)


            #  Птица съела арбуз
            for el in watermelons:
                if player.colliderect(pygame.Rect(el, 490, 100, 100)):
                    wp = el
                    for l in range(len(watermelons)):
                        if watermelons[l] == el:
                            watermelons[l] = -2000
                    tubing[sch] = -1000
                    tubing[sch + 1] = -1000
                    wat_t = 5


            # птица столкнулась с трубой(пока не работает)
            '''Birds((x - 10, y - 71))'''
            if state == "play":
                if prov_pipes():
                    state = "fall"
                    tubing = []
                    watermelons = []



        # состояние смерти
        elif state == "fall":
            create_particles((player[0], player[1]))
            flag = False
            state = "start"

            # Обработка максимального результата

            if sch > maxim_score:
                maxim_score = sch

            # остановка фоновой музыки, звук смерти птицы(стон Владислава Алексеевича) и обнуление координат

            pygame.mixer.music.stop()
            sound1.play()
            speed_player = 0
            acceleration = 0
            detect = FPS

        #  конец игры которого нет))

        elif state == "game over":
            pass


        #  так выглядит победа
        if sch == 101:
            running = False
            webbrowser.open('https://www.youtube.com/watch?v=8djnfFx_E0Y', new=2)


        screen.fill(pygame.Color(0, 0, 0))
        screen.blit(image_background, (0, 0))
        print_level()
        pos, sch = sch_2(pos, sch)
        schet(screen)
        print_vol()
        if state == 'start':
            print_maxim_score(maxim_score)


        # отображение и наклоны птицы
        x, y, w, h = player
        img_rotate = pygame.transform.rotate(birds[int(kadr)], -speed_player)
        screen.blit(img_rotate, (x - 10, y - 71))

        #  вывод всей этой красоты на экран
        all_sprites.update()
        all_sprites.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
pygame.quit()


