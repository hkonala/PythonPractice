n=raw_input()
if int(n)%2 == 0:
    if int(n) in range(2,6):
        print("Not Weird")
    elif int(n) in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
