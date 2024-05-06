# Author: Authey
# Date: 11/06/2020


import pygame
from NightWhenFireworksFlash import night_when_fireworks_flash

midi_music = night_when_fireworks_flash()
music = midi_music.generator()
freq = 44100    # audio CD quality
bit_size = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)
pygame.mixer.init(freq, bit_size, channels, buffer)
clock = pygame.time.Clock()
pygame.mixer.music.load(music)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    clock.tick(30)
