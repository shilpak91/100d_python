# TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/Users/shilpak/Documents/Code100/100d_python/Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as f:
    names = f.readlines()
    new_names = []
    for name in names:
        new_names.append(name.replace("\n",""))
    
with open ("/Users/shilpak/Documents/Code100/100d_python/Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as l:
    letter_txt = l.read()
    for name in new_names:
        new_letter = letter_txt.replace("[name]",f"{name}")
        with open(f"/Users/shilpak/Documents/Code100/100d_python/Day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt",mode="w") as fl:
            fl.write(new_letter)