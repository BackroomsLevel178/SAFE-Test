# quiz.py
aggressiveness = int(0)


answer = input('''You are approached by a frenzied scientist, who yells, "I'm going to put my quantum harmonizer in your photonic resonation chamber!" What's your response?\n1. I'd say "Up yours, too, buddy."\n2. I'd grab a pipe and knock him out.\n3. I'd slip away before he finishes.\n4. I wouldn't worry, if he did that it'd cause a parabolic destabilization of the fission singularity.''')
if answer == "1":
    aggressiveness = aggressiveness + 1
elif answer == "2":
    print(f"The answer is '1781', not {answer!r}")

answer = input("Which built-in function can get information from the user? ")
if answer == "input":
    print("Correct!")
else:
    print(f"The answer is 'input', not {answer!r}")