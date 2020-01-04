#width
m = 5
#depth
n = 4

EVENS_SET = set()

def main():
    pass

def mainRec(inPath=[]):
    if len(inPath) == n:
        return
    for t in getOptions(path):
        mainRec(inPath[:] + [t])

#Get applicable evens for path
#see if any path + tails would be even (Add to evens)
#return any that would be odd
def getOptions(path=[]):
    #all paths for now
    if len(path) == 0:
        return range(1,m+1)
    return range(1,path[-1]+1)


if __name__ == "__main__":
    main()
