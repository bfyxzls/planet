import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import random
import time
pygame.init()  #游戏初始化
pygame.mixer.init()  #混音器初始化
#游戏背景音乐
#pygame.mixer.music.load("./sound/game_music.wav")
#pygame.mixer.music.set_volume(0.2)
#子弹发射音乐
#bullet_sound = pygame.mixer.Sound("./sound/bullet.wav")
#bullet_sound.set_volume(0.2)
#我方飞机挂了的音乐
#me_down_sound = pygame.mixer.Sound("./sound/game_over.wav")
#me_down_sound.set_volume(0.2)
#敌方飞机挂了的音乐
#enemy_down_sound = pygame.mixer.Sound("./sound/enemy1_down.wav")
#enemy_down_sound.set_volume(0.2)

#设置定时器事件
CREAT_ENEMY = pygame.USEREVENT
pygame.time.set_timer(CREAT_ENEMY, 1000)

#创建一个窗口，用来显示内容
screen = pygame.display.set_mode((480, 800), 0, 32)


class Base(object):
    def __init__(self, screen):
        self.screen = screen


class Plan(Base):
    def __init__(self, screen):
        super().__init__(screen)

        self.image = pygame.image.load(self.imageName).convert()
        self.bulletList = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bulletList.remove(bullet)


class GamePlan(Plan, pygame.sprite.Sprite):
    def __init__(self, screen):
        self.imageName = "./image/hero/fly/hero1.png"
        super().__init__(screen)
        Sprite.__init__(self)

        self.rect = self.image.get_rect()

        self.rect.x = 200
        self.rect.y = 680
        #加载我机损毁图片
        self.bomb1 = pygame.image.load("./image/Enemy/down/enemy1_down1.png")
        self.bomb2 = pygame.image.load("./image/Enemy/down/enemy1_down2.png")
        self.bomb3 = pygame.image.load("./image/Enemy/down/enemy1_down3.png")
        self.bombList = [self.bomb1, self.bomb2, self.bomb3]

    def display(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def moveLeft(self):
        if self.rect.x >= 0:
            self.rect.x -= 20

    def moveRight(self):
        if self.rect.x < 480 - 100:
            self.rect.x += 20

    def moveUp(self):
        if self.rect.y > 0:
            self.rect.y -= 20

    def moveDown(self):
        if self.rect.y < 860 - 124:
            self.rect.y += 20

    def _del_(self):
        print("游戏结束")

    def shootbullet(self):
        Newbullet = PublicBullet(self.rect.x, self.rect.y, self.screen)
        self.bulletList.append(Newbullet)
    # bullet_sound.play()


class EnemyPlan(Plan, pygame.sprite.Sprite):
    def __init__(self, screen):
        self.speed = random.randint(1, 3)
        self.imageName = "./image/Enemy/fly/enemy1.png"
        super().__init__(screen)
        Sprite.__init__(self)
        #确定敌机位置
        self.rect = self.image.get_rect()
        self.reset()
        #加载敌机损毁图片
        self.bomb1 = pygame.image.load( "./image/Enemy/down/enemy1_down1.png")
        self.bomb2 = pygame.image.load("./image/Enemy/down/enemy1_down2.png")
        self.bomb3 = pygame.image.load("./image/Enemy/down/enemy1_down3.png")
        self.bombList = [self.bomb1, self.bomb2, self.bomb3]

    def reset(self):

        self.rect.x = random.randint(0, 400)
        self.rect.y = 0

    def move(self):
        self.rect.y += self.speed

    def update(self):
        if self.rect.y > 860:
            self.kill()

    def _del_(self):
        print("敌机挂了")


class PublicBullet(Base):
    def __init__(self, x, y, screen):
        super().__init__(screen)
        self.imageName = "./image/bullet/fly/bullet1.png"
        self.x = x + 40
        self.y = y - 20
        self.image = pygame.image.load(self.imageName).convert()

    def move(self):
        self.y -= 4

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0 or self.y > 860:
            return True
        else:
            return False


#设置敌机精灵组
enemy = EnemyPlan(screen)
enemy1 = EnemyPlan(screen)
enemy2 = EnemyPlan(screen)
enemy3 = EnemyPlan(screen)
enemy4 = EnemyPlan(screen)
enemy5 = EnemyPlan(screen)
enemy6 = EnemyPlan(screen)
enemy7 = EnemyPlan(screen)
enemy_group = pygame.sprite.Group(enemy, enemy1, enemy2, enemy3, enemy4,
                                  enemy5, enemy6, enemy7)

gamePlan = GamePlan(screen)


def key_control(gamePlan):
    for event in pygame.event.get():
        #退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == CREAT_ENEMY:
            enemy = EnemyPlan(screen)
            enemy_group.add(enemy)
        #按键
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                gamePlan.moveLeft()
            elif event.key == K_RIGHT:
                gamePlan.moveRight()
            elif event.key == K_UP:
                gamePlan.moveUp()
            elif event.key == K_DOWN:
                gamePlan.moveDown()
            elif event.key == K_SPACE:
                gamePlan.shootbullet()


def main():
    #创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 800), 0, 32)
    #创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./image/background.png").convert()
    #
    clock = pygame.time.Clock()
   # pygame.mixer.music.play(-1)
    enemy_index = 0
    plan_index = 0
    score = 0
    while True:
        #设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 刷新帧率
        clock.tick(60)
        gamePlan.display()

        #让精灵组中所有精灵更新位置
        enemy_group.update()
        enemy_group.draw(screen)

        for enemy in enemy_group:
            enemy.move()
            x1 = enemy.rect.x
            x2 = enemy.rect.x + 51
            y1 = enemy.rect.y
            y2 = enemy.rect.y + 39
            for bullet in gamePlan.bulletList:
                x = bullet.x
                y = bullet.y
                a = x > x1 and x < x2 and y > y1 and y < y2
                if a:
                    screen.blit(enemy.bombList[enemy_index], enemy.rect)
                    enemy_index = (enemy_index + 1) % 3
                    time.sleep(0.022)
                    if enemy_index == 0:
                        #enemy_down_sound.play()
                        enemy.kill()
                        score += 10
            c1 = gamePlan.rect.x
            c2 = gamePlan.rect.x + 100
            d1 = gamePlan.rect.y
            b = c1 < x2 and c2 > x1 and d1 < y2
            if b:
                screen.blit(enemy.bombList[enemy_index], enemy.rect)
                screen.blit(gamePlan.bombList[plan_index], gamePlan.rect)
                plan_index = (plan_index + 1) % 3
                time.sleep(0.022)
                if plan_index == 0:
                    #me_down_sound.play()
                    says = ("Game Over!")
                    my_font = pygame.font.SysFont("UbuntuMono-Bold1", 84)
                    says_suface = my_font.render(says, True, (10, 10, 10))
                    pygame.image.save(says_suface, "hello.png")
                    screen.blit(says_suface, (100, 300))
                    say = ("SCORE:%d" % score)
                    my_font = pygame.font.SysFont("UbuntuMono-Bold1", 64)
                    say_surface = my_font.render(say, True, (0, 0, 0))
                    pygame.image.save(say_surface, "12.png")
                    screen.blit(say_surface, (150, 400))

        key_control(gamePlan)
        pygame.display.update()


if __name__ == "__main__":

    main()