def reversetask(text):
    new=""
    v=len(text)
    while v>0:
        v-=1
        new+=text[v]
    return new
rev=input("I'm ready to get your input here: ")

print(reversetask(rev))