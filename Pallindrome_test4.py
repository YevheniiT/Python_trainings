def main() :
   inputStr = input("Enter a string: ")
   if isPalindrome(inputStr) :
      print("That's a palindrome.")
   else:
      print("That isn't a palindrome.")


def isPalindrome(string) :
   if len(string) <= 1 :
      return True
   if string[0] == string[len(string) - 1] :
      return isPalindrome(string[1:len(string) - 1])
   else :
      return False


main()

