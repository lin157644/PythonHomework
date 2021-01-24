from sympy import *

var("x y")

# x*3+y*7-x*9+y*5

# 展開
# print(latex(expand((x+y)**5)))
# 合併
# factor(x**2+2*x*y+y**2)
# 代入
# ((x+1)**3).subs(x,5)
# 極限
# limit( (x**2-1)/(x+1), x, -1)
# limit( (x**3-4)/(2*abs(x)**3+2), x, -oo)

# 微分
# f= x**3 + 2*x**2 + 1
# diff(f, x, 2)

# 不定積分 對x做不定積分 +記得+C
# print(integrate(3*x**5 + 3*x + 5, x))

# 定積分 重積分就在多一個括號
# integrate(x**2 + 3*x + 5, (x, 0, 10))

print(limit( 100*(1-(1-99/100)**x), x, oo))