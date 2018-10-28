
def main():

    # Define function of redaction 
    def input_letter(P_Phrase):
        list_letter = []
        letter = input("\nType a comma-seperated list of letters to redact: ")
        list_letter.extend(letter)
        
        total_num = 0 
        for c, l in enumerate(list_letter) :
            num_letters = P_Phrase.count(l)
            total_num = total_num + num_letters # To calculate number of letters redacted
            P_Phrase = P_Phrase.replace(l, '_') # Replace redacted letter to "_" 

        print(f"Number of letters redacted : {total_num}" )
        print(f"Redacted phrase : {P_Phrase} \n")

    # loop 
    i = 0
    while i == 0 : 
        phrase = input("Type a phrase (or quit to exit program): ")
        phrase = phrase.lower()
        if not phrase == "quit" :
            input_letter(phrase)    
        else : 
            print("The End")
            i = i + 1

main()
