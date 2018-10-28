
def main():

    def input_letter(a):
        list_letter = []
        letter = input("Type a comma-seperated list of letters to redact: ")
        list_letter.append(letter)
        #num for elem in list_letter for num in elem
        for c, l in enumerate(list_letter) :
            print(c,l)
            total_num = 0 
            num_letters = a.count(l)
            total_num = total_num + num_letters 
        print(num_letters)

    phrase = input("Type a phrase (or quit to exit program): ")
    input_letter(phrase)    

        

    # input
    # while
    #     phrase = input("Type a phrase (or quit to exit program): ")
            


    # process
 

    # output    

main()
