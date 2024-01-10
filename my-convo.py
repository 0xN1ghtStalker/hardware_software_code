def conversation():
    print("Do you like coding in Python? Answer yes or no.")
    answer = input()
    if answer == "yes":
        print("That's good - the United States needs more coders!!")
    else:
        print("perhaps you will change your mind")
        print("goodbye")

def main() :
            print("Welcome to my conversation program")
            conversation()
            print("thanks for chatting with me")

if __name__ == "__main__":
    main()