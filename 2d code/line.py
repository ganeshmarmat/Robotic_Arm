import math
speed=1
Fileobj=open("C:\\Users\\ganesh\\Desktop\\3dprinter\\New\\Robotic_Arm-master\\Files\\varadamidcore.gcode","w")
def getrange(first,last,step):
    a=[]
    a.append(first);
    if(first>last):
        if(step>0):
            step=step*-1;
        while(first>last):
            first=first+step
            a.append(first)
    else:
        while(first<last-step):
            first=first+step
            a.append(first)
    return a

def writepoint(x1,y1):
    global Fileobj
    Fileobj.write("X"+str(x1)+" Y"+str(y1)+"\n")
    print x1,y1

def writetofile(xst):
    Fileobj.write(xst)
def getpointonline(x1,y1,x2,y2):
    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if(x2-x1)==0 and (y2-y1)==0:
        return;
    if(x2-x1)==0:
        print ((y2-y1)/((y2-y1)*-1))*-1*speed
        for j in getrange(y1,y2,speed):
            writepoint(x1,j)
        return
    if(y2-y1)==0:
        for j in getrange(x1,x2,speed):
            writepoint(j,y1)
        return
    
        
    m=float(float(x2-x1)/float(y2-y1))
    #print m,speed,d
    getlinemover(x1,y1,x2,y2,m,d,speed)
    
def getlinemover(x1,y1,x2,y2,m,d,l):
    if(d>0):
        writepoint(x1,y1)
        t=speed/d;
        xt=(1-t)*x1+t*x2
        yt=(1-t)*y1+t*y2;
        #dx=(l/math.sqrt(1+(m*m)))
        #dy=m*dx
        getlinemover(xt,yt,x2,y2,m,d-l,l)



