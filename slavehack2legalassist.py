from builtins import any as any1

ts = 1

#012345678
#Action: Delete All

def newline():
    print("\n--------------------------------------------\n")

#list maker
def list_maker():
    list1 = []
    Penis = True
    while(Penis):
        data = input("data:")
        list1.append(data)
        if(data[0:3] == "Rep"):
            Penis = False

    return(list1)



#removes fluff and spits out usable numbers and letters.
#input = str()
def extraction_single(input):
    str(input)
    leng = len(input)
    position = input.find(":")
    position = position + 2
    final = input[position:leng]
    return(final)


#removes fluff and spits out usable numbers and letters.
#input = lst()
def extraction_full(input):
    position = 0
    leng = len(input)
    newlist = []
    while(position != leng):
        newlist.append(extraction_single(input[position]))
        position = position + 1
    return(newlist)



#detects type of mission and spits out the type as an integer.
#input = lst()
def type_detect(input):
    #tests which position action: is in
    Dick = input[0]
    test = 1
    if(Dick[0:6] == "action:" ):
        test = 0
    action = input[test]
    action = extraction_single(action)
    if(action == "Delete One"):
        type = 1
    elif(action == "Delete All"):
        type = 2
    elif(action == "Transfer File"):
        type = 3
    elif(action == "DDoS"):
        type = 4
    elif(action == "Steal Money"):
        type = 5
    elif(action == "Frame"):
        type = 6
    else:
        type = 7

    return(type)




#Delete One      type = 1
def delete_one(something):
    list = extraction_full(something)
    target = list[0]
    file = list[2]
    connection = "connect " + target
    delete =  "rm " + file
    print("\n--------------------------------------------\n")
    print(connection)
    print("\n--------------------------------------------\n")
    print(delete)
    print("\n--------------------------------------------\n")


#Delete All      type = 2
def delete_all(something):
    list = extraction_full(something)
    target = list[0]
    files = []
    leng = len(something)
    leng2 = leng - 3
    newlist = something[3:leng2]
    leng3 = len(newlist)
    counter = 0 
    delete = "rm "
    print("connect " + target)
    print("\n--------------------------------------------\n")
    while(counter != leng3):
        print(delete + newlist[counter])
        print("\n--------------------------------------------\n")
        counter = counter + 1


#Transfer File   type = 3
def transfer_file(something):
    list = extraction_full(something)
    target = list[0]
    destination = input("For transfer missions please type the ip of the employer:")
    file = list[2]
    newline()
    print("connect " + target)
    newline()
    print("download " + file)
    newline()
    print("connect " + destination)
    newline()
    print("upload " + file)


#DDoS            type = 4
def ddos(something):
    list = extraction_full(something)
    target = list[0]
    leng = len(something)
    leng2 = leng - 2
    newlist = something[3:leng2]
    leng3 = len(newlist)
    #slave printer
    while(counter != leng3):
        print("connect " + newlist[counter])
        newline()
        print("ul 1.ddos")
        newline()
        print("install 1.ddos")
        newline()
        print("bye")
        newline()
        counter = counter + 1
    print("ddos " + target)


#Steal Money     type = 5
def steal_money(something):
    list = extraction_full(something)
    bankip = list[2]
    account = list[3]
    newline()
    print("drill " + account + " " + bankip)
    newline()
    print("connect "  + bankip)
    print("account login " + account)
    print("account balance")
    print("account transfer " + yourbank + " " + yourbank2 + " ")


#Frame           type = 6
def frame(something):
    list = extraction_full(something)
    target = list[0]
    newline()
    type2 = input("please type authentication, withdrawl, ddos, spyware, ransom, bounce, or rce. for your mission type :>")
    newline()
    leng = len(something)
    leng2 = leng - 3
    newlist = something[4:leng2]
    leng3 = len(newlist)
    phrase1 = ""
    phrase2 = ""
    if(type2 == "withdrawl"):
        phrase1 = "addlog -type='withdrawal' -ip='"
        phrase2 = "' -entry='mission' -level='success'"
    elif(type2 == "authentication"):
        phrase1 = "addlog -type='authentication' -ip='"
        phrase2 = "' -entry='missions' -level='success'"
    elif(type2 == "ddos"):
        phrase1 = "addlog -type='ddos' -ip='"
        phrase2 = "' -entry='mission' -level='danger'"
    elif(type2 == "spyware"):
        phrase1 = "addlog -type='spyware' -ip='"
        phrase2 = "' -entry='mission' -level='info'"
    elif(type2 == "ransom"):
        phrase1 = "addlog -type='ransom' -ip='"
        phrase2 = "' -entry='mission' -level='danger'"
    elif(type2 == "bounce"):
        phrase1 = "addlog -type='bounce' -ip='"
        phrase2 = "' -entry='mission' -level='success'"
    elif(type2 == "rce"):
        phrase1 = "addlog -type='rce' -ip='"
        phrase2 = "' -entry='mission' -level='warning'"
    else:
        print("error typo")
        done = False

    counter =  0


    while(counter != leng3):
        newline()
        print("connect " + newlist[counter])
        newline()
        print(phrase1 + target + phrase2)
        print("bye")
        counter = counter + 1
    
    





#your banking info reciever for bank missions
print("this information is for banking missions input and will not leave your irl computer.\n but if you still do not trust me just use a throw away acct")
newline()
yourbank = input("please type your bank ip :>")
newline()
yourbank2 = input("please type your bank acct# :>")
newline()
#int main
while(True):
    done = True
    nothing = input("Press any key to continue:")
    print("\n--------------------------------------------\n--------------------------------------------\n")
    while(done == True):
        print("mission start\n--------------------------------------------\n")
        main = list_maker()
        type = type_detect(main)
        if(type == 1):
            delete_one(main)
        elif(type == 2):
            delete_all(main)
        elif(type == 3):
            transfer_file(main)
        elif(type == 4):
            ddos(main)
        elif(type == 5):
            steal_money(main)
        elif(type == 6):
            frame(main)
        else:
            print("error")
        done = False