"""Input: "    Mr John Smith     "
Output: "Mr%20Dohn%20Smith"
"""

def fill_empty_space(str1):
    list1=[]
    for i in str1:
        list1.append(i)
    print(list1)

    for j in range(len(list1)):
        if (list1[j]==" "):
            list1[j]= "%20"
    print(list1)

    while True:
        if (list1[0]=="%20"):
            del list1[0]
        else:
            break

    while True:
        if (list1[-1]=="%20"):
            del list1[-1]
        else:
            break

    print("".join(list1))



fill_empty_space("     my name is     saim    ")

