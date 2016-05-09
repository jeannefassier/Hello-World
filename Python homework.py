"""
Spyder Editor

This is a temporary script file.
"""
   
 
list=['jeanne','pierrette','simone','lu','nan','bb','baobab','xx','xabc']
print(list)


def match_ends(words):
    count=0
    for i in words:
        if len(i)>2:
            if i[0]==i[len(i)-1]:
                count+=1
    return (count)
test=match_ends(list)
print(test)




def front_x(words):
    list_x=[]
    list_no_x=[]
    for i in words:
        if i[0]=='x':
            list_x.append(i)
        else:
            list_no_x.append(i)
        list_x.sort()
        list_no_x.sort()
        output=[list_x]
        output.append(list_no_x)
    return(list_x,list_no_x)
test_list = front_x(list)
print (test_list)


def sort_last(tuples):
    def getKey(item):
        return item[len(item)-1]
    return (sorted(tuple, key=getKey))
tuple=[(1,1),(1,2),(1,2,3),(2,3,8),(5,6)]
test_tuple = sort_last(tuple)
print (test_tuple)





def remove_adjacent(nums):
    out=[]
    for i in range(0,len(nums)):
        if nums[i]!=nums[i-1]:
            out.append(nums[i])  
    return(out)
nums=[1,2,2,5,6,6,6,6,7,88]
test_out=remove_adjacent(nums)
print(test_out)




def linear_merge(list1, list2):
    return(sorted(list1+list2))
test_merge=linear_merge(list1, list2)
print(test_merge)




def donuts(count):
    if count<10:
        print "Number of donuts: %d" %(count)
    else: print "Number of donuts: many !!!"
    return()
donuts(5)
donuts(15)

def both_ends(s):
   out=s[0]+s[1]+s[len(s)-2]+s[len(s)-1]
   return(out)
both_ends("spring") 


def fix_start(s):
    out=s[0]
    for i in range(1,len(s)):
        if s[i]==s[0]:
            out+="*"
        else:
            out+= s[i]
    return(out)
fix_start("bubble")




def mix_up(a, b):
    a2=b[0]+b[1]
    b2=a[0]+a[1]
    for i in range(2,len(a)):
        a2+=a[i]
    for j in range(2,len(b)):
        b2+=b[i]
    return (a2+" "+b2)
mix_up("mix","pod")



def verbing(s):
    if len(s)>=3:
        if s[len(s)-3]+s[len(s)-2]+s[len(s)-1]=="ing":
            out=s+"ly"
        else:
            out=s+"ing"
    else:
        out=s
    return(out)
verbing("according")
verbing("la")
verbing("verb")





def not_bad(s):
    if s.find("not")==-1 and s.find("bad")==-1:
        out=s
    else:
        for i in range(1,len(s)):
            if s[i:(i+3)]=="not":
                for j in range(i,len(s)):
                    if s[j:(j+3)]=="bad":
                        out=s[:(i-1)]+s[(i+4):(j-1)]+" good"+s[(j+4):]
    return(out)
s="Cette phrase est un test et cest not bad"
print(not_bad(s))


def front_back(s):
    l=len(s)
    if l%2==0:
        a=s[:l/2]
        b=s[l/2:]
    else:
        a=s[:(l+1)/2]
        b=s[(l+1)/2:]
    return(a,b)
s1="abcdef"
a1=front_back(s1)
print (a1)
