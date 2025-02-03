import script2
print(f"{__name__},script1") # returns a string "__main__"
def print_script1():
    print("This is function of script1")
def main():
    print("this is script1")

if __name__=="__main__":
    main()

# when imported the code outside any function gets executed
#therefore we use main function where all the code is written
#the __name__ helps to check if the script is run directly or not
#import runs the imported program and __name__ in that program returns the file name
#and when the __name__ of the main or running program executes it returns "__main__"
#thus by checking if __name__=="__main__": we run only the main program