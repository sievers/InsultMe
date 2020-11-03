#!/usr/bin/env python
import random
import pyttsx3
    
if __name__ == '__main__':

	engine = pyttsx3.init()
	engine.setProperty('rate', 150)

	column_a=('lazy','stupid','insecure','idiotic','slimy','slutty','smelly','pompous','communist','dicknose','pie-eating','racist','elitist','white trash','drug-loving','butterface','tone deaf','ugly','creepy')
	column_b=('douch','ass','turd','rectum','butt','cock','shit','crotch','bitch','turd','prick','slut','taint','fuck','dick','boner','shart','nut','sphincter','menstrual','spigot','gigalo','pus','pillow','pole','chocolate')
	column_c=('pilot','canoe','captain','pirate','hammer','knob','box','jockey','nazi','waffle','goblin','blossom','biscuit','clown','socket','monster','hound','dragon','balloon','admiral','snarfer','muncher','burgler','gunner','swallower','gargler','swallower','muncher','raider')

	na=column_a.__len__()
	nb=column_b.__len__()
	nc=column_c.__len__()

	ia=int(random.random()*na)
	ib=int(random.random()*nb)
	ic=int(random.random()*nc)
	insult=column_a[ia]+' '+column_b[ib]+' '+column_c[ic]

	print(insult)
	engine.say(insult)
	engine.runAndWait()