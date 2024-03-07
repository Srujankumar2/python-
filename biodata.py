fp=open("192325030.txt","r")
line_count =0
for line in fp:
    line_count+=1
    if (line_count<=3):
        print(line)
    else:
        break
    
