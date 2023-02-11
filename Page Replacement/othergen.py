import random

temp=[]
n=10
for x in range(0,n):
    arrival_time = random.randint(1,10)
    z=arrival_time
    temp.append(z)
    
processes = [str(x) for x in temp]

with open ('zastepowanie.txt', 'w') as f:
    for x in processes:
        z=x+"\n"
        f.writelines(z)
        
