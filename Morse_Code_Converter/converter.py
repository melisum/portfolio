alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1','2','3','4','5','6','7','8','9']
morse= {"a":".-",
"b":"-...",
"c":"-.-.","d":"-..","e":".","f":"..-.",
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
"1":".----",
"2":"..---",
"3":"...--",
"4":"....-",
"5":".....",
"6":"-....",
"7":"--...",
"8":"---..",
"9":"----.",
"0":"-----",
" ":"/",
"-":"-....-",
".":".-.-.-",
"?":"..--..",
"!":"-.-.--",
",":"--..--",
"'":".----.",
}

def morse_converter():
    want_to_continue=True
    while want_to_continue:
        return_message=""
        text_to_convert=input("Type in your text: \n")
        for symbol in text_to_convert:
            for character in morse.keys():
                if symbol == character:
                    return_message+=morse[character]
                    return_message+=" "
        print(return_message)
        to_continue=input("Do you want to continue? Y or N: \n")
        if to_continue == "N":
            want_to_continue=False

morse_converter()
