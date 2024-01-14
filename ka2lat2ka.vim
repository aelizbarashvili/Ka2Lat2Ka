
vi -c ":%s/[[:alpha:]]*[[:alpha:]]/$Marker&$Marker/g" -c'%!sed "y/აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ/abgdevzTiklmnopJrstufqRySCcZwWxjh/"' -c':wq' file
