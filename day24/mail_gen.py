
def   get_names():

    names = []
    with open('guests.txt') as file:
        names =  file.readlines()

    return names


def get_letter_template():
    with open('letter_template.txt') as file:
        lines= file.readlines()
        return "".join(lines)

def  generate_letters():
    names = get_names()
    template = get_letter_template()

    for name in names:
        name = name.strip()
        letter = template
        letter = letter.replace("[Name]" , name)
        with open(f"letter_{name}.txt" , "w") as file:
            file.write(letter)

generate_letters()