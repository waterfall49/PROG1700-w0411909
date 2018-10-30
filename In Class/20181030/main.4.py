
def main():

    maybe_num = "a"
    while not maybe_num.isnumeric() :
        maybe_num = input("Enter a number: ") 
        if not maybe_num.isnumeric():
            print("No good. Not a number")
    else : 
        num = int(maybe_num)
        print(f"This is num! {num}")
            
main()
