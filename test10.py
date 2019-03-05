def char_freq(l):
    d={}
    for i in (range(len(l))):
        if (l[i] in d):
            d[l[i]]=int(d.get(l[i]))+1
        else:
            d[l[i]]=1
    return d
nt=input("Enter any String:")
n=char_freq(nt)

print(n)