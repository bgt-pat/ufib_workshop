x = np.arange(0,2*np.pi,0.2)

plt.plot(x,np.cos(x),'o-',label="cos(x)")
plt.plot(x,np.sin(x),'--',label="sin(x)") # this line is new!
plt.xlabel("x",fontsize=16)
plt.ylabel("y",fontsize=16)
plt.legend(fontsize=16)
plt.show()