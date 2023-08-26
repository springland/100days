import pandas as pd
import csv
import turtle


def  get_states_cord_dict():
    states_dict = {}
    rows = []
    with open('50_states.csv') as states_file:
        rows.extend(csv.reader(states_file))

        for row in rows[1:]:
            states_dict[row[0].lower()] = (int(row[1]) , int(row[2]))

    return  states_dict


def  main_game():
    screen = turtle.Screen()

    image = 'blank_states_img.gif'
    screen.addshape(image)
    turtle.shape(image)
    states_dict = get_states_cord_dict()
    count = 0
    total = len(states_dict)
    screen.title("State Game")
    while count < total :

        state_name = screen.textinput(f'{count}/{total} correct' , "Please input a state name").lower()

        if state_name in states_dict.keys():
            count = count+1
            name_turtle = turtle.Turtle()
            name_turtle.penup()
            (x , y) = states_dict[state_name]
            del states_dict[state_name]
            screen.title(f'{count}/{total} correct')
            name_turtle.setposition(x , y)
            name_turtle.write(state_name)

    screen.exitonclick()

main_game()