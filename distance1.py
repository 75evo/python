import math

pos=[0,0]
up=int(input("Enter upwards steps: "))
down=int(input("Enter downwards steps: "))
left=int(input("Enter left steps: "))
right=int(input("Enter right steps: "))

if up:
 pos[1]+=up
if down:
 pos[1]-=down
if left:
 pos[0]=pos[0]-left
if right:
 pos[0]=pos[0]+right

print(pos)

print(round(math.sqrt(pos[0]**2+pos[1]**2)))

