"""
Example:

str1 = saim
str2 = asaimkhan
Result = str2 is a permutation of str1

str_long = basaimkhan
str_small = saim
Result = str2 is not a permutation of str1

"""

def permutation_check(str_long,str_small):
    for i in range(len(str_long)):
        if(str_small[0]==str_long[i]):
            match = 0
            for j in range(len(str_small)):
                if (str_long[i+j] == str_small[j]):
                    match = match+1
            if match == len(str_small):
                return "is a subset"

    return "not a subset"            

while True:
    str_small = raw_input("\nenter the small string \n")
    str_large = raw_input("enter the large string \n")
    got = permutation_check(str_large, str_small)  
    print(got)  
