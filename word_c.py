fname=input("please enter the file name:")
#Or just press enter without entering any file name 
# to open a default .txt file. In this case I had 
# used clown.txt
if len(fname) < 1:
    fname="clown.txt"
hand=open(fname)

di = dict()

for lines in hand:
    lines=lines.rstrip()
    #print(lines)
    words=lines.split()
    #print(words)

    for each_w in words:
        
        #print(each_w,di.get(each_w,-99)) #if not present do default -99

        #Code1
        """
        defaultv = di.get(each_w,0)
        print(each_w, "defaultv: ",defaultv)
        newv = defaultv + 1
        print(each_w,"newv: ",newv)
        di[each_w] = newv
        """

        #Code2
        #idiom: retrieve/update/create counter
        di[each_w] = di.get(each_w,0) + 1
        print("The word:",each_w,"is repeated", di[each_w],"times")

        #Code3
        """
        if each_w in di:
            di[each_w]=di[each_w]+1
        else:
            di[each_w]=1
            #print("**New_Word**")
        #print(each_w,di[each_w])
        """

#print("\n")
#Uncomment to see complete dictionary and word count
#print("The Final dic. is:",di)

#most common word
print("\n")
largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k #capture/remember the key that was largest

print("The largest number is:",largest,"of the word:",theword)
    #print(k,v)
