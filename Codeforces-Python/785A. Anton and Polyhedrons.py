# Solved
##########
n= int(input())
ans=int(0)

for i in range(n):
	polyhedrons=input()
	if polyhedrons=="Icosahedron":
		ans=ans+20
	if polyhedrons=="Dodecahedron":
		ans=ans+12
	if polyhedrons=="Tetrahedron":
		ans=ans+4
	if polyhedrons=="Cube":
		ans=ans+6
	if polyhedrons=="Octahedron":
		ans=ans+8
	
print(ans)

####################
# Solution-2
"""
n=int(input())
counter=0
ans=0
polyhedron_list=[]
 
def count_hedron(text,counter):
	if text=='Tetrahedron':
		counter+=4
	elif text=='Cube':
		counter+=6
	elif text=='Octahedron':
		counter+=8
	elif text=='Dodecahedron':
		counter+=12
	elif text=='Icosahedron':
		counter+=20
	else:
		print("hello")
	return counter
 
 
for i in range(n):	
	text=input()
	ans+=count_hedron(text,counter)
	
print(ans)
"""