from queue import PriorityQueue
from util2 import *

sys.setrecursionlimit(5000000)

import faulthandler

faulthandler.enable()

w = PriorityQueue()

scanned = set()

w.put((REGEX().getCost(), REGEX()))


count = 0
traversed = 1
start = time.time()
prevCost = 0

rpn3 = 0
rpn4 = 0
rpn5 = 0
rpn6 = 0
rpn7 = 0
rpn8 = 0
rpn9 = 0
rpn10 = 0
rpn11 = 0
rpn12 = 0
rpn13 = 0


r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
r7 = 0
r8 = 0
r9 = 0
r10 = 0



finished = False


while not w.empty() and not finished:
    tmp = w.get()
    s = tmp[1]
    cost = tmp[0]

    prevCost = cost
    hasHole = s.hasHole()

    #print("state : ", s, " cost: ",cost)
    if hasHole and s.rpn()<=10:
        for j, new_elem in enumerate([Character('0'), Character('1'), Or(),  Or(Character('0'),Character('1')), Concatenate(Hole(),Hole()), KleenStar(), Question()]):

            #print(repr(s), repr(new_elem))

            k = copy.deepcopy(s)
            if not k.spread(new_elem):
                #print("false "+ new_elem)
                continue

            traversed += 1
            if repr(k) in scanned:
                # print("Already scanned?", repr(k))
                # print(list(scanned))
                continue
            else:
                scanned.add(repr(k))

            checker = False
            if repr(new_elem) == '0|1':
                checker = True

            end = False

            if k.starnormalform():
                # print(repr(k), "starNormalForm")
                r1+=1
                end = True
                continue

            if k.redundant_concat1():
                # print("concat1")
                r2 += 1
                end = True
                continue

            if k.redundant_concat2():
                # print("concat2")
                r3 += 1
                end = True
                continue

            if k.KCK():
                # print(repr(k), "is KCK")
                r4 += 1
                end = True
                continue

            if k.KCQ():
                # print(repr(k), "is KCQ")
                r5 += 1
                end = True
                continue

            if k.QC():
                # print(repr(k), "is QC")
                r6 += 1
                end = True
                continue

            if type(new_elem) == type(Question()) and k.OQ():
                # print(repr(k), "is OQ")
                r7 += 1
                end = True
                continue

            if is_orinclusive(k):
                # print(repr(k), "is orinclusive")
                r8 += 1
                end = True
                continue

            if k.prefix():
                #print(repr(k), "is prefix")
                r9 += 1
                end = True
                continue

            if k.sigmastar():
                #print(repr(k), "is equivalent_KO")
                r10 += 1
                end = True
                continue

            if end:
                continue

            if k.rpn()<=10:
                w.put((k.getCost(), k))



    if count % 1000 == 0:
        print("Iteration:", count, "\tCost:", cost, "\tScanned REs:", len(scanned), "\tQueue Size:", w.qsize(), "\tTraversed:", traversed)
    count = count+1

    if s.rpn() <= 13:
        rpn13 += 1
    if s.rpn() <= 12:
        rpn12 += 1
    if s.rpn() <= 11:
        rpn11 += 1
    if s.rpn() <= 10:
        rpn10 += 1
    if s.rpn() <= 9:
        rpn9 += 1
    if s.rpn()<=8:
        rpn8 +=1
    if s.rpn() <= 7:
        rpn7 += 1
    if s.rpn() <= 6:
        rpn6 += 1
    if s.rpn() <= 5:
        rpn5 += 1
    if s.rpn() <= 4:
        rpn4 += 1


print("--end--")
print("count = ")
print(count)

'''print("r1:" + str(r1))
print("r2:" + str(r2))
print("r3:" + str(r3))
print("r4:" + str(r4))
print("r5:" + str(r5))
print("r6:" + str(r6))
print("r7:" + str(r7))
print("r8:" + str(r8))
print("r9:" + str(r9))
print("r10:" + str(r10))'''

print("rpn4: "+ str(rpn4))
print("rpn5: "+ str(rpn5))
print("rpn6: "+ str(rpn6))
print("rpn7: "+ str(rpn7))
print("rpn8: "+ str(rpn8))
print("rpn9: "+ str(rpn9))
print("rpn10: "+ str(rpn10))
print("rpn11: "+ str(rpn11))
print("rpn12: "+ str(rpn12))
print("rpn13: "+ str(rpn13))



print("time = ")
print(time.time()-start)





