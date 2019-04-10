#!/usr/bin/env python3


#get english sentence from user
def get_sentence():
    
    english_sentence = input("{:12}".format("Enter text:  ")).strip()
    
    return english_sentence

#prepare english sentence for translation
def prepare_sentence(sentence):
    
    #replace all punctuation with spaces
    prepared_sentence = sentence.replace(".", "")
    prepared_sentence = prepared_sentence.replace("!", "")
    prepared_sentence = prepared_sentence.replace("?", "")    
    #make all characters lowercase
    prepared_sentence = prepared_sentence.lower()
    
    return prepared_sentence
    

#translate a word
def translate_word(word):
    
    #create list of vowels and a char variable from first letter of the word
    vowels = {'a', 'e', 'i', 'o', 'u'}
    char = word[0]
    
    #check to see if the first letter is a vowel and if so add way to it then return the word
    if char in vowels:
        word = word + "way"
        
        return word
    
    #if first letter not a vowel check to see if its a Y
    else:        
        if char == 'y':
            #if it is set the word equal to all the letters after the first one & add y to the end of it
            word = word[1:]
            word += "y"
            #reset the char variable to the new first letter
            char = word[0]
            #loop through the words letters until a vowel is hit
            while char not in vowels:
                #remove the first letter
                word = word[1:]
                #add the letter to the end of the word
                word += char
            #when a vowel is hit add ay to the end of the word and return it
            word = word + "ay"
            
            return word

        #if first letter not a y then add y to the list of vowels and reset char variable
        else:
            char = word[0]
            vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
            #loop through the words letters until a vowel is hit
            while char not in vowels:
                #remove the first letter
                word = word[1:]
                #add the letter to the end of the word
                word += char
                #reset char variable
                char = word[0]
            #when loop is finished add ay to the end and return the word    
            word = word + "ay"
            
            return word
    
#main function
def main():
    #print title
    print("Pig Latin Translator")
    print()

    #start main program loop
    choice = "y"
    while choice.lower() == "y":
        #prompt user for sentence to translate
        sentence = get_sentence()
        
        #prepare the sentence for translation
        prepared_sentence = prepare_sentence(sentence)
        
        #split prepared sentence into a list
        words1 = prepared_sentence.split()
        
        #start converting words and add to a new list
        words2 = []
        for item in words1:
            words2.append(translate_word(item))

        #add translated word list together to create a new string
        translated_sentence = " ".join(words2)

        #display the formatted results
        print("{:12} {:>15}".format("English: ", prepared_sentence))
        print("{:12} {:>15}".format("Pig Latin: ", translated_sentence))        
        print()

        #check to see if user wants to translate another sentence
        choice = input("Continue? (y/n): ")
        while (choice != "y" and choice != "n"):
            print("Please enter y or n")
            choice = input("Continue? (y/n): ")
        
        print()


if __name__ == "__main__":
    main()
