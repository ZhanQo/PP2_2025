import pygame
import os


pygame.init()
pygame.mixer.init()


s = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music")


MUSIC_FOLDER = r"C:\Users\Есен\OneDrive\Рабочий стол\songs"


music_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
if not music_files:
    print("no .mp3")
    exit()


tr = 0


def start(track):
    track_path = os.path.join(MUSIC_FOLDER, music_files[track])
    print(f"Now playing: {music_files[track]}")
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()

start(tr)

running = True
paused = False

print("\nуправление: SPACE - Play/Pause, S - Stop, N - Next, P - Previous")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                    print("on pause")
                else:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("continue")

            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
                print("stop")

            elif event.key == pygame.K_n:  # Next
                current_track = (current_track + 1) % len(music_files)
                start(current_track)

            elif event.key == pygame.K_p:  # Previous
                current_track = (current_track - 1) % len(music_files)
                start(current_track)

    pygame.display.flip()  

pygame.quit()