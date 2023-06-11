def destCity(paths):
    setdest = set()
    setstart = set()

    for start, des in paths:
        setdest.add(des)
        setstart.add(start)
    
    for des in setdest:
        if des not in setstart:
            return des
        

print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
