pkg('load', 'symbolic')
syms t
disp('Chon chieu duong huong len')
disp('Goc toa do tai mat dat');
disp('Phuong trinh dinh luat II Newton cho ten lua');
disp('m*dv/dt = -v0*dm/dt - mg');
k=input('Nhap toc do dot nhien lieu dm/dt = ');
m0=input('Nhap khoi luong ban dau cua ten lua m0 = ');
y0=input('Nhap vi tri ban dau cua ten lua y0 = ');
v0=input('Nhap van toc day khi cua ten lua v0 = ');
g=-9.81;
v=v0*log(m0/(m0+k*t))-g*t;
t1=m0/abs(k);
disp('Gia toc cua ten lua a=');
a=diff(v,1);
disp(a);
disp('Phuong trinh chuyen dong ten lua y = ');
y=y0+int(v, 0, t);
disp(y);
disp('Ten lua het nhien lieu tai thoi diem t=');
disp(t1);
yFinal = limit(y,t,t1,'left');
if yFinal >= 120000
  disp('Tai thoi diem nay ten lua da ra ngoai vu tru va khong con chuyen dong');
else
  disp('Tai thoi diem nay ten lua chua ra ngoai vu tru');
end
xFunc = linspace(0, t1);
yFunc = matlabFunction(y)(xFunc);
plot(xFunc, yFunc);
title('Do thi bieu dien phuong trinh chuyen dong cua ten lua');
xlabel('Thoi gian t');
ylabel('Vi tri y');
grid on;
