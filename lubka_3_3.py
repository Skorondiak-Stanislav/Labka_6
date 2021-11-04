"""
Знайти вектор c=2(a+c)-3(a-b) ,де a,b,c є R**n
"""
# позначення
"""
n- кількість вимірів
a,b,c- вектори
v - результат
"""
# введення
v = []
n = int(input('n='))
a = [float(input('Введіть координату вектора а {0} :'.format(i))) for i in range(1, n + 1)]
b = [float(input('Введіть координату вектора b {0} :'.format(o))) for o in range(1, n + 1)]
c = [float(input('Введіть координату вектора c {0} :'.format(p))) for p in range(1, n + 1)]
for i in range(n):
    c[i] = 2*(a[i] + c[i]) - 3*(a[i]-b[i])
    v.append(c[i])
print('c={0}'.format(v))