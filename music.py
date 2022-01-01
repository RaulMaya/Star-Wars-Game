import pygame
import time



screen = pygame.display.set_mode ( ( 420 , 240 ) )

playlist = list()
playlist.append ( "music/Star Wars - John Williams - Duel Of The Fates.mp3" )
playlist.append ( "music/Star Wars - John Williams - Duel Of The Fates.mp3" )
playlist.append ( "music/Star Wars - John Williams - Duel Of The Fates.mp3" )

pygame.mixer.music.load ( playlist.pop() )  # Get the first track from the playlist
pygame.mixer.music.queue ( playlist.pop() ) # Queue the 2nd song
pygame.mixer.music.set_endevent ( pygame.USEREVENT )    # Setup the end track event
pygame.mixer.music.play()           # Play the music

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:    # A track has ended
            if len ( playlist ) > 0:       # If there are more tracks in the queue...
                pygame.mixer.music.queue ( playlist.pop() ) # Q

