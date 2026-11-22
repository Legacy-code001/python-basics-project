import pandas as pd 
import numpy as np 

df1 = pd.DataFrame({
    "grade_1": [90, 78, 89],
    "grade_2": [78,90,93]
})

df2 = pd.DataFrame({
    "grade_1": [93, 72, 81],
    "grade_2": [98,80,83]
})
df3 = pd.DataFrame({
    "grade_1": ["first", "second", "third"],
    "pyscics": [98,80,83]
}, index=[0,1, 2])
df4 = pd.DataFrame({
    "grade_1": [ "second", "first"],
    "Chemistry": [68,80]
}, index=[1, 0])

# df_concat = pd.concat([df1, df2], keys=["junior", "senior"])
df_concat = pd.concat([df1, df2], ignore_index=True)
print(df_concat)

df_concat_r = pd.concat([df3, df4], axis=1)
print(df_concat_r)


df5 = pd.DataFrame({
    "grade_1": ["first", "second", "third"],
    "pyscics": [98,80,83]
})
df6 = pd.DataFrame({
    "grade_1": [ "second", "first"],
    "Chemistry": [68,80]
})
# df_merge = pd.merge(df3, df4, on="grade_1")
# print(df_merge)

# df_merge = pd.merge(df3, df4, on="grade_1", how='inner')
# print(df_merge)

# df_merge = pd.merge(df3, df4, on="grade_1", how='left')
# print(df_merge)

# df_merge = pd.merge(df3, df4, on="grade_1", how='right')
# print(df_merge)

df_merge = pd.merge(df3, df4, on="grade_1", how='outer')
print(df_merge)