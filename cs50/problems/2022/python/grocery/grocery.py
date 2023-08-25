groc = {}
while True:
    try:
        item = input().upper()
        if item in groc:
            groc[item] += 1
        else:
            groc.update({item: 1})

    except EOFError:
        print()
        for g in sorted(groc):
            print(f"{groc[g]} {g}")
        exit()
    else:
        pass
