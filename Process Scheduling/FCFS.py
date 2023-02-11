#Taking input from text file 
from file_array import file_2_arrays

arrival_time=[]
burst_time=[]
waiting_time=[0]
turnaround=[]
completiontime=[]
file_2_arrays(arrival_time,burst_time)
n=len(arrival_time)
"""
n=5
arrival_time=[0,1,2,3,4]
burst_time=[5,3,1,2,3]
"""
process_id=list(range(1,n+1))

#Waiting time - wt[i] = (bt[0] + bt[1] ...bt[i-1]) - at[i]
def find_waiting_time(waiting_time):
    w=0
    for bt in range(1,n):
        for y in range(bt):
            w+=burst_time[y]
        if w-arrival_time[bt]<0:
            waiting_time.append(0)
        else:
            waiting_time.append(w-arrival_time[bt])
        w=0
find_waiting_time(waiting_time)

#turnaround = burst_time + waiting time (whole waiting time)
def find_turnaround(turnaround):
    for i in range(n):
        turnaround.append(waiting_time[i]+burst_time[i])
find_turnaround(turnaround)
def find_completion(completiontime):
    for x in range(n):
        completiontime.append(turnaround[x]+ arrival_time[x])
find_completion(completiontime)

#ID;ARRIVAL_TIME,BURST_TIME,_WAITING_TIME,TURNAROUND_TIME,COMPLETION_TIME
print("ID:",process_id,"\nAT:",arrival_time,"\nBT:",burst_time,"\nWT:",waiting_time,"\nTAT",turnaround,"\nCT:",completiontime,"\nAverage waiting time: ",sum(waiting_time)/n,"ms\nAverage turnaround time: ",sum(turnaround)/n,"ms")

with open ("results_FCFS.txt",'w') as f :
    #ID;AT;BT;WT;TAT
    for x in range(n):
        z=str(process_id[x])+";"+str(arrival_time[x])+";"+str(burst_time[x])\
        +";"+str(waiting_time[x])+";"+str(turnaround[x])+"\n"
        f.write(z)
        