def isisomorphic(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        map1,map2={},{}
        for i in range(len(s1)):
            ch1,ch2=s1[i],s2[i]
            if ch1 not in map1:
                map1[ch1]=ch2
            if ch2 not in map2:
                map2[ch2]=ch1
            if map1[ch1]!=ch2 or map2[ch2]!=ch1:
                return False
    return False
s1=input("Enter string s:")
s2=input("Enter string t:")
print(isisomorphic(s1,s2))
