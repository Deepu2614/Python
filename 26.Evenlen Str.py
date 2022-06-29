n=input("Enter a String:")
s=n.split(" ")
for i in s:
    #checking the length of words
    if len(i)%2==0:
        print(i)
print("\n\n By Deepak")