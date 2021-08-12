import textwrap
string = input("")
width_max = int(input(""))
text = textwrap.wrap(string, width_max)
for num in range(len(text)):
    print(text[num])






