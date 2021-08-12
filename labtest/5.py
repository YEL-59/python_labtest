number_input = input()
tofa = number_input.split(" ")


out = []
def tofayel(tofa):
    for i in range(len(tofa)):
        if int(tofa[i]) < 100:
            if int(tofa[i]) % 5 == 0 or int(tofa[i]) % 8 == 0:
                out.append(int(tofa[i]))

    print(out)

tofayel(tofa)