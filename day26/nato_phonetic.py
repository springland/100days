import pandas as pd

def  get_nato_phonetic_dict():
    with open('nato_phonetic_alphabet.csv') as nato_phonetic_file:
        lines = nato_phonetic_file.readlines()
        return { line.split(',')[0].strip():line.split(',')[1].strip()   for line in lines}


def  get_nato_phoetic_df():
    return pd.read_csv('nato_phonetic_alphabet.csv').set_index('letter')

name = input('Please input name')
#nato_phonetic_dict = get_nato_phonetic_dict()
#
#print( [ nato_phonetic_dict[letter]  for letter in name.upper() ])

nato_phoetic_df = get_nato_phoetic_df()
#print(nato_phoetic_df)

print([ nato_phoetic_df.loc[letter, 'code'] for letter in name.upper()])