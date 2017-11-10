#leitura e execução de arquivo MP3
'''import pygame
pygame.init()

pygame.mixer.music.load('bom_bom_pai.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

from pygame import mixer, time
mixer.init()

mixer.music.load('bom_bom_pai.mp3')
mixer.music.play()

while mixer.music.get_busy():
    pass
