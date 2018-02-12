def set_union(list1, list2):
    union=[]
    for item in list1:
        union.append(item)
    for item in list2:
        union.append(item)
    union.sort()
    return union

print(set_union([2,1,3],[6,5,4]))

def list_zipper(list1, list2):
    #assumes list1 and list2 are of equal length 
    ziplist=[]
    for i in range(0,len(list1)):
        ziplist.append(list1[i])
        ziplist.append(list2[i])
    return ziplist
        
print(list_zipper([2,1,3],[6,5,4]))
    
def list_unpack(list1):
    names=[]
    ids=[]
    for name, id_no, level in list1:
        names.append(name)
        ids.append(id_no)
    return names, ids

print(list_unpack([["Mike", 10122, "A"], ["Ken", 10331, "B"], ["Jack", 10221, "C"]]))