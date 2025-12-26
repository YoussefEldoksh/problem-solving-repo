def reverse(x):
    num = 0
    while x > 0:
        num = (num*10)+(x%10)
        x = x//10
    print(num)

reverse(12345)
