import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    example_color = 1
    students_array = [1,2,3,4,5,6,7,8,9,10]
 
    #your loop here
    for i in range(len(students_array)):
        aleatorio=random.randint(0,4)
        print(get_color(aleatorio))         
    return i





print(get_allStudentColors())