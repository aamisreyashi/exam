import matplotlib.pyplot as plt
fig,axes=plt.subplots(nrows=2,ncols=2)
x=[i for i in range (0,11)]
y=[i**2 for i in x]
z=[i**3 for i in x]
b=[i**4 for i in x]
a=[i for i in x]
axes[0,0].plot(x,a,label='y=x')
axes[0,0].legend()
axes[0,0].set_title('Plot of y = x')
axes[1,1].plot(x,b,label='y=x^4')
axes[1,1].legend()
axes[1,1].set_title('Plot of y = x^4')
axes[0,1].plot(x,y,label='y=x^2')
axes[0,1].legend()
axes[0,1].set_title('Plot of y = x^2')
axes[1,0].plot(x,z,label='y=x^3')
axes[1,0].legend()
axes[1,0].set_title('Plot of y = x^3')
plt.show()