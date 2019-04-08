import math
import line as l
import circle as cir
firsthand=150#in mm
secondhand=150#in mm
old_x=0
old_y=0
x=0
y=0
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
def writez(z):
    if(z==-1):
        l.writetofile("C0\n")
    else:
        l.writetofile("C90\n")
def G1(line):
    global x
    global y
    global old_x
    global old_y
    old_x=x
    old_y=y
    for token in line:
        if 'X' in token:
            x=float(token[1:])
        if 'Y' in token:
            y=float(token[1:])
        if 'Z' in token:#temp for 2d code
            z=float(token[1:])
            writez(z)
    l.getpointonline(old_x,old_y,x,y)
        
def G0(line):
    global x
    global y
    global old_x
    global old_y
    old_x=x
    old_y=y
    for token in line:
        if 'X' in token:
            x=float(token[1:])
        if 'Y' in token:
            y=float(token[1:])
        if 'Z' in token: #temp for 2d code
            z=float(token[1:])
            writez(z)
    l.writepoint(x,y)
    

def writecirclepoint(data,sx,sy):
    l.writetofile("###\n")
    print data
    first=data[0]
    for d in data:
        l.writepoint(sx+(d[0]-first[0]),sy+(d[1]-first[1]))
    l.writetofile("###\n")
def G2(line):
    global x
    global y
    global old_x
    global old_y
    old_x=x
    old_y=y
    i=0
    j=0
    for token in line:
        if 'X' in token:
            x=float(token[1:])
        if 'Y' in token:
            y=float(token[1:])
        if 'I' in token:
            i=float(token[1:])
        if 'J' in token:
            j=float(token[1:])
    
    cx=old_x+i
    cy=old_y+j
    print "*****************"
    
    if(i==0):
        i=j
    if(j==0):
        j=i
    print old_x,old_y,x,y
    print old_x-cx,old_y-cy,x-cx,y-cy,i,j,-1
    data=cir.getpointoncircle(old_x-cx,old_y-cy,x-cx,y-cy,i,j,-1)
    writecirclepoint(data,old_x,old_y)
    
        
    print "*******************"
def G3(line):
    global x
    global y
    global old_x
    global old_y
    old_x=x
    old_y=y
    i=0
    j=0
    for token in line:
        if 'X' in token:
            x=float(token[1:])
        if 'Y' in token:
            y=float(token[1:])
        if 'I' in token:
            i=float(token[1:])
        if 'J' in token:
            j=float(token[1:])
    
    cx=old_x+i
    cy=old_y+j
    print "*****************"
    print old_x-cx,old_y-cy,x-cx,y-cy,i,j,1
    if(i==0):
        i=j
    if(j==0):
        j=i
    data=cir.getpointoncircle(old_x-cx,old_y-cy,x-cx,y-cy,i,j,1)
    writecirclepoint(data,old_x,old_y)
    print "*******************"

def ReadGcodeFile(filepath):
    f=open(filepath,"r")
    for l in f:
        line=l.split()
        if 'G1' in line:
            G1(line)
            continue
        if 'G0' in line:
            G0(line)
            continue
        if 'G2' in line:
            G2(line)
            continue
        if 'G3' in line:
            G3(line)
            continue        

def Convert2dtoangle(filepath,filepath2):
    f=open(filepath,"r")
    fr=open(filepath2,"w")
    for l in f:
        line=l.split()
        x=0
        y=0
        for token in line:
            if 'X' in token:
                x=float(token[1:])
            if 'Y' in token:
                y=float(token[1:])
            if 'C' in token:#for tempray 2d code
                z=float(token[1:])
                fr.write("C"+str(z)+"\n")
                
        distancexy=math.hypot(x,y)
        if x==0:
            A1=90
            distancexy=y
        else:
            A1=getangle(x,distancexy,y)#below rotation angle
        if y==0:
            distancexy=x
        A2=getangle(distancexy,firsthand,secondhand)

        A=A1+A2
        B=getangle(firsthand,secondhand,distancexy)

        fr.write("A"+str(A)+" B"+str(B)+"#x="+str(x)+" y="+str(y)+"\n")
        
        print("A"+str(A)+" B"+str(B)+"\n")

def main():
    ReadGcodeFile("C:\\Users\\\ganesh_marmat\\Desktop\\3d\\Robotic_Arm-master\\2d code\\files\\varada.gcode");
    Convert2dtoangle("C:\\Users\\\ganesh_marmat\\Desktop\\3d\\Robotic_Arm-master\\2d code\\files\\varadamidcore.gcode","C:\\Users\\\ganesh_marmat\\Desktop\\3d\\Robotic_Arm-master\\2d code\\files\\varadaangle.gcode")
main()
