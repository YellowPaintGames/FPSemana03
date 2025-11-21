from collections import deque
nums=deque()
ask=input("Dê um conjunto de números INTEIROS, SEPARADOS POR ESPAÇOS: ")
for num in ask.split():
    nums.append(int(num))
print(nums) 
while nums:
    value = nums.pop()*2
    print(value)