import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
responses=["Hello","I AM A SMART CALCULATER","CAN I HELP YOU"]
def lcm(a,b=0):
    l = b if a>b else a
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1
def hcf(a,b=0):
    h= b if a>b else a
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1
def add(a,b=0):
    return a+b
def sub(a,b=0):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def Exit():
    speaker.Speak("Thank You")
    exit()
def wel():
    speaker.Speak("Your Welcome")
    exit()
def pow(a,b):
    return a**b
def name():
    speaker.Speak("My name is Smart Calculater")
def how():
    print("I am Fine")
introduction={"NAME":name,"WHO":name,"HOW":how}
operations = {"PLUS": add, "ADDITION": add, "ADD": add,"SUM":add ,"+": add, "MINUS": sub, "SUBSTRACTION": sub,"DIFFERENCE":sub,
                  "SUBSTRACT": sub, "-": sub, "MULTIPLY": mul, "MULTIPLECATION": mul, "*": mul, "DIVISION": div,
                  "DIVIDE": div, "/": div, "HCF": hcf, "LCM": lcm,"POWER":pow}
Exit_commonds = {"QUIT": Exit, "THANKS": wel, "EXIT": Exit,"OK":Exit}
print(responses[0],"\n",responses[1],"\n",responses[2])
while True:
   flag=0
   a=[]
   taxt=input("Enter What You Want to calculater to me").split(' ')
   for i in taxt:
    try:
        a.append(float(i))
    except:
        pass
   for word in taxt:
    if word.upper() in operations:
      try:
         print(operations[word.upper()](a[0],a[1]))
         break
      except:
          print("Sorry It is Beyond my ability\n Please try another another number")
          break
    elif word.upper() in Exit_commonds:
          Exit_commonds[word.upper()]()
          flag=1
          break
    elif word.upper() in introduction:
        introduction[word.upper()]()
        break
   else:
        print("So,Sorry \n Please Try Again")
   if flag==1:
       break
