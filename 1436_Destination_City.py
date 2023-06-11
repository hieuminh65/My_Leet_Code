def destCity(paths):
    mapp = {}
    for p in paths:
        mapp[p[1]] = p[0]
    # print(mapp.keys())
    # print(paths[1][0] in mapp)
    for p in paths:
        print(p[1])
        if p[1] not in mapp:
            return p[1]
        

print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))