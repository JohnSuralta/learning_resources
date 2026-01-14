import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
plt.scatter(x_values, y_values, s=5) # plot the point (2, 4) with a dot size of 200

# ax.plot(x_values, y_values, linewidth=3)

# Labels
ax.set_title("Squared Function", fontsize=36)
ax.set_ylabel("X Value Squared", fontsize=18)
ax.set_xlabel("X Value", fontsize=18)

# tick size and tick style
ax.ticklabel_format(style="plain")
ax.tick_params(labelsize=14)


plt.show()
