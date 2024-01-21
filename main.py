# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt") as letter_file:
    template_letter = letter_file.read()
# print(template_letter)

with open("Input/Names/invited_names.txt") as names_file:
    names_list = names_file.read().split("\n")


for name in names_list:
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as req_file:
        req_file.write(template_letter.replace("[name]", f"{name}"))
