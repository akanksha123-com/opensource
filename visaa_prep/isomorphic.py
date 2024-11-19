def isIsomorphic(s, t): return len(s) == len(t) and len(set(zip(s, t))) == len(set(s)) == len(set(t))



n = int(input())

s = input() 

t = input() 

print("true" if isIsomorphic(s, t) else "false")
