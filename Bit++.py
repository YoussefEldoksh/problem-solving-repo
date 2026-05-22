


def check_command(cmd,val):
    if cmd == "++X" or cmd == "X++":
        val +=1
    elif cmd == "--X" or cmd == "X--":
        val -=1
    return val


n = int(input())
value = 0

for i in range(n):
    cmd = input()
    value = check_command(cmd,value)

print(value)