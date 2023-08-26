def  get_nato_phonetic_dict():
    with open('nato_phonetic_alphabet.csv') as nato_phonetic_file:
        lines = nato_phonetic_file.readlines()
        return { line.split(',')[0].strip():line.split(',')[1].strip()   for line in lines}



nato_phonetic_dict = get_nato_phonetic_dict()
name = input('Please input name')
print( [ nato_phonetic_dict[letter]  for letter in name.upper() ])
