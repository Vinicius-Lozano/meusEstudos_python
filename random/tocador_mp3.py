#mp3
import pygame

pygame.init()
pygame.mixer.music.load ('mixkit-mystwrious-bass-pulse.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()