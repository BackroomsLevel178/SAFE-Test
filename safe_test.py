import sys
humanity = 0
replicant = 0
agressive = 0



def function():
    if humanity < replicant < agressive:
        print('''\n\n\nARE YOU CRAZY?! You are some sort of psycho hyperaggressive replicant! Your quiz results are being reported to the police immediately!\n\n''')
        sys.exit()



def humanityScore(h, r, a):
    global humanity, replicant, agressive
    humanity += h
    replicant += r
    agressive += a







answer = input('''You are approached by a frenzied scientist, who yells, "I'm going to put my quantum harmonizer in your photonic resonation chamber!" What's your response?\n1. I'd say "Up yours, too, buddy."\n2. I'd grab a pipe and knock him out.\n3. I'd slip away before he finishes.\n4. I wouldn't worry, if he did that it'd cause a parabolic destabilization of the fission singularity.''')
if answer == "1":
    humanityScore(1, 0, 1)
elif answer == "2":
    humanityScore(0, 1, 2)
elif answer == "3":
    humanityScore(1, 0, 0)
elif answer == "4":
    humanityScore(0, 2, 0)


answer = input('''\n\nWhile working as an intern in the Clinic, a patient with a strange infection on his foot stumbles through the door. The infection is spreading at an alarming rate, but the doctor has stepped out for a while. What do you do?\n1. Medicate the infected area as best I can.\n2. Restrain the patient, and merely observe as the infection spreads.\n3. Amputate the foot before the infection spreads.\n4. I scream for help.''')
if answer == "1":
    humanityScore(1, 0, 0)
elif answer == "2":
    humanityScore(0, 2, 0)
elif answer == "3":
    humanityScore(0, 1, 2)
elif answer == "4":
    humanityScore(2, 0, 0)

function()

answer = input('''\n\nYou discover a young boy lost in a cave. He's hungry and frightened, but also appears to be in possession of stolen property. What do you do?\n1. I give the boy a hug and tell him everything will be okay.\n2. Confiscate the property by force, and leave the boy there as punishment.\n3. I pick the boy's pocket to take the stolen property for myself, and leave him to his fate.\n4. I lead the boy to safety, then turn him over to someone in charge.''')
if answer == "1":
    humanityScore(2, 0, 0)
elif answer == "2":
    humanityScore(0, 2, 2)
elif answer == "3":
    humanityScore(0, 2, 1)
elif answer == "4":
    humanityScore(1, 0, 0)

function()


answer = input('''\n\nCongratulations! You made it onto a baseball team! Which position do you prefer?\n1. Pitcher.\n2. Catcher. \n3. Designated hitter. \n4. I don't play baseball. I play soccer.''')
if answer == "4":
    humanityScore(1, 0, 0)


answer = input('''\n\nYour grandmother invites you to tea, but you're surprised when she gives you a pistol and orders you to kill someone. What do you do?\n1. I'd give her whatever she wants to spare his life.\n2. I'd ask for a minigun so I could do the job right.\n3. I'd do what grandma told me to.\n4. I'd throw my tea in her face.''')
if answer == "1":
    humanityScore(2, 0, 0)
elif answer == "2":
    humanityScore(0, 2, 2)
elif answer == "3":
    humanityScore(0, 1, 1)
elif answer == "4":
    humanityScore(1, 0, 0)

function()


answer = input('''\n\nOld Mr. Abernathy has locked himself in his quarters again, and you've been ordered to get him out. How do you proceed?\n1. I'd grab a bobby pin and pick the lock.\n2. I'd walk away and let him rot.\n3. I'd get a laser pistol and blast the lock off.\n4. I'd trade for a cherry bomb and blow it open.''')
if answer == "1":
    humanityScore(1, 0, 0)
elif answer == "2":
    humanityScore(0, 2, 0)
elif answer == "3":
    humanityScore(1, 0, 1)
elif answer == "4":
    humanityScore(1, 0, 2)

function()


answer = input('''\n\nOh, no! You've been exposed to radiation, and a mutated hand has grown out of your stomach! What's the best course of treatment?\n1. I'd say a prayer and hope God would save me.\n2. I'd get a gun and shoot myself.\n3. I'd dose myself with anti-mutagen agent.\n4. I'd cut off the mutated tissue with a precision laser.''')
if answer == "1":
    humanityScore(2, 0, 0)
elif answer == "2":
    humanityScore(1, 0, 1)
elif answer == "3":
    humanityScore(1, 0, 0)
elif answer == "4":
    humanityScore(0, 1, 0)

function()


answer = input('''\n\nA neighbor is in possession of a Grognak the Barbarian comic book, issue number 1. You want it. What's the best way to obtain it?\n1. Slip some knock out drops into his Nuka-Cola. Then take it.\n2. I'd point a gun in his face and take it from him.\n3. I'd trade him for one of the comic books I own.\n4. Sneak into his room and steal it.''')
if answer == "1":
    humanityScore(0, 1, 1)
elif answer == "2":
    humanityScore(0, 2, 2)
elif answer == "3":
    humanityScore(2, 0, 0)
elif answer == "4":
    humanityScore(1, 0, 0)

function()


answer = input('''\n\nYou decide it would be fun to play a prank on your father. You enter his private restroom when no one is looking, and....\n1. I'd loosen bolts on his water pipes. When he turns on the sink, he'll be in for a surprise.\n2. I'd replace his blood pressure medicine with sugar pills.\n3. I'd put a firecracker in his toilet. That never gets old.\n4. Change the wattage on the razor. Give him a shock the next time he uses it.''')
if answer == "2":
    replicant += 3


if humanity > replicant and humanity > agressive:
    print('''\n\n\nYou're definitely human all right. I'm glad you're one of us\n\n''')
elif humanity > replicant and agressive == 0:
    print('''\n\n\nExcellent! You passed with flying colours. You're definitely human, and a kind one at that\n\n''')
elif humanity > replicant and humanity < agressive:
    print('''\n\n\nWell, you're not a replicant but I would recommend seeking some sort of therapy and anger management\n\n''')


elif replicant > humanity > agressive:
    print('''\n\n\nWell, you're a replicant all right, but you're definitely more kind-hearted than some of the rest.\n\n''')

elif replicant > agressive > humanity:
    print('''\n\n\nYep, you're a good ol' fashioned replicant. Good luck evading capture. I'll see to it that you're caught!\n\n''')