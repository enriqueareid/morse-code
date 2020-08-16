import json


print("""
 ______________                                                  
|   __    __   |                                                 
|  |  |  |  |  |  __________   __          _________   _________ 
|  |  |  |  |  | |   ____   | |  |-----|  /        /  |   ___   |
|  |  |  |  |  | |  |    |  | |    ____| (  ------(   |  |___|  |
|  |  |  |  |  | |  |    |  | |   /       \______  \  |   ______|
|  |  |  |  |  | |  |____|  | |  |        |         ) |  |______ 
|__|  |__|  |__| |__________| |__|        /________/  |_________|

 _________                        __
|         |                      |  |
|    _____|  __________   _______|  |    _________
|   |       |   ____   | |   ____   |   |   ___   |
|   |       |  |    |  | |  |    |  |   |  |___|  |
|   |_____  |  |    |  | |  |    |  |   |   ______|
|         | |  |____|  | |  |____|  |__ |  |______
|_________| |__________| |____________| |_________|
""")
print("-   •-•   •-   -•   •••   •-••   •-   -   ---   •-•")
print("\n\n\n")

# Character to Morse Code Translator
def morse_translator(x, y='a2m'):
    # Load Morse Code json file as a dictionar
    with open('morseCode.json', 'r') as f:
        morse_code = json.load(f) 

    x = x.strip()
    out_str = ""

    if y == 'a2m': # ABC to Morse Code
        for char in x:
            try: # In case the key isn't in the dictionary
                if char == " ":
                    out_str += '    '
                else:
                    out_str += morse_code[char] + '   '
            except KeyError:
                out_str += '<' + char + '>   '
    elif y == 'm2a':
        x = x.replace('.', '•').replace('_', '-')
        morse_code = {value:key for key, value in morse_code.items()} # Reverse keys and values
        
        x_split = x.split('      ')
        for i in range(len(x_split)):
            x_split[i] = x_split[i].split('  ')

        for word in x_split:
            for char in word:
                if char == '':
                    pass
                else:
                    try:
                        char = char.strip()
                        out_str += morse_code[char]
                    except KeyError:
                        out_str += '<' + char + '>'
            out_str += ' '

    return out_str

# User Input
translate_again = 'placeholder'
while translate_again != False:
    translate_again = 'placeholder'
    language = 'placeholder'
    while language not in ('a2m', 'm2a'):
        language = input("Translate from ABC to Morse Code(m),  or vice versa(a): ").lower() 
        if language in ('morse' or 'm'):
            language = 'a2m'
            in_str = input("Enter the message that you want to translate: ").upper()
            print("\nOutputted Morse Code: ")
        elif language in ('abc' or 'a'):
            language = 'm2a'
            print("""
            Instructions:
                1) Dits can be represented with '.' or '•'
                2) Dahs can be represented with '_' or '-'
                3) There should be NO space in between Dits and Dahs
                4) There should be 3 spaces in between characters
                5) There should be 7 spaces in between words
    
            """)
            in_str = input("Enter the message that you want to translate: ")
            print("\nOutputted ABC: ")

        out_str = morse_translator(in_str, language)
        print(out_str + "\n")
        
        # Ask user if they want to translate again
        while type(translate_again) != bool:
            translate_again = input("Translate again? (y/n): ").lower()
            if translate_again in ('yes', 'y'):
                translate_again = True
            elif translate_again in ('no', 'n'):
                translate_again = False
