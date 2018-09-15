import csv

flag = True

while flag:
    userName = input("username:")
    passWord = input("passWord:")
    count = 0
    exist = True
    with open('eggs.csv', newline='') as f:
        reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        for row in reader:
            print(row[0])
            print(row[1])
            if userName == row[0] and passWord == row[1]:
                print('''welcome user {name} login...'''.format(name=userName))
                exist = False
                flag = False
                break
        if exist:
            print("invalid name or passWord")
            with open('some.csv', newline='') as readfile:
                reader = csv.reader(readfile, delimiter=':', quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    if userName == row[0]:
                        count +=1
                        print(userName + "======")
                        print(row[0])
                        if count >= 2:
                            print("you have tried too many times, fuck off")
                            flag = False
                            break
            with open('some.csv', 'a', newline='') as writefile:
                spamwriter = csv.writer(writefile, delimiter=':', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([userName])










