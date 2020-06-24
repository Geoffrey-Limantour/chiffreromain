def Transpose(i,x,y,z):
    if i ==0:
        return("")
    if i == 1:
        return(x)
    if i == 2:
        return(x+x)
    if i == 3:
        return(x+x+x)
    if i == 4:
        return(x+y)
    if i == 5:
        return(y)
    if i == 6:
        return(y+x)
    if i == 7:
        return(y+x+x)
    if i == 8:
        return(y+x+x+x)
    if i == 9:
        return(x+z)
    else:
        return("error")

def Selector(i):
    centaineArabe = int(i/100)    
    centaineRomain = Transpose(centaineArabe, "C", "D", "M")
    
    dizaineArabe = int((i-centaineArabe*100)/10)
    dizaineRomain = Transpose(dizaineArabe, "X", "L", "C");
    
    uniteArabe = i-centaineArabe*100-dizaineArabe*10
    uniteRomain = Transpose(uniteArabe, "I", "V", "X");
    
    chiffreRomain = centaineRomain + dizaineRomain + uniteRomain

    return(chiffreRomain)