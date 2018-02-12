def remove_dupes(list1, list2):
    #list1 -> list of all elements
    #list2 -> list of elements that will be removed
    for item in list1:
        if item in list2:
            list1.remove(item)
    
    return list1
    
def find_dupes(list):
    seen=[]
    dupes=[]
    for item in list:
        if item not in seen:
            seen.append(item)
        elif item in seen and item not in dupes:
            dupes.append(item)
        else:
            pass
    print("duplicates ->", dupes)
    print("singletons ->", remove_dupes(seen, dupes))

find_dupes([1,2,3,3,3,4,5,6,6,7,6,9,9,8,9])