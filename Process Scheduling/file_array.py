def file_2_arrays(arrival_time,burst_time):
    temp=[]
    with open ('procesy.txt','r') as f:
        temp.append(f.readlines())

    temp=temp[0]
    processes = list(map(lambda x: x[:-1], temp))

    for x in processes:
        if x[1]!=";":
            arrival_time.append(int(x[0:2]))
            burst_time.append(int(x[3:5]))
            
        else:
            arrival_time.append(int(x[0]))
            burst_time.append(int(x[2:4]))
