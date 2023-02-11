import random

#Generating in pattern: AT;BT
temp=[]
n=10
for x in range(0,n):
    arrival_time = random.randint(0,50)
    z=arrival_time
    temp.append(z)

temp.sort()

processes = [str(x) for x in temp]
for x in range(0,len(temp)):
    burst_time = random.randint(1,50)
    processes[x]+= ";"+str(burst_time)+"\n"
with open ('procesy.txt', 'w') as f:
    for x in processes:
        f.writelines(x)

