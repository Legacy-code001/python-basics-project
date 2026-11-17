from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


df_sales_detail = pd.read_excel("linechart.xlsx")
print(df_sales_detail)

# plt.figure(figsize=(12, 5))
# plt.plot(df_sales_detail["Quarter"], df_sales_detail["Fridge"], color="blue", label="Fridge")
# plt.plot(df_sales_detail["Quarter"], df_sales_detail["Dishwasher"], color="green", label="Dishwasher")
# plt.plot(df_sales_detail["Quarter"], df_sales_detail["Washing Machine"], color="red", label="Washing Machine")

# plt.title("Product Sales")
# plt.xlabel("Quarter")
# plt.ylabel("Million $")

# plt.legend()
# plt.show()


# total_sales = df_sales_detail[["Fridge", "Dishwasher", "Washing Machine"]].sum()
# print(total_sales)
# print(total_sales.index)

# plt.pie(total_sales, labels=total_sales.index, autopct="%1.1f%%", shadow=True, explode=(0.1, 0, 0), startangle=120)
# plt.axis("equal")
# plt.show()

#Bar Chart
# df_sales_detail.plot(kind="bar", x="Quarter" )
#index is set
# df_sales_title = df_sales_detail.set_index("Quarter")
# df_sales_title.plot(kind="bar")

#
# df_sales_title.plot(kind="barh")
# plt.xticks(rotation=45, ha="right")
plt.xticks(rotation=45) # rotates the text labels along the horizontal x-axis by 45 degrees counter-clockwise
#ha adding horizontal alignment (ha="right") lines up the end of each tilted label directly beneath its tick mark on the axis.

# plt.show()

#histogram
df_score = pd.read_excel("histograms.xlsx")
# print(df_score)
# plt.hist(df_score["Exam_Score"], density=True)

# plt.show()

# for histoogram, seaborn has special visual appeal and it is easier to use
# kernal density estimator


# Plot normalized histogram (total area = 1)
# plt.hist(df_score["Exam score"], bins=10, density=True, alpha=0.6, edgecolor="black")

# # Overlay a smooth density curve (KDE) on the same scale
# sns.kdeplot(df_score["Exam score"], color="red")

# plt.xlabel("Exam Score")
# plt.ylabel("Density")
# plt.title("Normalized Exam Score Distribution")
# plt.show()

# sns.histplot(df_score["Exam_Score"], kde=True)
# sns.histplot(df_score, x="Exam_Score", kde=True)

# plt.xlabel("score")
# plt.ylabel("count")
# plt.title("title")
# plt.show()

"""

"""
df_scatter_plot = pd.read_excel("scatter_plot.xlsx")
print(df_scatter_plot.head(3))
sns.scatterplot(df_scatter_plot, x="area_square_ft", y="price" )
plt.show()

# matplotliv abd seaborn are two majour library widly use for visualization, they are use interchangeably,
