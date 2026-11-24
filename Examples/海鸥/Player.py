"""Generate and play the guitar arrangement of 海鸥."""
import pygame

from Seagull import Seagull


def main():
    music = Seagull().generator()
    pygame.mixer.init(44100, -16, 2, 2048)
    try:
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(30)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


if __name__ == '__main__':
    main()
