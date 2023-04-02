#!/usr/bin/env python
import random, sys
    
if __name__ == '__main__':

    n = 1
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    column_a=('poncy','fucking','little','bloody','dodgy','manky','poxy','skanky','arse-licking','cack-handed','complete','stupid','pikey','total','half-arsed', 'whiny','shitty', 'shitey', 'tiny-fingered','mangled')
    column_b=('arse','shit','fucking','cock-up','wanking','little','bastard','minging','shit-faced','whinging','inebriated','cunty','piss-pot','twat-faced','jizzmongering','cheeto-faced','ferret-wearing')
    column_c=('pillock','bollocks','cunt','piss-artist','monkey','pillow muncher','arsehole','bugger','chav','git','minger','muppet','nancy','numpty','nutter','pikey','plonker','prat','trollop','tosser','wanker','slag','knob-head','arse licker','twat','slapper','bell-end','nonce','wank-stain','dickhead','bender','tit-head','fag','poofter','chocolate raider','arsebadger','piss-stain','fucknugget','wazzock','fanny-flaps','cockwomble','spunktrumpet','cuntpuddle','shit-pouch','tosspot','fuckwit',"shitgibbon",'cockwomble','cocksplat','jizztrumpet')

    na=column_a.__len__()
    nb=column_b.__len__()
    nc=column_c.__len__()

    for i in range(n):
        ia=int(random.random()*na)
        ib=int(random.random()*nb)
        ic=int(random.random()*nc)
        insult=column_a[ia]+' '+column_b[ib]+' '+column_c[ic]
        print(insult)
