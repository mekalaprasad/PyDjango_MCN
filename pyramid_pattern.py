# METHOD -1

# def pypattern(n):

#     for i in range(0, n):

#         for j in range(0, i+1):

#             print("*", end="")

#         print("\r")
# n= 5
# pypattern(n) 

#METHOD -2
def pypart(n):
    
    list = []
    for i in range(1, n+1):
        list.append("*"*i)
    print("\n".join(list))

n = 10
pypart(n)