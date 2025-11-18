import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) #8
    kk_img = pg.transform.flip(pg.image.load("fig/3.png"), True, False) #3  
    kk_rct=kk_img.get_rect() #10
    kk_rct.center=300, 200  #10
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200 #5
        screen.blit(bg_img, [-x, 0]) #5
        screen.blit(bg_img2, [-x+1600, 0]) #8
        screen.blit(bg_img, [-x+3200, 0]) #9

        key_lst = pg.key.get_pressed()
        vx,vy=-1,0
        if key_lst[pg.K_UP]:
            vy-=1
        if key_lst[pg.K_DOWN]:
            vy+=1
        if key_lst[pg.K_LEFT]:
            vx-=1    
        if key_lst[pg.K_RIGHT]:
            vx+=1
        kk_rct.move_ip(vx,vy)
        screen.blit(kk_img, kk_rct) #10

        pg.display.update()
        tmr += 1        
        clock.tick(200) #6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()