def coun(rep1):
    print(rep1)
    list1=[]
    for i in rep1:
        list1.append(i)
    print(list1)
    list1.sort()
    print(list1)
    list2 =[]
    for i in range(len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])
    print(list2)
    list3 = []
    if list2[1] in rep1:
        cou = rep1.count(list1[1])
        print(f"{list1[1]}\t{cou}")



str = input("enter:")
str1 = str.lower()
rep=""
if '"' in str1:
    rep = str1.replace('"',"")
    rep1 = rep.replace(" ","")
    coun(rep1)
