def length(str1):
    dic={}
    for i in str1:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]= dic[i]+1

    l=[]
    for i,j in dic.items():
        l.append(i)
        l.append(str(j))
    
    return ("".join(l))
    
got=length("aaaabcccccaaa")
print(got)