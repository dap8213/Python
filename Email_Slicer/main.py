userInput = input("Please Enter Your Email:")


indexNum = int(userInput.index("@"))
userName = userInput[:indexNum]
domain = userInput[indexNum:]
domainStrip = domain.strip("@")
print("Your user name is:" + userName)
print("Your domain is:"+ domainStrip)



#slice_object = slice(1, -1, 1)

