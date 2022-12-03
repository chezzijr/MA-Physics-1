import sympy as sp

# Get all the required inputs
k = float(input('Nhap toc do dot nhien lieu dm/dt: '))
m0 = float(input('Nhap khoi luong ban dau cua ten lua m0: '))
y0 = float(input('Nhap vi tri ban dau cua ten lua y0: '))
v0 = float(input('Nhap van toc day khi cua ten lua v0: '))

# Define t as a symbolic variable
t = sp.Symbol('t', positive=True, real=True)

# Gravitational acceleration is negative as the axis's direction is upward
g = -9.81

# Define v(t)
v = v0 * sp.ln(m0 / (m0 + k * t)) - g * t

# The moment when m(t) = 0
t1 = m0/abs(k)

# Acceleration is the derivative of velocity with respect to time
# coordinate y is the integral of velocity with respect to time
a = sp.diff(v, t)
y = y0 + sp.integrate(v, (t, 0, t))

# Find the coordinate y the moment before going out of fuel when m = 0
yFinal = sp.limit(y, t, t1, '-')
yFinal = yFinal.evalf(6)

# Output
print('Phuong trinh gia toc:', a)
print('Phuong trinh van toc:', v)
print('Phuong trinh toa do:', y)
print('Ten lua het nhien lieu tai thoi diem:', t1)
print('Tai thoi diem do, toa do cua ten lua:', yFinal)

# Plot the coordinate according to time
sp.plot(
    y,
    (t, 0, t1),
    title='Do thi bieu dien phuong trinh chuyen dong cua ten lua',
    xlabel='Thoi gian t',
    ylabel='Vi tri y',
)
