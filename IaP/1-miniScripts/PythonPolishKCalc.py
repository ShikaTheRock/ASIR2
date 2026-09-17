nums = []
while True:
    def lenCheck():
        if len(nums) >= 2:
            return 1
        else:
            return 0
    def lastnum():
        pos=len(nums) -1
        numA = nums[pos]
        return float(numA)
    def plastnum():
        pos=len(nums) -2
        numB = nums[pos]
        return float(numB)
    def remops():
        nums.reverse()
        nums.pop(1)
        nums.pop(1)
        nums.reverse()

    print("\n" * 1000)

    print("      ===================== ")
    print("     | ,-----------------. |")
    print("     | |    1.05459 e -34| |")
    print("     | `-----------------' |")
    print("     | [@ ] On/Off  ###### |")
    print("     |              ###### |")
    print("     | [7] [8] [9] [C] [AC]|")
    print("     |                     |")

    print("=====================================")
    print("         PYTHON POLISH KCALC         ")
    print("=====================================")

    print("Wellcome to the CLI python-based polish notation calculator\n\nMenu:\n\nEnter a number and add it to the stack\n\n+. Sum the 2 first numers of the stack\n\n-. Subtract the 2 first numers of the stack\n\n*. Multiply the 2 first numers of the stack\n\n/. Divide the 2 first numers of the stack\n\n^. Power the first number to the second number of the stack\n\ne. Delete a number of the stack\n\nr. Delete all the stack\n\nq. Quit\n\nStack: ")
    for op in nums:
        print(op)
    definput = input("Choose an option:")
    try:
        numtest = float(definput)
        nums.append(definput)
    except:
        if definput == "+":
            if lenCheck() == 1:
                nums.append(plastnum()+lastnum())
                remops()
        elif definput == "-":
            if lenCheck() == 1:
                nums.append(plastnum()-lastnum())
                remops()
        elif definput == "*":
            if lenCheck() == 1:
                nums.append(plastnum()*lastnum())
                remops()
        elif definput == "/":
            if lenCheck() == 1:
                nums.append(plastnum()/lastnum())
                remops()
        elif definput == "^":
            if lenCheck() == 1:
                nums.append(plastnum()**lastnum())
                remops()
        elif definput == "e" or definput == "E":
            nums.reverse()
            nums.pop(0)
            nums.reverse()
        elif definput == "r" or definput == "R":
            nums = []
        elif definput == "q" or definput == "Q":
            print("Vuelve pronto!!")
            break
        else:
            print("NULL VALUE")
            break