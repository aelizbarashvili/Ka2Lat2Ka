### Variables:
export Marker='\x0'  # Marker=$'\036' # Marker=$'\034'
export Ka='აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
export Lat='abgdevzTiklmnopJrstufqRySCcZwWxjh'


### Transliteration
---------------------------
sed -e "s/[a-zTJRSCZW]*[a-zTJRSCZW]/${Marker}&${Marker}/g" -e "y/$Ka/$Lat/" File > File_tr


### Detransliteration
--------------------------
sed "s/\(${Marker}[^${Marker}]*[^${Marker}]${Marker}\)\1*/\n&\n /g;G;s/^/ /" File_tr | sed -e '/^ /y/'${Lat}/${Ka}'/;/./{H;d;}' -e'x;s/\n \{0,1\}//g' -e "s/${Marker}//g" >File_restored
