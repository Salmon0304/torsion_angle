from math import pi
from math import acos
from sys import argv

def distance(line1,line2):
  x1=[float(line1[30+i*8:38+i*8]) for i in range(3)]
  x2=[float(line2[30+i*8:38+i*8]) for i in range(3)]
  return (sum([(x1[i]-x2[i])**2 for i in range(3)]))**0.5

def angle(a1,a2,a3):
    dist12=((a1[0]-a2[0])**2+(a1[1]-a2[1])**2+(a1[2]-a2[2])**2)**0.5
    dist32=((a3[0]-a2[0])**2+(a3[1]-a2[1])**2+(a3[2]-a2[2])**2)**0.5
    cross=(a1[0]-a2[0])*(a3[0]-a2[0])+(a1[1]-a2[1])*(a3[1]-a2[1])+(a1[2]-a2[2])*(a3[2]-a2[2])
    return acos(cross/dist12/dist32)/pi*180.0

def cross_p(a,b):
    x=a[1]*b[2]-a[2]*b[1]
    y=a[2]*b[0]-a[0]*b[2]
    z=a[0]*b[1]-a[1]*b[0]
    return([x,y,z])

def torsion_angle(line1,line2,line3,line4):
    lines=[line1,line2,line3,line4]
    x=[float(i[30:38]) for i in lines]
    y=[float(i[38:46]) for i in lines]
    z=[float(i[46:54]) for i in lines]
    V12=[i[0]-i[1] for i in [x,y,z]]
    V32=[i[2]-i[1] for i in [x,y,z]]
    V23=[i[1]-i[2] for i in [x,y,z]]
    V43=[i[3]-i[2] for i in [x,y,z]]
    vertical_v1,vertical_v2=cross_p(V12,V32),cross_p(V23,V43)
    vertical_v3=cross_p(vertical_v1,vertical_v2)
    da=angle(vertical_v1,[0.0,0.0,0.0],vertical_v2)
    if vertical_v3[0]*V32[0] < 0:
        da*=-1
    
    return da



