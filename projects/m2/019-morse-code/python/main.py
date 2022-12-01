def translate_into_morse(entered_message):
    morse_code = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", 
    "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...",
    "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "1":".----", "2":"..---", "3":"...--",
    "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----", "Á":".--.-", "É":"..-..",
    "Ö":"---.", "Ä":".-.-", "Ñ":"--.--", "Ü":"..--"}
    translated_message = ""
    for character in entered_message:
        if character.upper() in morse_code:
            translated_message += morse_code[character.upper()] + " "
    return translated_message

def main():
    user_message = input("Enter a message to translate: ")
    print ("Translated message:", translate_into_morse(user_message))

if __name__ == "__main__":
    main()