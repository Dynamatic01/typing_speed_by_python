from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(min(len(partest),len(usertest))):
        if partest[i] != usertest[i]:
            error +=1
       
    return error
          
def speed_time(time_s,time_e,userinput):
    time_delay= time_e -time_s
    time_R=round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)





test= ["The quick brown fox jumps over the lazy dog. This classic sentence contains every letter of the alphabet, making it perfect for testing typing speed and accuracy. With practice, you can improve your typing skills and type this sentence with lightning speed!",
       "My name is moooooooooooo"]
test1=r.choice(test)
print("*****Typing Speed**********")
print(test1)
print()
print()
time_1 = time()
testinput=input("enter :")
time_2 = time()

print("Speed:", speed_time(time_1,time_2,testinput),"Word/sec")
print("error", mistake(test1, testinput))