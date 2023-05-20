import pandas

nato_data = pandas.read_csv("Day26/NATO-alphabet/nato_phonetic_alphabet.csv")
# print(nato_data)

nato_data_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}
# print(nato_data_dict)

name = input("Whats your string !!!\n").upper()

# result = [letter for letter in name]

result = [nato_data_dict[letter] for letter in name]

print(result)




