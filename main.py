from Morse import Morse

m = Morse()

def __main__():
    text = input("Phrase to encode: ")
    morse = m.to_morse(text)
    m.play_beeps(morse)
    new_text = m.from_morse(morse)
    print(new_text)

if __name__ == "__main__":
    __main__()