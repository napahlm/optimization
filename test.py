from scipy.optimize import linprog

# LP Prob. 1

c = [-30, -50]
A = [[-1,0],[0,-1],[1,1],[1,3]]
b = [-20,-10,100,200]
x1_b = (0,None)
x2_b = (0,None)

res = linprog(c, A_ub=A, b_ub=b, method="revised simplex")
print(res)