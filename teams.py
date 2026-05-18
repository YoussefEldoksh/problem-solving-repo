

def check_problem(val1,val2,val3):
    val = (f"{val1}{val2}{val3}")
    if(val == '111' or val == '101' or val == '011' or val == '110' ):
        return 1
    else: return 0



n = int(input())

output = 0
for i in range(n):
    vals = input()
    a, b, c = map(int,vals.split())
    output += check_problem(a ,b ,c)
print(output)