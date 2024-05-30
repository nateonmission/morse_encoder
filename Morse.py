import numpy
import pygame

class Morse:

    MORSE_CODE = {
        "a":".-",
        "b":"-...",
        "c":"-.-.",
        "d":"-..",
        "e":".",
        "f":"..-.",
        "g":"--.",
        "h":"....",
        "i":"..",
        "j":".---",
        "k":"-.-",
        "l":".-..",
        "m":"--",
        "n":"-.",
        "o":"---",
        "p":".--.",
        "q":"--.-",
        "r":".-.",
        "s":"...",
        "t":"-",
        "u":"..-",
        "v":"...-",
        "w":".--",
        "x":"-..-",
        "y":"-.--",
        "z":"--..",
        "0":"-----",
        "1":".----",
        "2":"..---",
        "3":"...--",
        "4":"....-",
        "5":".....",
        "6":"-....",
        "7":"--...",
        "8":"---..",
        "9":"----.",
        ",":"--..--",
        ".":".-.-.-",
        "?":"..--..",
        ";":"-.-.-",
        ":":"---...",
        "/":"-..-.",
        "-":"-....-",
        "'":".----.",
        "(":"-.--.",
        ")":"-.--.-",
        "_":"..--.-",
        "@":".--.-.",
        "!":"-.-.--",
        "&":".-...",
        "=":"-...-",
        "+":".-.-.",
        "\"":".-..-.",
        "$":"...-..-",
        # "á":".--.-",
        # "ä":".-.-",
        # "ç":"-.-..",
        # "ch":"----",
        # "đ":"..--.",
        # "é":"..-..",
        # "è":".-..-",
        # "ĝ":"--.-.",
        # "ĵ":".---.",
        # "ñ":"--.--",
        # "ö":"---.",
        # "š":"...-.",
        # "þ":".--..",
        # "ü":"..--",
        # "wait":".-...",
        # "over":"-.-",
        # "error":"........",
        # "end":"...-.-",
        # "roger":"...-.",
        # "start":"-.-.-",
    }

    SPECIAL_CHARS = ",.?;:/-'()_@!&=+\"$"

    def to_morse(self, text) -> str:
        morse = ""
        prosign = ""
        is_Prosign = False
        for letter in text:
            if is_Prosign and letter == ">":
                morse += self.MORSE_CODE[prosign] + "   "
                prosign = ""
                is_Prosign = False
            elif is_Prosign:
                prosign += letter.lower()
            elif letter == "<":
                is_Prosign = True
                pass
            elif letter == " ":
                morse += "    "
            elif letter.isalnum() or letter in self.SPECIAL_CHARS:
                morse += self.MORSE_CODE[letter.lower()] + "   "
            else:
                morse += "\n"
        morse += "\n"
        print(text)
        print(morse) # .replace("|", "     "))
        return morse
    
    def from_morse(self, morse):
        text = ""

        space_count = 0
        space_counting = False
        prosign = ""
        is_prosign = False
        char_string = ""

        for char in morse:
            if not space_counting and (char == "." or char == "-"):
                char_string += char
            elif space_counting and (char == "." or char == "-"):
                if space_count > 6:
                    text += " "
                char_string += char
                space_counting = False
                space_count = 0
            elif not space_counting and char == " ":
                for key, value in self.MORSE_CODE.items():
                    if char_string == value:
                        if len(key) > 1:
                            text += f"<{key}>"
                        else:
                            text += key
                        char_string = ""
                space_count += 1
                space_counting = True
            elif space_counting and char == " ":
                space_count += 1

        return text
    
    def play_beeps(self, morse) -> int:
    # Audio settings
        sampleRate = 44100
        freq = 440
        unit = 98
        pygame.mixer.init(44100,-16,2,512)
        arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
        arr2 = numpy.c_[arr,arr]
        sound = pygame.sndarray.make_sound(arr2)

        def dash():
            sound.play(-1)
            pygame.time.delay(unit * 3)
            sound.stop()

        def dot():
            sound.play(-1)
            pygame.time.delay(unit)
            sound.stop()

        def pause():
            pygame.time.delay(unit)

        for letter in morse:
            if letter == ".":
                dot()
                pause()
            elif letter == "-":
                dash()
                pause()
            elif letter == " ":
                pause()

        return 0