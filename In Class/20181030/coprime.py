
def main():

#     def getvalidNum(num_to_check) : 
#         nc = num_to_check.replace(".","")
#         while not num_to_check.isnumeric() : 
#             num_to_check = input("Not a number. Please try again")
#             nc = num_to_check(".","")
#         else : 
#             num_to_check = int(num_to_check)
#         return(num_to_check)

    n = 18
    for d in range(1,19) : 
        if n % d == 0 : 
            print(d)
                            
main()
