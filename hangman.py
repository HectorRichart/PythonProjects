import random

HANGMANPICS = ['''
+---+
| |
|
|
|
|
=========''', '''
+---+
| |
O |
|
|
|
=========''', '''
+---+
| |
O |
| |
|
|
=========''', '''
+---+
| |
O |
/| |
|
|
=========''', '''
+---+
| |
O |
/|\ |
|
|
=========''', '''
+---+
| |
O |
/|\ |
/ |
|
=========''', '''
+---+
| |
O |
/|\ |
/ \ |
|
=========''']

print("JUEGO DEL SUICIDIO")
print(HANGMANPICS[0])

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
'coyote crow deer dog donkey duck eagle ferret fox frog goat '
'goose hawk lion lizard llama mole monkey moose mouse mule newt '
'otter owl panda parrot pigeon python rabbit ram rat raven '
'rhino salmon seal shark sheep skunk sloth snake spider '
'stork swan tiger toad trout turkey turtle weasel whale wolf '
'wombat zebra ').split()

computer = random.choice(words)
converted = list(computer)
count = 0

for i in range(len(converted)):
    converted[i]="_"

print(converted)
while count <= 6:
    user = input("Enter a letter\n")
if user not in computer:
    count+=1
else:
    for i in range(len(computer)):
        if computer[i] == user:
            converted[i] = user
if "_" not in converted:
    count = 8
if count < 7:
    print(HANGMANPICS[count])
else:
    print("\nWord was:", computer)
print(converted)
if count == 8:
    print("You won a kiss from Ulises Escalante!!")
else:
    print("You won a beatover by IT department!!")