# Margaret Chen (mdc5bv) and Alice Zormelo (adz8cc)

import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
character = gamebox.from_color(50, 50, "red", 30, 60)
character.image = 'squidward.png'
character.size = [80,80]
character.yspeed = 0
enemy = gamebox.from_color(50, 550, "green", 30, 60)
enemy.image = 'spongebob.jpg'
enemy.size = [80,80]
enemy.yspeed = 0
background = gamebox.from_image(400, 285,'bikini_bottom.png')
walls = [gamebox.from_color(-100, 600, "seagreen", 3000, 60), gamebox.from_color(200, 450, "seagreen", 200, 20), gamebox.from_color(600, 450, "seagreen", 200, 20),
         gamebox.from_color(100, 300, "skyblue", 200, 20), gamebox.from_color(400, 300, "skyblue", 200, 20), gamebox.from_color(700, 300, "skyblue", 200, 20),
         gamebox.from_color(200, 150, "skyblue", 200, 20), gamebox.from_color(600, 150, "skyblue", 200, 20)]
coins = [gamebox.from_image(0,0,'krabby_patty.png')]
time = 1810
score = 0
counter = 0
current_health = 100
fire = []
agreed = False

def tick(keys):
    global time, score, counter, current_health, agreed
    camera.clear("cyan")
    line = gamebox.from_text(560, 25, "Created by: Alice Zormelo (adz8cc) and Margaret Chen (mdc5bv)", "Arial",15,"black")
    line1 = gamebox.from_text(400,90,"Welcome to Bikini Bottom!","Arial",34,"black")
    line2 = gamebox.from_text(400,140, "This is a 2 player game, one will play as Squidward, and the other will play as Spongebob.", "Arial",20,"black")
    line3 = gamebox.from_text(400, 190, "Squidward's objective is to collect as many krabby patties as possible to boost his health.", "Arial",20,"black")
    line4 = gamebox.from_text(400, 240, "Spongebob's objective is to stop Squidward by using his rocks.", "Arial",20,"black")
    line5 = gamebox.from_text(400, 290, "To control Squidward, use the left and right keys and space to jump.", "Arial",20,"black")
    line6 = gamebox.from_text(400, 340, "To control Spongebob, use 'a' for left and 'd' for right and 'w' to shoot.","Arial",20,"black")
    line7 = gamebox.from_text(400, 390, "If the timer runs out, Squidward wins!", "Arial",20,"black")
    line8 = gamebox.from_text(400, 440, "If Squidward's health meter runs out, Spongebob wins!", "Arial",20,"black")
    line9 = gamebox.from_text(400, 490, "PRESS SPACE TO START", "Arial",30,"black")
    camera.draw(line1)
    camera.draw(line2)
    camera.draw(line3)
    camera.draw(line4)
    camera.draw(line5)
    camera.draw(line6)
    camera.draw(line7)
    camera.draw(line8)
    camera.draw(line9)
    camera.draw(line)
    if pygame.K_SPACE in keys:
        agreed = True
    if agreed == True:

        time -= 1
        seconds = str(int((time / ticks_per_second))).zfill(3)

        camera.clear("cyan")
        background.size = 800,600
        camera.draw(background)

        if pygame.K_RIGHT in keys:
            character.x += 5
        if pygame.K_LEFT in keys:
            character.x -= 5
        if pygame.K_d in keys:
            enemy.x += 5
        if pygame.K_a in keys:
            enemy.x -= 5
        if pygame.K_w in keys:
            new_shot = gamebox.from_color(enemy.x,enemy.y,"saddlebrown",8,8)
            fire.append(new_shot)

        character.yspeed += 1
        character.y = character.y + character.yspeed
        enemy.y = enemy.y + enemy.yspeed

        for wall in walls:
            if character.bottom_touches(wall):
                character.yspeed = 0
                if pygame.K_SPACE in keys:
                    character.yspeed = -18
            if character.touches(wall):
                character.move_to_stop_overlapping(wall)
            camera.draw(wall)


        for shot in fire:
            if character.touches(shot):
                current_health -= 1
                fire.remove(shot)
                if current_health <= 0:
                    camera.draw(gamebox.from_text(400,100, "Spongebob Wins!", "Arial", 70, "red"))
                    gamebox.pause()
            shot.y -= 3
            camera.draw(shot)

        health_bar = gamebox.from_color(260, 30, 'plum', current_health*2, 30)
        camera.draw(health_bar)

        time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, "arial", 24, "white")
        score_box = gamebox.from_text(80, 30, "Health Meter", "arial", 24, "white")
        camera.draw(time_box)
        camera.draw(score_box)

        counter += 1
        if counter % 50 == 0:
            new_coin = gamebox.from_image(random.randint(0, 800), random.randint(100, 500), 'krabby_patty.png')
            new_coin.size = 50,50
            coins.append(new_coin)
        for coin in coins:
            if character.touches(coin):
                current_health += 1
                coins.remove(coin)
            camera.draw(coin)

        if time <= 0:
            camera.draw(gamebox.from_text(400, 100, "Squidward Wins!", "Arial", 70, "red"))
            gamebox.pause()

        camera.draw(character)
        camera.draw(enemy)
    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)


