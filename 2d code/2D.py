import math
firsthand=150#in mm
secondhand=100#in mm
homelocation=(firsthand+secondhand)-math.sqrt(3)/2*(firsthand+secondhand)
speed=2
# in mm
def getangle(a,b,c):
    cosa=(a**2+b**2-c**2)
    
    #cosa=cosa/(2*a*b)
    print (a,b,c,cosa)
    try:
        cosa=cosa/(2*a*b)
        return round(math.acos(cosa)*180/math.pi,2)
    except:
        return 0
    return 0
        
    

def readfile():
    f=open("C:\\Users\\ganesh\\Desktop\\3dprinter\\line_ganeshmarmat.gcode","r")
    fr=open("C:\\Users\\ganesh\\Desktop\\3dprinter\\line_ganeshmarmat1.gcode","w")
    fc=open("C:\\Users\\ganesh\\Desktop\\3dprinter\\line_ganeshmarmat2.gcode","w")
    x=0
    y=0
    z=0
    hi=0
    for l in f:
        line=l.split()
        
        for token in line:
            if 'X' in token:
                z=float(token[1:])+homelocation
            if 'Y' in token:
                y=float(token[1:])+homelocation
            if 'Z' in token:
                hi=float(token[1:])
                #z=float(token[1:])
            
        distancexy=math.hypot(x,y)
        
        A=getangle(x,distancexy,y)#below rotation angle
        
        distancexyz=math.hypot(distancexy,z)#hypo for abve y axiis toward z
        b=getangle(distancexy,distancexyz,z)#first angle upto z point
        B=getangle(distancexyz,firsthand,secondhand)+b#adding both angle
        C=getangle(firsthand,secondhand,distancexyz)
        fr.write("A"+str(A)+" B"+str(B)+" C"+str(C)+"#x="+str(x)+" y="+str(y)+" z="+str(z)+"\n")
        fc.write("|5="+str(B)+"|6="+str(C)+"|13="+str(hi)+"|\n")
        print("A"+str(A)+" B"+str(B)+" C"+str(C)+"\n")


def writepoint(x1,y1):
    print x1,y1
def getlinemove(x1,y1,x2,y2):
    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if(x2-x1)==0 and (y2-y1)==0:
        return;
    if(x2-x1)==0:
        print ((y2-y1)/((y2-y1)*-1))*-1*speed
        for j in range(y1,y2,((y2-y1)/((y2-y1)*-1))*-1*speed):
            writepoint(x1,j)
        return
    if(y2-y1)==0:
        for j in range(x1,x2,((x2-x1)/((x2-x1)*-1))*-1*speed):
            writepoint(j,y1)
        return
    
        
    m=float(float(x2-x1)/float(y2-y1))
    print m,speed,d
    getlinemover(x1,y1,m,d,speed)
def getlinemover(x1,y1,m,d,l):
    if(d>0):
        writepoint(x1,y1)
        dx=(l/math.sqrt(1+(m*m)))
        dy=m*dx
        getlinemover(x1+dx,y1+dy,m,d-l,l)
def getacrmove(x1,y1,x2,y2,xi,yj):
    dc=math.sqrt((x2-x1)**2+(y2-y1)**2)
    ctrx=x1+xi
    ctry=y1+yj
    da=math.sqrt((ctrx-x1)**2+(ctry-y1)**2)
    db=math.sqrt((ctrx-x2)**2+(ctry-y2)**2)
    angle=getangle(da,db,dc)
    getarcmoves(x1,y2,angle,da,db);
def getarcmoves(x1,y1,angle,rx,ry):
    r=math.sqrt((rx**2+ry**2)/2)
    stepthita=(2*math.pi*r*(angle/360))/speed
    stepthita=(angle/stepthita)
    cnt=0;
    print angle,stepthita
    while(cnt<angle):
        cnt=cnt+stepthita
        i=cnt*(math.pi/180)
        tempx=r*math.cos(i)+x1
        tempy=r*math.cos(i)+y1
        writepoint(tempx,tempy)
        
    



def getpointoncircle(sx,sy,ex,ey,xr,yr):
    angle=360
    cnt=0
    cnt=currentangle(sx,sy,xr,yr)
    points=[]
    print cnt
    csx=yr*math.sin(cnt)
    csy=xr*math.cos(cnt)
    
    stepthita=getthita(xr,yr,speed)
    while(cnt<angle):
        cnt=cnt+stepthita
        i=cnt*(math.pi/180)
        tempy=yr*math.sin(i)
        tempx=xr*math.cos(i)
        points.append((tempx,tempy))
        #newx=tempx-csx
        #newy=tempy-csx
        writepoint(tempx,tempy)
        #writepoint(newx+sx,newy+sy)
        if(math.sqrt((tempx-ex)**2+(tempy-ey)**2)<speed):
            break
    return points
        
def currentangle(startx,starty,rx,ry):
    cnt=0
    old=100
    while(1):
        i=cnt*(math.pi/180)
        endy=ry*math.sin(i)
        endx=rx*math.cos(i)
        dist=math.sqrt((endx-startx)**2+(endy-starty)**2)
        #print dist,endx,endy
        #print dist
        if(dist>old and dist<1):
            break;
        if(cnt==360):
            break;
        old=dist
        cnt=cnt+1
    return cnt
    
def getthita(xr,yr,speed):
    startx=yr*math.sin(0)
    starty=xr*math.cos(0)
    cnt=1;
    old=0
    while(1):
        endx=yr*math.sin(cnt)
        endy=xr*math.cos(cnt)
        dist=math.sqrt((endx-startx)**2+(endy-starty)**2)
        #print dist
        if(dist==speed):
            break;
        if(dist>speed):
            cnt=cnt-0.01
            if(old==dist):
                break;
            old=dist
        else:
            cnt=cnt+0.01

    return cnt
    




                     
def main():
    print getpointoncircle(0,5,-5,0,5,5)
    #print getthita(20,10,1)
    #print currentangle(0,5,10,5)

    
    #print("enter file path")
    #fpath=raw_input()
    #print(fpath)
    #readfile()
    #getlinemove(1,11,3,11)
    #getacrmove(10,0,0,10,10,0)
    #print getangle(0,0,0)
    #print homelocation
    
main();
