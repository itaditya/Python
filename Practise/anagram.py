# cook your code here
def anagram(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    j=0
    flag = False   #false indicates that anagrams
    while ( j < 26 and not flag) :
        if c1[j] != c2[j]:
            flag = True
        else :
            j += 1
    if(not flag):
        print("YES")
    else :
        print("NO")
    #print c1,c2,s1,s2
t=int(raw_input())
for i in range(t):
    a,b=raw_input().split()
    anagram(a,b)
# print a,b