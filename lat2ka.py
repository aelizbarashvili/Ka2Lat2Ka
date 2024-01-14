#!/home/achiko/anaconda3/bin/python3.9

File = '5_tr.txt'
Marker = chr(0)

def tr(text, translit_table):
    converted_text = ''
    for char in text:
        transchar = ''
        if char in translit_table:
            transchar = translit_table[char]
        else:
            transchar = char
        converted_text += transchar
    return converted_text

lat2ka={'a': '\u10D0',
       'b': '\u10D1',
       'g': '\u10D2',
       'd': '\u10D3',
       'e': '\u10D4',
       'v': '\u10D5',
       'z': '\u10D6',
       'T': '\u10D7',
       'i': '\u10D8',
       'k': '\u10D9',
       'l': '\u10DA',
       'm': '\u10DB',
       'n': '\u10DC',
       'o': '\u10DD',
       'p': '\u10DE',
       'J': '\u10DF',
       'r': '\u10E0',
       's': '\u10E1',
       't': '\u10E2',
       'u': '\u10E3',
       'f': '\u10E4',
       'q': '\u10E5',
       'R': '\u10E6',
       'y': '\u10E7',
       'S': '\u10E8',
       'C': '\u10E9',
       'c': '\u10EA',
       'Z': '\u10EB',
       'w': '\u10EC',
       'W': '\u10ED',
       'x': '\u10EE',
       'j': '\u10EF',
       'h': '\u10F0'
}

alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#x = tr('ერiiთი',en2ka)
#print(x)

x = ''; y = False;

with open(File) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if c in alpha:
            if x == Marker:
                if y is True:
                    print(c,end='')
                else:
                    print(tr(c,lat2ka),end='')
            else:
                if y is True:
                    print(c,end='')
                else:
                    print(tr(c,lat2ka),end='')
        elif c == Marker:
                y = not y
                k = c
        else:
            print(c,end='')
        x = c
