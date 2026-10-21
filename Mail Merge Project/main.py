PLACEHOLDER_TEXT="[name]"
with open("./Input/Names/invited_names.txt") as name_file:
    names=name_file.readlines() #readlines is used to turn text into list

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        n_strip=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER_TEXT,n_strip)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{n_strip}.docx","w") as completed_letter:
            completed_letter.write(new_letter)