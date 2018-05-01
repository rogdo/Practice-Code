#setup.py
import random  ## import the random number module
malady=("Blind", "Crippled", "Deaf", "Drunk", "Cramps", "Migraine", "Diabetic", \
        "Nauseous", "Arrhythmia", "Scraped", "Incontinent", "Achey", "Ruptured", \
        "Acid Reflux", "Epileptic", "Bursitis", "Erectile Dysfunctional", \
        "Attention Deficient", "Hyperactive", "Hypoglycemic", "Adrenal Insufficient",  "Freckled", "Agoraphobic",\
        "Albino", "Alcoholic", "Intoxicated", "Allergic", "Anal Fissure", "Glaucoma", \
        "Swollen", "Anorexic", "Anthrax", "Bipolar", "Schizophrenic") ## A bluesman's first name is a malady
fruit=("Melon", "Lemon", "Lime", "Grapefruit", "Apple", "Apricot", "Avocado", \
       "Banana", "Blackberry", "Blueberry", "Boysenberry", "Cherry", "Cranberry", \
       "Dragonfruit", "Gooseberry", "Grape", "Guava", "Huckleberry", "Jabuticaba", \
       "Kumquat", "Mango", "Nectarine", "Orange", "Papaya", "Peach", "Passion Fruit", \
       "Pear", "Persimmon", "Plantain", "Plum", "Pineapple", "Pomegranate", "Mangosteen", \
       "Raspberry", "Strawberry") ## A bluesman's middle name is a fruit
president=("Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Van Buren", "Harrison", \
           "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", \
           "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "Cleveland", \
           "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", \
           "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", \
           "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump") ## A bluesman's last name is a president's last name
random1 = random.randint(0,33) ## creating three random numbers to be used to create a unique name each time
random2 = random.randint(0,34) ## the first element in an array is element 0, so using 0 - 3 for random integers
random3 = random.randint(0,44)
print("Your blues name is: ", malady[random1], fruit[random2], president[random3])  # output the name
