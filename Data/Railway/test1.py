x=[1,3,5,7,9,2,6,4,10]
y=[1,2,3,4,5,6,7,8,9]

l=sorted(zip(x,y))

nx,ny=zip(*l)

print(nx,ny)