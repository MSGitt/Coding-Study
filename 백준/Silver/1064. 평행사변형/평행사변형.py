import sys 


xA, yA, xB, yB, xC, yC = map(int, sys.stdin.readline().split()) 

A = (xA,yA)
B = (xB,yB)     
C = (xC,yC)

if (xA-xB) * (yA-yC) == (yA-yB) * (xA-xC) : 
    print(-1.0)

AB_length = ((xA-xB)**2 + (yA-yB)**2)**0.5
AC_length = ((xA-xC)**2 + (yA-yC)**2)**0.5
BC_length = ((xB-xC)**2 + (yB-yC)**2)**0.5 

max_length = max(AB_length, AC_length, BC_length) 
min_length = min(AB_length, AC_length, BC_length) 

print(2 * (max_length - min_length))
