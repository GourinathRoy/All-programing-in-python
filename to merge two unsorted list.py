def Merge(list1,list2):
    final_list=list1+list2
    final_list.sort()
    return(final_list)
list1=[25,18,9,41,26,31]
list2=[25,45,3,32,15,20]
print(Merge(list1, list2))
