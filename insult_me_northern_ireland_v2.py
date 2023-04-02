#!/usr/bin/env python
import random, sys
    
if __name__ == '__main__':

    n = 1
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    column_a=('fucking','little','wee','friggin','feckin','full-on','spasticated','slabbering','steaming')
    column_b=('arse','shite','fuckin','minging','spidey','bolloxed','banjaxed','pole-axed','cunty','ugly-baked')
    column_c=('cunt','slapper','wank-stain','dickhead','ballsack','eeijit','buck-eeijit','blurt','ring','tube','spide','minger','nob','spastic','fucker','hole','munter','ballroot','dick-wad','maggot','gobshite','dogs-dinner','hallion','rocket','flid','taig','hun','prod','ballbag')

    na=column_a.__len__()
    nb=column_b.__len__()
    nc=column_c.__len__()
    
    for i in range(n):
        ia=int(random.random()*na)
        ib=int(random.random()*nb)
        ic=int(random.random()*nc)
        insult=column_a[ia]+' '+column_b[ib]+' '+column_c[ic]
        print(insult)
