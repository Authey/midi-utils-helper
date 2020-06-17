# Author: Authey
# Date: 11/06/2020


import pygame
from SomeMusic import some_music

midi_music = some_music()
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

