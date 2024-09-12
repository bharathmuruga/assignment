def check_Palindrome(word):
    words=word.lower()
    if words==words[::-1]:
        print(f"{word} palindrome word")
    else:
        print(f"{word} not Palindrome word")

word=input("enter the word: ")
check_Palindrome(word)
