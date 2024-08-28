
### Variables:
export Marker=$'\03'  # (Marker=$'\034')


### Transliteration
---------------------------
vi -c ":%s/[a-zTJRSCZW]*[a-zTJRSCZW]]/$Marker&$Marker/g" -c'%!sed "y/აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ/abgdevzTiklmnopJrstufqRySCcZwWxjh/"' -c':wq' File


### Detransliteration
--------------------------
vim -c "%s/$Marker\zs[^$Marker]*$Marker\|\zs[a-zTJRSCZW]/\=submatch(0) ==# 'a' ? 'ა' : submatch(0) ==# 'b' ? 'ბ' : submatch(0) ==# 'g' ? 'გ' : submatch(0) ==# 'd' ? 'დ' : submatch(0) ==# 'e' ? 'ე' : submatch(0) ==# 'v' ? 'ვ' : submatch(0) ==# 'z' ? 'ზ' : submatch(0) ==# 'T' ? 'თ' : submatch(0) ==# 'i' ? 'ი' : submatch(0) ==# 'k' ? 'კ' : submatch(0) ==# 'l' ? 'ლ' : submatch(0) ==# 'm' ? 'მ' : submatch(0) ==# 'n' ? 'ნ' : submatch(0) ==# 'o' ? 'ო' : submatch(0) ==# 'p' ? 'პ' : submatch(0) ==# 'J' ? 'ჟ' : submatch(0) ==# 'r' ? 'რ' : submatch(0) ==# 's' ? 'ს' : submatch(0) ==# 't' ? 'ტ' : submatch(0) ==# 'u' ? 'უ' : submatch(0) ==# 'f' ? 'ფ' : submatch(0) ==# 'q' ? 'ქ' : submatch(0) ==# 'R' ? 'ღ' : submatch(0) ==# 'y' ? 'ყ' : submatch(0) ==# 'S' ? 'შ' : submatch(0) ==# 'C' ? 'ჩ' : submatch(0) ==# 'c' ? 'ც' : submatch(0) ==# 'Z' ? 'ძ' : submatch(0) ==# 'w' ? 'წ' : submatch(0) ==# 'W' ? 'ჭ' : submatch(0) ==# 'x' ? 'ხ' : submatch(0) ==# 'j' ? 'ჯ' : submatch(0) ==# 'h' ? 'ჰ' : submatch(0)/g" -c "%s/$Marker//g" -c ':wq' File

### Alernative way for detransliteration 
### create a vim function in the file tr.vim
$ cat tr.vim
" translate.vim
function! Translate(char)
    let charmap = {'a': 'ა', 'b': 'ბ', 'g': 'გ', 'd': 'დ', 'e': 'ე', 'v': 'ვ', 'z': 'ზ', 'T': 'თ', 'i': 'ი', 'k': 'კ', 'l': 'ლ', 'm': 'მ', 'n': 'ნ', 'o': 'ო', 'p': 'პ', 'J': 'ჟ', 'r': 'რ', 's': 'ს', 't': 'ტ', 'u': 'უ', 'f': 'ფ', 'q': 'ქ', 'R': 'ღ', 'y': 'ყ', 'S': 'შ', 'C': 'ჩ', 'c': 'ც', 'Z': 'ძ', 'w': 'წ', 'W': 'ჭ', 'x': 'ხ', 'j': 'ჯ', 'h': 'ჰ'}
    return get(charmap, a:char, a:char)
endfunction

vim -S <(echo "source tr.vim") -c "%s/$Marker\zs[^$Marker]*$Marker\|\zs[a-zTJRSCZW]/\=Translate(submatch(0))/g" -c "%s/$Marker//g" -c 'wq' File
