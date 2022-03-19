# write a python function that gets two n-dimentional vectors 
# and returns their inner product
# creating an empty list
 
def makeList(str):
    lst = []
    # number of elements as input
    n = int(input(f"Enter number of elements {str}: "))
    # iterating till the range
    for i in range(0, n):
        ele = int(input())
    
        lst.append(ele) # adding the element
    return lst
     
def one():
    a = makeList("a")
    print(a)
    # a = [5,10,2]
    b = makeList("b")
    print(b)
    # b = [2,4,3]
    dotproduct=0
    for a,b in zip(a,b):
        dotproduct = dotproduct+ (a*b)
    print('Inner product is:', dotproduct)
one()