import heapq
from collections import defaultdict
import turtle as t

###Keys to sort items in lists###
def getKey_1(item):
    return item[1]
def getKey_2(item):
    return len(item[1])
def getKey_3(item):
    return len(item[0])
def getKey_4(item):
    return item[0]


def encode(frequency):
    heap = [[weight, [symbol,'']] for symbol, weight in frequency.items()]

    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

###main function###
def __main__():
    data = input("Enter a sentence: \n")
    
    try:
        frequency = defaultdict(int)
        for symbol in data:
            frequency[symbol] += 1

        huff = encode(frequency)
        if len(huff)==1:
            a/0
        print("\nSentence:",data,"\n")
        print ("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
        for p in huff:
            p_=str(frequency[p[0]]).ljust(10) + p[1]
            if p[0]==" ":
                print("[space]".ljust(10)+str(frequency[p[0]]).ljust(10) + p[1])
            else:
                print(p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])

        t.hideturtle()
        #set origin point
        origin=0,270
        #set other turtle stuff
        t.speed(0)
        t.pu()
        t.goto(origin)
        t.pd()
        t.color("white")
        t.bgcolor("black")
        #determine how much space of the parent nodes
        def space():
            t.pu()
            t.fd(20)
            t.pd()
        #the branch that goes down left
        def down_lt_branch(a):

            if a==0:
                b=200
            elif a==1:
                b=100
            elif a==2:
                b=50
            elif a==3:
                b=30
            elif a==4:
                b=15
            else:
                b=40//a
            t.fd(10)
            t.rt(90)
            t.fd(b)
            t.lt(90)
            t.fd(10)
            space()
        #the branch that goes down right
        def down_rt_branch(a):
            if a==0:
                b=200
            elif a==1:
                b=100
            elif a==2:
                b=50
            elif a==3:
                b=30
            elif a==4:
                b=15
            else:
                b=40//a
        
            t.fd(10)
            t.lt(90)
            t.fd(b)
            t.rt(90)
            t.fd(10)
            space()
        #write the roots with no circle

        def write_1(c,b):
            t.pu()
            t.lt(90)
            t.bk(b*2)
            t.pd()
            if c!='[space]':
                t.write(c,font=("Helvetica",10,"normal"))
            else:
                t.write(c,font=("Helvetica",8,"normal"))
            t.pu()
            t.fd(b*2)
            t.rt(90)
            t.pd()

        #write the parent roots with a circle
        def write_2(c,b):
            t.pu()
            t.lt(90)
            t.bk(b*2)
            t.pd()
            t.write(c,font=("Helvetica",12,"normal"))
            t.pu()
            t.fd(b*2)
            t.rt(90)
            t.pd()
            t.lt(90)
            t.circle(10)
            t.rt(90)

        #starting with the main branch
        t.pu()
        t.bk(4)
        t.pd()
        t.write(len(data),font=("Helvetica",12,"normal"))
        t.pu()
        t.fd(4)
        t.pd()
        t.circle(10)
        t.rt(90)
        t.pd()
        #list for the binary code for the roots
        q1=[]

        #append all the binary code of the roots

        x1=0
        x=0
        m=0

        while m==0:
            try:
                for i in range(len(huff[x])):
                    if huff[x][1][x1]=='0':
                        down_lt_branch(x1)
                    elif huff[x][1][x1]=='1':
                        down_rt_branch(x1)
                    x1+=1
            except:
                try:
                    if huff[x][0]==" ":
                        write_1("[space]",len('[space]'))
                    else:
                        write_1(huff[x][0],len(huff[x][0]))
                except:
                    m=1
                x+=1
                x1=0
                t.pu()
                t.goto(origin)
                t.pd()
        weights=[]
        weights_01=[]
        for i in huff:
            q1.append(i[1])
            weights_01.append(int(frequency[i[0]])) 
        m=[]

        q=[]
        for i in range(len(q1)):
            m.append(q1[i])
            m.append(weights_01[i])
            q.append(m)
            m=[]
        q=sorted(q,key=getKey_1)
        q=sorted(q,key=getKey_3)
        #########

        bq=[]
        a=0
        c=0
        ###To find the parent nodes of the roots of the Huffman tree###
        while True:
            try:
                bq=[]
                for i in q:
                    y=list(i[0])
                    y.pop(len(y)-1)
                    j=''.join(y)
                    bq.append(j)
                a=0
                if len(bq)==2:
                    break
                for x in range(len(bq)-1):
                    if bq[x]==bq[x+1]:
                        q[x][1]=int(q[x][1]+q[x+1][1])
                        q[x][0]=bq[x]
                        l=q[x]
                        c=0
                        for i in range(len(l[0])):
                            if l[0][c]=="0":
                                down_lt_branch(c)
                            elif l[0][c]=="1":
                                down_rt_branch(c)
                            c+=1
                        write_2(l[1],len(str(l[1])))
                        t.pu()
                        t.goto(origin)
                        t.pd()
                        q[x+1]=['']
                        a+=1
                for i in range(a):
                    q.remove([''])
                q=sorted(q,key=getKey_4)
                q=sorted(q,key=getKey_3)
            except:
                break

        
        ascii_total_bits=0
        huff_total_bits=0
        no_of_bits_per_chr=[]
        for i in huff:
            no_of_bits_per_chr.append(int(len(i[1])*int(frequency[i[0]])))
        for i in no_of_bits_per_chr:
            huff_total_bits+=i
        ascii_total_bits=len(data*7)
        print('\nNumber of bits used in Huffman coding: '+str(huff_total_bits))
        print('Number of bits used in ASCII coding: '+str(ascii_total_bits)+"\n")
        print('Storage saved by using Huffman coding instead of ASCII coding:',int(ascii_total_bits-huff_total_bits),"bits\n")
    except:
        
        print("There was an error, please type two or more different characters\n")
    
    tm=input("Press Enter to continue, enter 'q' to quit\n")
    if tm!='q':
        t.Screen().reset()
        __main__()


###call main function
__main__()
