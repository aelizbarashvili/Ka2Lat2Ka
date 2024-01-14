#!/home/achiko/anaconda3/bin/python3.9

File = 'File_10M'
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

ka2lat = {'\u10D0': 'a',
        '\u10D1': 'b',
        '\u10D2': 'g',
        '\u10D3': 'd',
        '\u10D4': 'e',
        '\u10D5': 'v',
        '\u10D6': 'z',
        '\u10D7': 'T',
        '\u10D8': 'i',
        '\u10D9': 'k',
        '\u10DA': 'l',
        '\u10DB': 'm',
        '\u10DC': 'n',
        '\u10DD': 'o',
        '\u10DE': 'p',
        '\u10DF': 'J',
        '\u10E0': 'r',
        '\u10E1': 's',
        '\u10E2': 't',
        '\u10E3': 'u',
        '\u10E4': 'f',
        '\u10E5': 'q',
        '\u10E6': 'R',
        '\u10E7': 'y',
        '\u10E8': 'S',
        '\u10E9': 'C',
        '\u10EA': 'c',
        '\u10EB': 'Z',
        '\u10EC': 'w',
        '\u10ED': 'W',
        '\u10EE': 'x',
        '\u10EF': 'j',
        '\u10F0': 'h'
}

ka2lat = {'ა': 'a', 'ბ': 'b', 'გ': 'g', 'დ': 'd', 'ე': 'e', 'ვ': 'v', 'ზ': 'z', 'თ': 'T', 'ი': 'i', 'კ': 'k', 'ლ': 'l', 'მ': 'm', 'ნ': 'n', 'ო': 'o', 'პ': 'p', 'ჟ': 'J', 'რ': 'r', 'ს': 's', 'ტ': 't', 'უ': 'u', 'ფ': 'f', 'ქ': 'q', 'ღ': 'R', 'ყ': 'y', 'შ': 'S', 'ჩ': 'C', 'ც': 'c', 'ძ': 'Z', 'წ': 'w', 'ჭ': 'W', 'ხ': 'x', 'ჯ': 'j', 'ჰ': 'h'
}

#აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ/abgdevzTiklmnopJrstufqRySCcZwWxjh

#x = tr('ერiiთი',ka2en)
#print(x)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

x = ''
with open(File) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if c in alpha:
            if x in alpha:
                print(c,end='')
            else:
                print(Marker,c,sep='',end='')
        else:
            if x in alpha:
                print(Marker,tr(c,ka2lat),sep='',end='')
            else:
                print(tr(c,ka2lat),end='')
        x = c
