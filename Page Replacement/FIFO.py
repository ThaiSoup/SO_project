from collections import deque
#replace the pages that has been in the memory for longest time
#since the process of adding pages and removing will be from the first and last we will use queue for frame

size_frame=8
pages=[]
page_fault=0

with open ("zastepowanie.txt","r") as f:
    for line in f:
        pages.append(int(line))
mis=pages[0]
#Using queue
print(pages)
frames=deque()
def pprint_queue(frames,page,missing):
    frames=str(frames)
    print(frames[6:-1],"Needed:",page,"Missing:",missing)

for page in pages:
    
    if len(frames)<size_frame and page not in frames:
        mis=page
        pprint_queue(frames,page,mis)
        frames.append(page)
        page_fault+=1

    else:
        if page not in frames:
            mis=page
            pprint_queue(frames,page,mis) 
            frames.popleft()
            frames.append(page)
            page_fault+=1
        else: #just for pretty queue print
            pprint_queue(frames,page,mis)           
    mis=None

print("Ilosc bledow:",page_fault)
print("Fault Rate:",(page_fault/len(pages))*100,"%")
with open("FIFO_results.txt","w") as f:
    f.write(str(page_fault))
