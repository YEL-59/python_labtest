command = int(input())
max = []
command_num = 0
while command_num < command:

    print(command_num)
    com = input("")
    com_out = com.split(" ")
    if com_out[0] == "insert":
        max.insert(int(com_out[1]), int(com_out[2]))
        command_num += 1
    elif com_out[0] == "print":
        print(max)
        command_num += 1
    elif com_out[0] == 'remove':
        max.remove(int(com_out[1]))
        command_num += 1
    elif com_out[0] == "append":
        max.append(int(com_out[1]))
        command_num += 1
    elif com_out[0] == 'sort':
        max.sort()
        command_num += 1
    elif com_out[0] == "pop":
        max.pop()
        command_num += 1
    elif com_out[0] == "reverse":
        max.reverse()
        command_num += 1