import random

def generate_question(arr):
    name = arr[0]
    date = arr[1]
    creator = arr[2]
    location = arr[3]
    product = arr[4]
    image = arr[5]

    opt = random.randint(0, 2)

    if opt == 0:
        question = "Who created this item? "
        return question, creator, image
    elif opt == 1: 
        question = "Where was this item invented? "
        return question, location, image
    else:
        question = "When was this item invented? "
        return question, date, image
        
    
    

    
    
