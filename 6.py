contact_lists = []
name = input("enter your name :")

father_name = input(f"enter {name}'s father's name :")

mother_name = input(f"enter {name}'s mother's name :")

number = input(f"enter {name}'s mobile number :")

contact_lists.append(name)
contact_lists.append(father_name)
contact_lists.append(mother_name)
contact_lists.append(number)
_list = "".join(contact_lists)
total_length = len(_list)

vowel_count = 0

vowel_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for i in _list:
    if i in vowel_list:
        vowel_count += 1

print("Number of Character: " + str(total_length))
print("Number of Vowel: " + str(vowel_count))
