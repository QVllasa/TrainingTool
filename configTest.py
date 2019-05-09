

with open('config.txt', 'r') as file:
    s = 0
    x = int
    b = int
    y = int
    c = int
    lines = file.readlines()
    for i in lines:
        if 'trainer' in i: x = lines.index(i)
        if len(i.strip())==0: b = lines.index(i)
        if 'location' in i: y = lines.index(i)



    for j in lines[x+1:b]:
        print(j.strip())
    print(b)
    for j in lines[y+1:]:
        print(j.strip())


        # # if 'trainer' in i:
        # for j in lines[lines.index(i) + 1:lines.index(i.startswith('location'))]:
        #     print(j)
