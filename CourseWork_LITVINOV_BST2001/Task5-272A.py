
friend=int(input())
claws=sum(map(int,input().split()))
print(sum((claws+i)%(friend+1)!=1 for i in range(1,6)))