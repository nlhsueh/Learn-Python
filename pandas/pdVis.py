import pandas as pd
import matplotlib.pyplot as plt # for saving fig
fig = plt.figure()

# Series
fruit = ['A', 'B', 'C', 'D']
quantity = [90, 87, 23, 45]
s = pd.Series(quantity, index = fruit)
s.plot(231)
fig.savefig('images/seriesPlot.png')

# DataFrame
f = {"name": ['A', 'B', 'C', 'D'],
      "price": [10, 12, 20, 30],
      "quantity": [90, 87, 23, 45],
      }

ff = pd.DataFrame(f, index = f['name'])
ff.plot()
fig.savefig('images/dfPlot.png')

# Using Twin Axes
fig, ax = plt.subplots()
fig.suptitle("Fruit price and quantity")
ax.set_ylabel("Price")
ax.set_xlabel("Fruit")
ax2 = ax.twinx()
ax2.set_ylabel("Quantity")

ff["price"].plot(ax=ax, style="b-", use_index=True, rot=90)
ff["quantity"].plot(ax=ax2, style="g-", use_index=True, rot=90)
fig.savefig('images/twin.png')

# Multiple Y Axes
fig, ax = plt.subplots()
fig.suptitle("Fruit price and quantity")
ax.set_ylabel("Price")
ax.set_xlabel("Fruit")

ff["total"] = ff["price"] * ff["quantity"]
ax_quantity, ax_total = ax.twinx(), ax.twinx() 
ax_quantity.set_ylabel("Quantity")
ax_total.set_ylabel("Total")
rspine = ax_total.spines['right']
rspine.set_position(('axes', 1.25))
ax_total.set_frame_on(True)
ax_total.patch.set_visible(False)
fig.subplots_adjust(right=0.75)

ff["price"].plot(ax=ax, style="b-", use_index=True, rot=90)
ff["quantity"].plot(ax=ax2, style="g-", use_index=True, rot=90)
ff["total"].plot(ax=ax_total, style="r-", use_index=True, rot=90)
fig.savefig('images/d.png')