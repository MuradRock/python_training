

N=int(input('enter number'))


prev=0
curr=1

for i in range(0,N):
   print(prev)
   prev, curr =curr,prev+curr