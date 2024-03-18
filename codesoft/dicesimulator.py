import random

print("\u25CF,\u250C,\u2500,\u2510,\u2502,\u2518")   ####   ● ┌ ─ ┐ │ └ ┘

#simply copy the ascii art 

# Note:
# die-single 
# dice-plural

dice_art={

1: ("┌─────────┐ ",
    "│         │ ",
    "│    ●    │ ",
    "│         │ ",
    "└─────────┘ "),
2: ("┌─────────┐ ",
    "│ ●       │ ",
    "│         │ ",
    "│        ●│ ",
    "└─────────┘ "),
3: ("┌─────────┐ ",
    "│ ●       │ ",
    "│    ●    │ ",
    "│       ● │ ",
    "└─────────┘ "),
4: ("┌─────────┐ ",
    "│ ●     ● │ ",
    "│         │ ",
    "│ ●     ● │ ",
    "└─────────┘ "),
5: ("┌─────────┐ ",
    "│ ●     ● │ ",
    "│    ●    │ ",
    "│ ●     ● │ ",
    "└─────────┘ "),

6: ("┌─────────┐ ",
    "│ ●     ● │ ",
    "│ ●     ● │ ",
    "│ ●     ● │ ",
    "└─────────┘ "),
}

dice_values=[]
total=0

no_of_dice=int(input("enter the number of dice :"))


for die in range(no_of_dice):
    dice_values.append(random.randint(1,6))

for values in dice_values:

    for i in dice_art[values]: 
        print(i)

for values in dice_values:
    total+=values


print("total score is :",total)

    
    
    



