# -*- coding: utf-8 -*-

# Baby Development - first questions listed with initial logic"

# defining variables

print "Please enter below the age of the baby (in months)"
month = raw_input("> ")
# here I want to add in a drop-down menue to choose the months 1...12
# also want to have the person enter the birth month and year and have the age calculated, not entered

print "Is the baby a 'he' or a 'she'?"
sex = raw_input(" ")

if sex != "he" or "she":
    print "Error: please write either 'he' or 'she'"
else:
	print "The baby is a %r, and %r is %r months old" % (sex, sex, month)
	


if month == "0":
	print """Your friends have just become parents. There's so much to ask about the newborn! For example: 
	\n1. Did the birth go smoothly?
	\n2. Was everything okay with the baby? How soon did they let you home from the hospital?
	\n3. How big was %d at birth?
	\n4. What colour are the baby's eyes?
	\n5. Is %d crying a lot or is %d sleeping well?
	\n6. Are you getting enough sleep? How do you feel? (to ask from the newborn' parents""" % (sex, sex, sex) 
elif month =="2" or month =="3":
	print """During the first three months, babies' bodies and brains are learning to live in the outside world. 
	\nQuestions to ask from the parents: 
	\n1. Is %d crying a lot or is %d sleeping well?
	\n2. Does the baby react already to your smile? 
	\n3. Does %d smile back at you? 
	\n4. Can the baby raise his/her head already when on his/her tummy? 
	\n5. Does %d try to clap his/her hands already? 
	\n6. Can %d grip objects?
	\n7. Is %d holding his/her head already?""" % (sex, sex, sex, sex, sex, sex)
elif month =="4" or month =="5" or month =="6":
	print """During months 4 to 6, babies are really learning to reach out and manipulate the world around them. 
	They’re mastering the use of those amazing tools, their hands. And they’re discovering their voices.
	\nQuestions do ask from the parents at this stage: 
	\n1. Is the baby sleeping well?
	\n2. Can %d already roll over from front to back or back to front? (Front-to-back usually comes first)
	\n3. Does %d babble a lot? Making funny sounds? 
	\n4. Does %d laugh a lot? 
	\n5. Does %d recognise your face?
	\n6. Does %d reach out and grab objects already?
	\n7. Can %d sit up with support""" % (sex, sex, sex, sex, sex, sex)
elif month =="7" or month =="8" or month =="9":
	print """During the 6th to 9th month, the baby becomes a baby on the go! 
	After learning that %d can get somewhere by rolling over, %d\'ll spend the next few months figuring out how to move forward or backward. 
	\nQuestions to ask from the parents at this stage: 
	\n1. Is the baby sleeping at regular intervals?
	\n2. Can %d crawl already?
	\n3. Can %d sit without support? 
	\n4. Does %d react to his/her name?
	\n5. Say his/her first words?
	\n6. Can %d pull himself/herself up to standing position?""" % (sex, sex, sex, sex, sex, sex)
elif month =="10" or month =="11" or month =="12":
	print """The period before turning 1 year old is characterized by fast change. The baby becomes physically more coordinated and capable, 
	%d is also learning the first words. At this stage, for example, babies are normally able already to hold small objects such as O-shaped 
	cereal between their thumb and forefinger and start trying to eat by themselves.
	\nQuestions to ask from the parents at this stage: 
	\n1. Is %d showing his/her temper already? E.g. demanding things by pointing at them?
	\n2. Has %d done his/her first steps already? Or maybe cruise, or move around the room on his/her feet while holding onto the furniture?
	\n3. Is the baby copying others in his/her games already? E.g. playing being on the phone?
	\n4. Does %d react to his/her name?
	\n5. Say his/her first words?
	\n6. Can %d pull himself/herself up to standing position?""" % (sex, sex, sex, sex, sex)
else: 
	print "Ups, something went wrong... Please enter the baby's age in months (0 - for a newborn... 12 - for a one-year-old"


