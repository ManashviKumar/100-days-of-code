import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data=pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict=data.to_dict()
p_dict={row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic():
    word=input("enter word: ").upper()
    try:
        output_list=[p_dict[letter] for letter in word]
    except KeyError:
        print("Enter letters only")
        phonetic()
    else:
        print(output_list)
phonetic()
