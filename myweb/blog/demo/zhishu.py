primeMax = int(input("请输入素数的范围:"))
#raw_input在Pythonx,y2.7中始终是乱码，先转码，然后将输入的字符串转int  
from math import sqrt         
x = 2  
while x<=primeMax:  
    start = 2  
    end = sqrt(x)  
    while start <= end:  
        if x%start==0:#非素数的满足条件  
            break  
        start+=1#因素自增  
     #此处解释：如果x能被 2~ 根号x整除 然后跳出循环，那么start一定<=end  
     #否则循环完毕start肯定>end，此时就是素数  
    if start>end:  
        print (x)
    x+=1  
print("-------------------------")  
for x in range(2,primeMax+1):  
    flag = True#标记位，默认为素数  
    for y in range(2,int(sqrt(x))+1):  
        if x%y==0:#非素数的满足条件  
            flag = False#非素数  
            break  
    if flag:  
        print(x)