decoded_phrase = []

keyboard = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', "\\",
'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

while True:
    try:
        phrase = str(input()).upper()

    except EOFError:
        break

    else:
        char_list = [char for char in phrase]

        for index, char in enumerate(char_list):

            if char in keyboard:
                i = keyboard.index(char)
                decoded_phrase.append(keyboard[i - 1] if i > 0 else char)
            else:
                decoded_phrase.append(' ')

        print(''.join(decoded_phrase))
        decoded_phrase.clear()