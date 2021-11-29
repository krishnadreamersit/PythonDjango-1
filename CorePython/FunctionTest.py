import MyFunctions # import module

# MyFunctions.f1()
# # passing value to function
# var1 = "Broadway"
# MyFunctions.f2(var1) # call f2 with passing value of var1
# MyFunctions.f2(None)
# MyFunctions.f2(True)
# var1 = False
# MyFunctions.f2(var1)
# MyFunctions.f2([1, 2.3, 45+6j, True, "KTM"])
# var1 = (1,2,3,4,5,6)# Stop point/Break point
# MyFunctions.f2(var1)

# note
# pass set, dictionary, and array
# argument - source
# parameter - destination


# f2_1(p1, p2)
# n1 = 45
# n2 = 67
# MyFunctions.f2_1(n1, n2)

# f2_1(p1, p2)
# n1 = float(input("Enter first value : ")) # always string -> convert to float
# n2 = float(input("Enter second value : ")) # always string -? convert to float

# tmp1 = input("Enter first value : ")
# tmp2 = input("Enter second value : ")
# print(isinstance(tmp1, float))
# print(isinstance(tmp2, float))
# n1 = float(tmp1)
# n2 = float(tmp2)
# MyFunctions.f2_1(n1, n2)

# result1 = MyFunctions.isInteger(tmp1)
# result2 = MyFunctions.isInteger(tmp2)
# if(result1 and result2):
#     # print("Can add")
#     sum = MyFunctions.f2_2(int(tmp1), int(tmp2))
#     print("Sum : ", sum)
# else:
#     print("cannt add")

tmp1 = input("Enter first value : ")
tmp2 = input("Enter second value : ")
result1 = MyFunctions.isInteger(tmp1)
result2 = MyFunctions.isInteger(tmp2)
if(result1 and result2):
    sum = MyFunctions.f2_2(int(tmp1), int(tmp2))
    print("Sum : ", sum)
else:
    print("cannt add")
