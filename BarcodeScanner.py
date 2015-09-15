def ISBN10(Bar):
    print("ISBN10")
    Count = 10
    Tot = 0
    list1 = []
    BarC = str(Bar)
    for i in BarC:
        list1.append(i)
    for i in list1:
        A = int(i)
        Tot += (A*Count)
        Count -= 1
    Ele = Tot%11
    if Ele != 0:
        print("Not a valid ISBN10 Barcode")
    else:
        print("Valid Barcode Entered!")
    return None

def ISBN13(Bar):
    print("ISBN13")
    Count = 1
    Tot = 0
    list1 = []
    BarC = str(Bar)
    for i in BarC:
        list1.append(i)
    for i in list1:
        A = int(i)
        Tot+= (int(i)*Count)
        print(Tot)
        if Count ==1:
            Count = 3
            print(Count)
        else:
            Count = 1
            print(Count)
    A = Tot%10
    if A != 0:
        print("Not a valid ISBN13 Barcode")
    else:
        print("Valid Barcode Entered!")
    return None

def UPC(Bar):
    print("UPC")
    Count = 1
    Tot = 0
    Tot2 = 0
    list1 = []
    BarC = str(Bar)
    for i in BarC:
        list1.append(i)
    for i in list1:
        A = int(i)
        if Count ==1:
            Count = 3
            Tot+= int(i)
            print(i)
            #print(Count)
        else:
            Count = 1
            Tot2 += int(i)
            #print(Count)
    Tot = Tot*3
    Tot = Tot+Tot2
    A = Tot%10
    if A != 0:
        print("Not a valid UPC Barcode")
    else:
        print("Valid Barcode Entered!")
    return None

def Chooser():
    while True:
        Choice = input("Barcode = UPC, ISBN-10 or ISBN-13? (U,10,13) ")
        if Choice == "U":
            UPC(input("Enter Barcode "))
        elif Choice == "10":
            ISBN10(input("Enter Barcode "))
        elif Choice == "13":
            ISBN13(input("Enter Barcode "))
        else:
            print("Not one of the options! ")

Chooser()
