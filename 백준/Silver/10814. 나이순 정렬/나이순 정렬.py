import sys

N = int(sys.stdin.readline())
people = []
for i in range(N):
    age, name = (map(str, sys.stdin.readline().split()))
    age = int(age)
    people.append([age, name])

people = sorted(people, key= lambda x: x[0])    
for j in range(0, len(people)):
    print(people[j][0], people[j][1])

