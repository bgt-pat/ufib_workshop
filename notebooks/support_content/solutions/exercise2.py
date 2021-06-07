x = np.arange(-10,15,0.1)

g1 = gauss(x,2,4)
g2 = gauss(x,4,1)

plt.plot(x,g1,'-',label=r"$\mu = 2,\sigma^2 = 4$")
plt.plot(x,g2,'--',label=r"$\mu = 4,\sigma^2 = 1$")
plt.xlabel("x",fontsize=14)
plt.ylabel("p(x)",fontsize=14)
plt.legend(fontsize=14)
plt.show()