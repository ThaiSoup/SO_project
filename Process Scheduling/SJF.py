from file_array import file_2_arrays
""" Implementacja:
1.Przejdź przez wszystkie procesy do momentu, aż zostaną one całkowicie wykonane.
    a) Znajdź proces o najmniejszym remaining_bt przy każdym pojedynczym kroku czasowym.
    b) Zmniejsz jego czas o 1.
    c) Sprawdź, czy pozostały czas jest równy 0
    d) Zwiększ licznik zakończonych procesów.
    e) Czas zakończenia bieżącego procesu =bieżący czas +1;
    f) Oblicz czas oczekiwania dla każdego ukończonego procesu
    wt[i]= completion time - arrival time - burst time
    g) Zwiększ time o 1
2. Znajdź turn around time (czas oczekiwania + czas trwania)
"""


at = []
bt = []
file_2_arrays(at,bt)
n = len(at)

wt = [0] * n
tat = [0] * n
completion = []

"""
n=5
at=[2,5,1,0,4]
bt=[6,2,8,3,4]
"""
pid=list(range(1,n+1))
processes=[]
for x in range(n):
    processes.append([pid[x],at[x], bt[x]])
print(processes)
processes.sort(key=lambda x : x[2] )



def findWaitingTime(processes, n, wt):  
    remaining_bt = [0] * n 
    #duplicating burst time  
    for i in range(n):  
        remaining_bt[i] = processes[i][2] 
    complete = 0
    time= 0
    low  = 99999
    low_i = 0
    check = 0
    #loop untill all proceses are completed  
    while complete != n: 
        #finding processes with with minimum remaining_bt of processes that arrived in time
        for j in range(n): 
            if (processes[j][1] <= time) and (remaining_bt[j] < low ) and remaining_bt[j] > 0: 
                low  = remaining_bt[j] 
                low_i = j 
                check = True
        if check == 0: 
            time+= 1
            continue
        remaining_bt[low_i] -= 1
        # Update minimum  
        low  = remaining_bt[low_i]  
        if (low  == 0):  
            low  = 99999
        #if a process gets executed:
        if (remaining_bt[low_i] == 0):   
            complete += 1
            check = 0
            #find finish time of current process  
            f_time = time+ 1
            # calculate waiting time  
            wt[low_i] = (f_time - processes[low_i][2] -processes[low_i][1]) 

            if (wt[low_i] < 0): 
                wt[low_i] = 0
        #time increment
        time+= 1

findWaitingTime(processes, n, wt)

def findTurnAroundTime(processes, n, wt, tat):  
    for i in range(n): 
        tat[i] = processes[i][2] + wt[i] 

findTurnAroundTime(processes, n, wt, tat) 

with open ("results_SJF.txt",'w') as f :
    #ID;AT;BT;WT;TAT
    for x in range(n):
        z=str(processes[x][0])+";"+str(processes[x][1])+";"+str(processes[x][2])+";"+str(wt[x])+";"\
        +str(tat[x])+"\n"
        f.write(z)


print("ID:",pid)
print("AT:",at)
print("BT:",bt)
print("WT:",wt)
print("TAT",tat)
print("Average waiting time: ",sum(wt)/n)
print("Average turnaround time: ",sum(tat)/n)
