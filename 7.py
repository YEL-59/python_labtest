_list = []

for _ in range(20, 60):
    if _ % 2 == 0:
        _ = _ + 5
        _list.append(_)


    elif _ % 5 == 0:
        _ = _ + 2
        _list.append(_)



print(_list)
