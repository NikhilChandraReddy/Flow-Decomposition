import sys

input1= [];
heuristic = [];
visited=[];
fringe=[];
route=[];


#need to added methods

if len(sys.argv) < 4:
    print ("No in correct format")

start = sys.argv[2];
goal = sys.argv[3];

filepath = sys.argv[1]
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line != "END OF INPUT":
       input1.append(line.split());
       line = fp.readline()
h=0;
if len(sys.argv)==5:
	h=1;
	filepath = sys.argv[4]
	with open(filepath) as fp:
	   line = fp.readline()
	   while line != "END OF INPUT":
	       heuristic.append(line.split());
	       line = fp.readline()

s=0;
e=0;
g=0;
List=[0,start,0,0,0,0]
#print(visited)
route.append(List)
fringe.append(List)
#print(fringe)
y=[]
#print("\n\nprinting LIST \n\n\n")
#print(List)
visited.append(List[1])
while (List[1]!=goal):
	#print("\n\n\nbefore removing")
	#print(fringe)
	for x in fringe:
		if x[1]==List[1]:
			fringe.remove(x)
			e=e+1
			break
			#visited.append(x)
	for x in input1:
		if x[0]==List[1]:
			g=g+1;
			if x[1] not in visited:
				#print("\n\nprinting X \n\n\n")
				#print(x)
				if(h==0):
					s=0
				else:
					for z in heuristic:
						if(z[0]==x[1]):
							s=int(z[1])

				y=[List[1],x[1],List[2]+1,List[3]+int(x[2]),List[3]+s+int(x[2]),int(x[2])]
				visited.append(x[1])
				fringe.append(y)
				route.append(y)

		elif x[1]==List[1]:
			g=g+1
			if x[0] not in visited:
				#print("\n\nprinting X \n\n\n")
				#print(x)
				if(h==0):
					s=0
				else:
					for z in heuristic:
						if(z[0]==x[0]):
							s=int(z[1])

				y=[List[1],x[0],List[2]+1,List[3]+int(x[2]),List[3]+s+int(x[2]),int(x[2])]
				visited.append(x[0])
				fringe.append(y)
				route.append(y)

	if(h==0):
		bubbleSort(fringe)
		e=int(len(set(visited)))-1
	else:
		bubbleSort_hur(fringe)
		e=int(len(set(visited))/2)
	#print("\n\n\n after sorting")
	#print(fringe)
	if(len(fringe)==0):
		List[3]='infinity';
		break
	List=fringe[0]

print ("\n\nmaximum nodes in memory:  {}".format(len(route)))
print ("maximum generated :  {}".format(g))
print ("maximum expanded :  {}".format(e))
if(List[3]=='infinity'):
	print ("Distance :  infinity")
	print ("ROUTE:")
	print("None")
else:	
	print ("Distance :  {} kms".format(float(List[3])))
	print ("ROUTE:")
	print_route(route,start,goal)
print("\n\n")
