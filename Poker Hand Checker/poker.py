values=['A','K','Q','J','10','9','8','7','6','5','4','3','2']
suits=['C','D','H','S']
def highcard(cardlist):
    high=12
    for i in range(len(cardlist)):
        cardvalue=cardlist[i][:2]
        cardindex=values.index(cardvalue.strip())
        if cardindex <= high:
            high=cardindex
            highindex=i
            card=cardlist[highindex]
    cardlist.pop(highindex)
    return [[card],cardlist]
def onepair(cardlist):
    found=False
    for i in range(len(cardlist)):
        for j in range(i+1,len(cardlist)):
            if cardlist[i][:2].strip()==cardlist[j][:2].strip():
                pair=[cardlist[i],cardlist[j]]
                cardlist.pop(j)
                cardlist.pop(i)
                found=True
                final=[pair,cardlist,[found]]
                break
        if found==True:
            break        
    if found==False:
        return [False]
    else:
        return final
                
def twopair(cardlist):
    found=False
    first=onepair(cardlist)
    if first[0]!=False:
        second=onepair(first[1])
        if second[0]!=False:
            last=[first[0],second[0],second[1],[True]]
            found=True
    if found==True:
        return last
    else:
        return[False]

def threeofakind(cardlist):
    found=False
    for i in range(len(cardlist)):
        for j in range(i+1,len(cardlist)):
            for k in range(j+1,len(cardlist)):
               if cardlist[i][:2].strip()==cardlist[j][:2].strip() and cardlist[i][:2].strip()==cardlist[k][:2].strip() and cardlist[k][:2].strip()==cardlist[j][:2].strip():
                    three=[cardlist[i],cardlist[j],cardlist[k]]
                    cardlist.pop(k)
                    cardlist.pop(j)
                    cardlist.pop(i)
                    found=True
                    final=[three,cardlist,found]
                    break
    if found==False:
        return [False]
    else:
        return final        

def straight(cardlist):
    found=False
    sortedlist=[]
    for i in range(5):
        sorter=highcard(cardlist)
        sortedlist.append(sorter[0])
        cardlist =sorter[1]
    sortednumbers=[]
    for j in range(5):
        sortednumbers.append(sortedlist[j][0][:2].strip())
    for k in range(9):
        if sortednumbers==values[k:k+5]:
            found=True
    if sortednumbers==['A','5', '4', '3', '2']:
        found=True
    if found==True:
        return[sortedlist,[found]]
    else:
        return[False]

def flush(cardlist):
    found=False
    if cardlist[0][-1:]==cardlist[1][-1:] and cardlist[1][-1:]==cardlist[2][-1:] and cardlist[2][-1:]==cardlist[3][-1:] and cardlist[3][-1:]==cardlist[4][-1:]:
        found=True
    return [found]

def fullhouse(cardlist):
    three=threeofakind(cardlist)
    if three==[False]:
        return [False]
    threefound=three[2]
    if threefound==True:
        pair=onepair(three[1])
        if pair==[False]:
            return [False]
        pairfound=pair[2]
    if threefound==True and pairfound==True:
        return [three[0],pair[0],[True]]
    else:
        return[False]

def fourofakind(cardlist):
    found=False
    two=twopair(cardlist)
    if two==[False]:
        return [False]
    else:
        if two[0][0][:2].strip()==two[1][0][:2].strip():
            found=True
            final=[two[0]+two[1],[found]]
    if found==True:
        return final
    else:
        return [False]

def straightflush(cardlist):
    if flush(cardlist)==[False] or straight(cardlist)==[False]:
        return [False]
    else:
        return [True]
def compare_hands(firsthand,secondhand):
    firstlist=list(firsthand)
    secondlist=list(secondhand)
    if straightflush(list(firsthand))!=[False] and straightflush(list(secondhand))==[False]:
        return 1
    elif straightflush(list(firsthand))==[False] and straightflush(list(secondhand))!=[False]:
        return -1
    elif straightflush(list(firsthand))!=[False] and straightflush(list(secondhand))!=[False]:
        if values.index(straight(list(firsthand))[0][1][0][:2].strip())< values.index(straight(list(secondhand))[0][1][0][:2].strip()):
            return 1
        elif values.index(straight(list(firsthand))[0][1][0][:2].strip())> values.index(straight(list(secondhand))[0][1][0][:2].strip()):
            return -1
        elif  values.index(straight(list(firsthand))[0][1][0][:2].strip())== values.index(straight(list(secondhand))[0][1][0][:2].strip()):
            return 0

    if fourofakind(list(firsthand))!=[False] and fourofakind(list(secondhand))==[False]:
        return 1
    elif fourofakind(list(firsthand))==[False] and fourofakind(list(secondhand))!=[False]:
        return -1
    elif fourofakind(list(firsthand))!=[False]and fourofakind(list(secondhand))!=[False]:
        if values.index(fourofakind(list(firsthand))[0][0][:2].strip())< values.index(fourofakind(list(secondhand))[0][0][:2].strip()):
            return 1
        elif values.index(fourofakind(list(firsthand))[0][0][:2].strip())> values.index(fourofakind(list(secondhand))[0][0][:2].strip()):
            return -1

    if fullhouse(list(firsthand))!=[False] and fullhouse(list(secondhand))==[False]:
        return 1
    elif fullhouse(list(firsthand))==[False] and fullhouse(list(secondhand))!=[False]:
        return -1
    elif fullhouse(list(firsthand))!=[False] and fullhouse(list(secondhand))!=[False]:
        if values.index(fullhouse(list(firsthand))[0][0][:2].strip())< values.index(fullhouse(list(secondhand))[0][0][:2].strip()):
            return 1
        elif values.index(fullhouse(list(firsthand))[0][0][:2].strip())> values.index(fullhouse(list(secondhand))[0][0][:2].strip()):
            return -1

    if flush(list(firsthand))!=[False] and flush(list(secondhand))==[False]:
        return 1
    elif flush(list(firsthand))==[False] and flush(list(secondhand))!=[False]:
        return -1
    elif flush(list(firsthand))!=[False] and flush(list(secondhand))!=[False]:
        flushhighfound=False
        while values.index(highcard(list(firsthand))[0][0][:2].strip())==values.index(highcard(list(secondhand))[0][0][:2].strip())  and len(list(firsthand))!=1:
            print(list(firsthand),list(secondhand))
            firsthand=tuple(highcard(list(firsthand))[1])
            secondhand=tuple(highcard(list(secondhand))[1])
        if values.index(highcard(list(firsthand))[0][0][:2].strip())<values.index(highcard(list(secondhand))[0][0][:2].strip()):
            flushhighfound=True
            return 1
        elif values.index(highcard(list(firsthand))[0][0][:2].strip())>values.index(highcard(list(secondhand))[0][0][:2].strip()):
            flushhighfound=True
            return -1
            
        if flushhighfound==False:
            return 0
    
    if straight(list(firsthand))!=[False] and straight(list(secondhand))==[False]:
        return 1
    elif straight(list(firsthand))==[False] and straight(list(secondhand))!=[False]:
        return -1
    elif straight(list(firsthand))!=[False] and straight(list(secondhand))!=[False]:
        if values.index(straight(list(firsthand))[0][1][0][:2].strip())< values.index(straight(list(secondhand))[0][1][0][:2].strip()):
            return 1
        elif values.index(straight(list(firsthand))[0][1][0][:2].strip())> values.index(straight(list(secondhand))[0][1][0][:2].strip()):
            return -1
        elif  values.index(straight(list(firsthand))[0][1][0][:2].strip())== values.index(straight(list(secondhand))[0][1][0][:2].strip()):
            return 0

    if threeofakind(list(firsthand))!=[False] and threeofakind(list(secondhand))==[False]:
        return 1
    elif threeofakind(list(firsthand))==[False] and threeofakind(list(secondhand))!=[False]:
        return -1
    elif threeofakind(list(firsthand))!=[False] and threeofakind(list(secondhand))!=[False]:
        if values.index(threeofakind(list(firsthand))[0][0][:2].strip())< values.index(threeofakind(list(secondhand))[0][0][:2].strip()):
            return 1
        elif values.index(threeofakind(list(firsthand))[0][0][:2].strip())> values.index(threeofakind(list(secondhand))[0][0][:2].strip()):
            return -1
    
    if twopair(list(firsthand))!=[False] and twopair(list(secondhand))==[False]:
        return 1
    elif twopair(list(firsthand))==[False] and twopair(list(secondhand))!=[False]:
        return -1
    elif twopair(list(firsthand))!=[False] and twopair(list(secondhand))!=[False]:
        if (values.index(twopair(list(firsthand))[0][0][:2].strip())< values.index(twopair(list(secondhand))[0][0][:2].strip()) and values.index(twopair(list(firsthand))[0][0][:2].strip())< values.index(twopair(list(secondhand))[1][0][:2].strip())) or (values.index(twopair(list(firsthand))[1][0][:2].strip())< values.index(twopair(list(secondhand))[0][0][:2].strip()) and values.index(twopair(list(firsthand))[1][0][:2].strip())< values.index(twopair(list(secondhand))[1][0][:2].strip())):
            return 1
        elif (values.index(twopair(list(secondhand))[0][0][:2].strip())< values.index(twopair(list(firsthand))[0][0][:2].strip()) and values.index(twopair(list(secondhand))[0][0][:2].strip())< values.index(twopair(list(firsthand))[1][0][:2].strip())) or (values.index(twopair(list(secondhand))[1][0][:2].strip())< values.index(twopair(list(firsthand))[0][0][:2].strip()) and values.index(twopair(list(secondhand))[1][0][:2].strip())< values.index(twopair(list(firsthand))[1][0][:2].strip())):
            return -1
        elif (values.index(twopair(list(firsthand))[0][0][:2].strip())== values.index(twopair(list(secondhand))[0][0][:2].strip()) or values.index(twopair(list(firsthand))[0][0][:2].strip())== values.index(twopair(list(secondhand))[1][0][:2].strip())) and (values.index(twopair(list(firsthand))[1][0][:2].strip())== values.index(twopair(list(secondhand))[0][0][:2].strip()) or values.index(twopair(list(firsthand))[1][0][:2].strip())== values.index(twopair(list(secondhand))[1][0][:2].strip())):
            if values.index(twopair(list(firsthand))[2][0][:2].strip())<values.index(twopair(list(secondhand))[2][0][:2].strip()):
                return 1
            elif values.index(twopair(list(firsthand))[2][0][:2].strip())>values.index(twopair(list(secondhand))[2][0][:2].strip()):
                return -1
            elif values.index(twopair(list(firsthand))[2][0][:2].strip())==values.index(twopair(list(secondhand))[2][0][:2].strip()):
                return 0

    if onepair(list(firsthand))!=[False] and onepair(list(secondhand))==[False]:
        return 1
    elif onepair(list(firsthand))==[False] and onepair(list(secondhand))!=[False]:
        return -1
    elif onepair(list(firsthand))!=[False] and onepair(list(secondhand))!=[False]:
        if values.index(onepair(list(firsthand))[0][0][:2].strip())<values.index(onepair(list(secondhand))[0][0][:2].strip()):
            return 1
        elif values.index(onepair(list(firsthand))[0][0][:2].strip())>values.index(onepair(list(secondhand))[0][0][:2].strip()):
            return -1
        highcardfound=False
        firsthand=tuple(onepair(list(firsthand))[1])
        secondhand=tuple(onepair(list(secondhand))[1])
        while values.index(highcard(list(firsthand))[0][0][:2].strip())==values.index(highcard(list(secondhand))[0][0][:2].strip())  and len(list(firsthand))!=1:
            if values.index(highcard(list(firsthand))[0][0][:2].strip())<values.index(highcard(list(secondhand))[0][0][:2].strip()):
                highcardfound=True
                return 1
            elif values.index(highcard(list(firsthand))[0][0][:2].strip())>values.index(highcard(list(secondhand))[0][0][:2].strip()):
                highcardfound=True
                return -1
            firsthand=tuple(highcard(list(firsthand))[1])
            secondhand=tuple(highcard(list(secondhand))[1])
        if values.index(highcard(list(firsthand))[0][0][:2].strip())<values.index(highcard(list(secondhand))[0][0][:2].strip()):
            highcardfound=True
            return 1
        elif values.index(highcard(list(firsthand))[0][0][:2].strip())>values.index(highcard(list(secondhand))[0][0][:2].strip()):
            highcardfound=True
            return -1
        if highcardfound==False:
            return 0 
            
    while values.index(highcard(list(firsthand))[0][0][:2].strip())==values.index(highcard(list(secondhand))[0][0][:2].strip())  and len(list(firsthand))!=1:
            print(highcard(list(firsthand))[0][0][:2].strip(),highcard(list(secondhand))[0][0][:2].strip())
            if values.index(highcard(list(firsthand))[0][0][:2].strip())<values.index(highcard(list(secondhand))[0][0][:2].strip()):
                highcardfound=True
                return 1
            elif values.index(highcard(list(firsthand))[0][0][:2].strip())>values.index(highcard(list(secondhand))[0][0][:2].strip()):
                highcardfound=True
                return -1
            firsthand=tuple(highcard(list(firsthand))[1])
            secondhand=tuple(highcard(list(secondhand))[1])
    highcardfound=False        
    if values.index(highcard(list(firsthand))[0][0][:2].strip())<values.index(highcard(list(secondhand))[0][0][:2].strip()):
        highcardfound=True
        return 1
    elif values.index(highcard(list(firsthand))[0][0][:2].strip())>values.index(highcard(list(secondhand))[0][0][:2].strip()):
        highcardfound=True
        return -1
    if highcardfound==False:
        return 0 

print(compare_hands(['3 D', '4 D', '9 D', '7 D', '8 D'], ['9 H', '8 H', '7 H', '4 H', '2 H']))

