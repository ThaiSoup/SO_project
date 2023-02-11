#Least Recently Used
#Replace the page that hasn't been used for the longest

size_frame=4
pages=[]
page_fault=0
frame=[]
page_fault=0
h=0
with open ("zastepowanie.txt","r") as f:
    for line in f:
        pages.append(int(line))
#Creating a list of processes with a no. of step in which they were used most recently
n=len(pages)
when_used=[0]*n
pages=list(map(list,zip(pages,when_used)))
step=0

def find_lowest_step(frame):
    lowest_step=1
    while True:
        for y in frame:
            if y[1]==lowest_step:
                return y
        lowest_step+=1

def not_in_frame(frame,page):
    #print("TEST:",frame[0],pages[page])
    for x in range(len(frame)):
        if page[0]==frame[x][0]:
            return False
    return True

def find_same_page(frame,page):
    st=page[0]
    for x in frame:
        if x[0]==st:
            return x

for page in pages:
    step+=1
    p=page[0]
    page[1]=step
    if len(frame)<size_frame and not_in_frame(frame,page):
        page_fault+=1
        frame.append(page) #or page will see
        print("PF",frame)
    else: 
        if not_in_frame(frame,page):
                #find page with lowest step to replace it with a new one
                frame.remove(find_lowest_step(frame))
                frame.append(page)
                page_fault+=1
                print("PF ",frame)
        else:
            if not not_in_frame(frame,page):
                frame.remove(find_same_page(frame,page))
                frame.append(page)
            print("HIT",frame)
            h+=1
print("Ilosc bledow:",page_fault)
#print("Hits: ",h)
print("Fault Rate: ",(page_fault/len(pages))*100,"%")

with open("LRU_results.txt","w") as f:
    f.write(str(page_fault))