def mergestring(s1, s2):
    seq=[]
    for i in range(0, len(s1)+len(s2)):
        if i < len(s1):
            seq.append(s1[i])
        if i < len(s2):
            seq.append(s2[i])
    newstring=''.join(seq)
    return newstring

def main():
    s1=input("Enter string 1: ")
    s2=input("Enter string 2: ")
    print(mergestring(s1, s2))

main()