# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:32:13 2024

@author: kinga
"""

import pygame, random, simpleGE

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(25, 25)
        self.reset()
        self.coinSound = simpleGE.Sound("coinEffect.WAV")
        
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Boy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("boy.png")
        self.setSize(90, 90)
        self.position = (320, 400)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("plainField.png")
        self.boy = Boy(self)  # Corrected the variable name
        self.coins = []
        for i in range(10):
            self.coins.append(Coin(self))
                
        # Load and play background music
        pygame.mixer.music.load("newSong.mp3")
        pygame.mixer.music.set_volume(.3)
        pygame.mixer.music.play(-1)  # -1 indicates loop indefinitely

        self.sprites = [self.boy,  # Corrected the variable name
                        self.coins]
    
    def process(self):
        for coin in self.coins:
            if coin.collidesWith(self.boy):
                coin.coinSound.play()
                coin.reset()
def main():
   
    game = Game()
    game.start()

if __name__ == "__main__":
    main()

