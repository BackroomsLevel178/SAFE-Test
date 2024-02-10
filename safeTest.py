# quiz.py
aggressiveness = int(0)
humanity = int(0)
replicant = int(0)


answer = input('''You are approached by a frenzied scientist, who yells, "I'm going to put my quantum harmonizer in your photonic resonation chamber!" What's your response?\n1. I'd say "Up yours, too, buddy."\n2. I'd grab a pipe and knock him out.\n3. I'd slip away before he finishes.\n4. I wouldn't worry, if he did that it'd cause a parabolic destabilization of the fission singularity.''')
if answer == "1":
    aggressiveness = aggressiveness + 1
    humanity = humanity + 1
elif answer == "2":
    aggressiveness = aggressiveness + 2
    replicant = replicant + 1
elif answer == "3":
    humanity = humanity + 1
elif answer == "4":
    replicant = replicant + 2


answer = input('''While working as an intern in the Clinic, a patient with a strange infection on his foot stumbles through the door. The infection is spreading at an alarming rate, but the doctor has stepped out for a while. What do you do?\n1. Medicate the infected area as best I can.\n2. Restrain the patient, and merely observe as the infection spreads.\n3. Amputate the foot before the infection spreads.\n4. I scream for help.''')
if answer == "1":
    humanity = humanity + 1
elif answer == "2":
    replicant = replicant + 2
elif answer == "3":
    aggressiveness = aggressiveness + 2
    replicant = replicant + 1
elif answer == "4":
    humanity = humanity + 2


answer = input('''You discover a young boy lost in a cave. He's hungry and frightened, but also appears to be in possession of stolen property. What do you do?\n1. I give the boy a hug and tell him everything will be okay.\n2. Confiscate the property by force, and leave the boy there as punishment.\n3. I pick the boy's pocket to take the stolen property for myself, and leave him to his fate.\n4. I lead the boy to safety, then turn him over to someone in charge.''')
if answer == "1":
    humanity = humanity + 2
elif answer == "2":
    replicant = replicant + 2
    aggressiveness = aggressiveness + 2
elif answer == "3":
    aggressiveness = aggressiveness + 1.5
    replicant = replicant + 2
elif answer == "4":
    humanity = humanity + 1


answer = input('''Congratulations! You made it onto a baseball team! Which position do you prefer?\n1. Pitcher.\n2. Catcher. \n3. Designated hitter. \n4. I don't play baseball. I play soccer.''')
if answer == "4":
    humanity = humanity + 1


answer = input('''Your grandmother invites you to tea, but you're surprised when she gives you a pistol and orders you to kill someone. What do you do?\n1. I'd give her whatever she wants to spare his life.\n2. I'd ask for a minigun so I could do the job right.\n3. I'd do what grandma told me to.\n4. I'd throw my tea in her face.''')
if answer == "1":
    humanity = humanity + 2
elif answer == "2":
    replicant = replicant + 2
    aggressiveness = aggressiveness + 2
elif answer == "3":
    aggressiveness = aggressiveness + 1
    replicant = replicant + 1
elif answer == "4":
    humanity = humanity + 1