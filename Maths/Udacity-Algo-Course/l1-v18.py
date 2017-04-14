def rec_russian(x,y):
    if(x == 0):
        return 0
    if(x % 2 == 0):
        return 2*rec_russian(x/2, y)
    return y + 2*rec_russian((x-1)/2, y)
print(rec_russian(20,7))