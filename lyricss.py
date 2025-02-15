import time

def print_lyrics():
    lyrics = [
        ("", 1.0, 0.1),
        ("...", 10, 0.1),
        ("", 1.0, 0.1),
        ("Your morning eyes, I could stare like watching stars", 0.1, 0.13),
        ("I could walk you by, and I'll tell without a thought", 0.1, 0.11),
        ("You'd be mine, would you mind if I took your hand tonight?", 0.1, 0.13),
        ("Know you're all that I want this life", 0.1, 0.16),
        ("", 1.0, 0.1),
        ("", 1.0, 0.1),
        ("I'll imagine we fell in love",0.1 , 0.09),
        ("I'll nap under moonlight skies with you", 0.1, 0.1),
        ("I think I'll picture us, you with the waves", 0.1, 0.09),
        ("The ocean's colors on your face", 0.1, 0.12),
        ("I'll leave my heart with your air", 0.1, 0.12),
        ("So let me fly with you", 0.1, 0.15),
        ("Will you be forever with me?", 0.1, 0.16),
        ("", 0.5, 0.1),
        ("...", 31, 0.1),
        ("", 0.6, 0.1),
        ("My love will always stay by you", 0.7, 0.16),
        ("I'll keep it safe, so don't you worry a thing, I'll tell you I love you more", 0.6, 0.11),
        ("It's stuck with you forever, so promise you won't let it go", 0.2, 0.11),
        ("I'll trust the universe will always bring me to you...", 0.1, 0.12),
        ("", 0.7, 0.1),
        ("", 0.6, 0.1),
        ("I'll imagine we fell in love", 0.2, 0.12),
        ("I'll nap under moonlight skies with you", 0.18, 0.1),
        ("I think I'll picture us, you with the waves", 0.18, 0.08),
        ("The ocean's colors on your face", 0.18, 0.1),
        ("I'll leave my heart with your air", 0.18, 0.12),
        ("So let me fly with you", 0.2, 0.15),
        ("Will you be forever with me???", 0.1, 0.18),
        ("", 0.7, 0.0),
        ("...", 5.3, 0.1),
    ]

    for line_text, line_delay, char_delay in lyrics:
        for char in line_text:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(line_delay)

if __name__ == "__main__":
    print_lyrics()
