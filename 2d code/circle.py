import math
speed=1
def writepoint(x1,y1):
    print x1,y1

def getpointoncircle(sx,sy,ex,ey,xr,yr,direction):
    angle=360
    cnt=0
    cnt=currentangle(sx,sy,xr,yr)
    points=[]
    points.append((sx,sy))
    print cnt
    csx=yr*math.sin(cnt)
    csy=xr*math.cos(cnt)
    ori=0
    stepthita=getthita(xr,yr,speed)
    print stepthita
    old=5
    while(cnt<angle):
        ori=ori+1
        cnt=cnt+(stepthita * direction)
        if(cnt>360):
            cnt=cnt%360
        i=cnt*(math.pi/180)
        tempy=yr*math.sin(i)
        tempx=xr*math.cos(i)
        points.append((tempx,tempy))
        #newx=tempx-csx
        #newy=tempy-csx
        writepoint(tempx,tempy)
        #writepoint(newx+sx,newy+sy)
        dist=math.sqrt((tempx-ex)**2+(tempy-ey)**2)
        if(dist<speed):
            break
            if(old<dist):#this will not call
                break
        if(ori==360):
            break
        old=dist
    points.append((ex,ey))
    return points
        
def currentangle(startx,starty,rx,ry):
    cnt=0
    old=100
    while(1):
        cnt=cnt+0.1
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
        
    return cnt
    
def getthita(xr,yr,speed):
    
    cnt=1;
    i=cnt*(math.pi/180)
    startx=yr*math.sin(i)
    starty=xr*math.cos(i)
    old=0
    while(1):
        i=cnt*(math.pi/180)
        endx=yr*math.sin(i)
        endy=xr*math.cos(i)
        dist=math.sqrt((endx-startx)**2+(endy-starty)**2)
        #print dist
        if(dist==speed):
            break;
        if(dist>speed):
            cnt=cnt-0.1
            if(old==dist):
                break;
            old=dist
        else:
            cnt=cnt+0.1

    return cnt#*(math.pi/180)
    



