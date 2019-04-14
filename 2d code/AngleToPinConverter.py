pinA=3
pinB=9
pinC=13

def ConvertAngleToPin(filepath,filepath2):
    f=open(filepath,"r")
    fr=open(filepath2,"w")
    for l in f:
        line=l.split()
        fr.write("|")
        for token in line:
            
            if 'A' in token:
                a=float(token[1:])
                fr.write(str(pinA)+"="+str(a))
                fr.write("|")
            if 'B' in token:
                b=float(token[1:])
                fr.write(str(pinB)+"="+str(b))
                fr.write("|")
            if 'C' in token:
                c=float(token[1:])
                fr.write(str(pinC)+"="+str(c))
                fr.write("|")
            
                 
        fr.write("\n")


        
ConvertAngleToPin("C:\\Users\\ganesh\\Desktop\\3dprinter\\New\\Robotic_Arm-master\\Files\\varadaangle.gcode","C:\\Users\\ganesh\\Desktop\\3dprinter\\New\\Robotic_Arm-master\\Files\\varadapin.gcode")
