import time 

def display_lyrics_with_tempo(lyrics, tempo):
    for line, duration in zip(lyrics, tempo):
        print(line)
        time.sleep(duration)

if __name__ == "__main__":
    #lyrics lagu
    lyrics = [
        "She's be my queen",
        "Since we were 16",
        "We want the same things",
        "We dream the same dreams",
        "Alright",
        "Alright",
    ]

    tempo = [1.5, 1.5, 1.5, 1.5, 2.5, 4]

    display_lyrics_with_tempo(lyrics, tempo)