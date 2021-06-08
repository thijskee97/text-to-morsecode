morse_code_lib = {
    'a' : '. _',
    'b':'_ . . . ',
    'c': '_ . _ .',
    'd': '_ . .',
    'e': '.',
    'f': '. . _ .',
    'g': '_ _ .',
    'h':'. . . .',
    'i': '. .',
    'j': '. _ _ _',
    'k': '_ . _',
    'l': '. _ . .',
    'm': '_ _',
    'n': '_ .',
    'o': '_ _ _',
    'p': '. _ _ .',
    'q': '_ _ . _',
    'r': '. _ .',
    's': '. . .',
    't': '_',
    'u': '. . _',
    'v': '. . . _',
    'w': '. _ _',
    'x': '_ . . _',
    'y':'_ . _ _',
    'z': '_ _ . .',
    ' ': 'space'
}

bericht_normaal = []
bericht_morse_code = []
for letter in input('your message: ').lower():
    bericht_normaal.append(letter)
    print(morse_code_lib[letter])
    morse_letter = morse_code_lib[letter]
    bericht_morse_code.append(morse_letter)

