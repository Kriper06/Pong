from pygame import *
clock=time.Clock()
window=display.set_mode((700,500))
window.fill((0,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(size_x, size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 405:
            self.rect.y += self.speed
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 405:
            self.rect.y += self.speed
Player_l=Player("Ракетка_Pong.png",20,200,30,140,5)
Player_r=Player("Ракетка_Pong.png",670,200,30,140,5)
ball=GameSprite("Мяч_Pong.png",250,360,30,30,0)
game=True
speed_x=3
speed_y=3
font1=font.Font(None,35)
lose1=font1.render("PLAYER L LOSE!", True, (180, 0, 0))
font2=font.Font(None,35)
lose2=font2.render("PLAYER R LOSE!", True, (180, 0, 0))
while game:
    window.fill((0,0,0))
    Player_l.reset()
    Player_r.reset()
    ball.reset()
    Player_l.update_l()
    Player_r.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y>470 or ball.rect.y<0:
        speed_y *= -1
    if sprite.collide_rect(Player_l,ball) or sprite.collide_rect(Player_r,ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish=True
        window.blit(lose1, (200,200))
    if ball.rect.x > 700:
        finish=True
        window.blit(lose2, (200,200))
    for e in event.get():
        if e.type==QUIT:
            game=False
    clock.tick(60)
    display.update()