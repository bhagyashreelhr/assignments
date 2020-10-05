# Program to check if a string is palindrome or not

def isPalindrome(st):

    try:
        st=st.lower()
        st=list(st)
        flist=[]
        rev=None
        checklist=list("asdfghjklqwertyuiopzxcvbnm")
        for i in st:
            if i in checklist:
                flist.append(i)
                rev=flist[::-1]
        if((rev != None) and (rev==flist)):
            print("is palindrome")
        else:
            print("not palindrome")

    except TypeError:
        print("Invalid Input")

st=input("enter the sentence to check palindrome")
output=isPalindrome(st)

