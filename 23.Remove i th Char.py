test_str =input("Enter String:")
print ("The original string is : " + test_str)
new_str = test_str.replace('e', '')
print ("The string after removal of i'th character( doesn't work) : " + new_str)
new_str = test_str.replace('s', '', 1)
print ("The string after removal of i'th character(works) : " + new_str)

print("\n\n By Deepak")
