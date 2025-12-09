#creating a quiz game
print ("Welcome to my quiz")

playing=input("hey bro wanna play game???")

if playing.lower() != "yes":
    quit()
    print("cool no issue")

print("okay ! come on lets play bro")
score=0

answer=input("what is the ic number of NAND?")
if answer=="7400":
    print("cool correct answer")
    score+=1
else:
    print("oops wrong ,its 7400")

answer=input("what is the ic number of AND?")
if answer=="7408":
    print("cool correct answer")
    score+=1
else:
    print("oops wrong ,its 7408")


answer=input("what is the ic number of XOR?")
if answer=="7486":
    print("cool correct answer")
    score+=1
else:
    print("oops wrong ,its 7486")


answer=input("what is the ic number of NOT?")
if answer=="7404":
    print("cool correct answer")
    score+=1
else:
    print("oops wrong ,its 7404")

print("you  got " + str(score) + " questions correct")

print ("THANKS FOR PLAYING!")




