input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))


binarylist = input_lines

def criteria_find(count,binarylist,ratingtype="oxygen"):
    checkdict = {"0":[],"1":[]}
    for i in binarylist:
        if i[count] == '0':
            checkdict['0'].append(i)
        else:
            checkdict['1'].append(i)
    #
    if ratingtype == "oxygen":
        
        if len(checkdict['0']) > len(checkdict['1']):
            binarylist=checkdict['0']
        elif len(checkdict['0']) < len(checkdict['1']):
            binarylist=checkdict['1']
        else:
            binarylist=checkdict['1']
        if len(binarylist)==1:
            return binarylist[0]
        else:
            return criteria_find(count+1,binarylist,"oxygen")
    #    
    elif ratingtype == "co2":
        
        if len(checkdict['0']) < len(checkdict['1']):
            binarylist=checkdict['0']
        elif len(checkdict['0']) > len(checkdict['1']):
            binarylist=checkdict['1']
        else:
            binarylist=checkdict['0']
        if len(binarylist)==1:
            return binarylist[0]
        else:
            return criteria_find(count+1,binarylist,"co2")
    #    
    else:
        print("ratingtype must be 'oxygen' or 'co2'")


oxygen = criteria_find(0,binarylist)
co2 = criteria_find(0,binarylist,'co2')

print(int(oxygen,2)*int(co2,2))

# did this one messier initially, then cleaned up into one function




