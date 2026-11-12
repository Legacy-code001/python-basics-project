import csv

import pandas as pd


# def checks(data, industry=None):
#     ratings = []

#     for row in data:
#         if row[3] != 'NULL' and (not industry or row[1] == industry):
#             ratings.append(float(row[3]))

#     maximum = max(ratings)
#     minimum = min(ratings)
#     avg = sum(ratings)/len(ratings)
#     return maximum, minimum, avg



# with open("movies.csv") as f:
    
#     read_output = list(csv.reader(f))
#     print(read_output)
#     header = read_output[0]
#     data = read_output[1:]

#     min_val, max_val, avg_val = checks(data)
#     print(f"print all records: Min_rating{min_val}, Max_rating{max_val}, the avg: {avg_val}")
#     min_val, max_val, avg_val = checks(data, industry="Bollywood")
#     print(f"Bollywood: Min_rating: {min_val}, Max_rating: {max_val}, the avg: {avg_val}")
        

df = pd.read_csv("movies.csv")
# print(df)

print(df.head(3))
# print(df.tail(3))
# print(df.sample(3))
# print(df[3 : 5])
# print(df.shape)
# print(df[df.industry == "Hollywood" ])
# hollywood = df[df.industry == "Hollywood" ]
# print(df.imdb_rating.max())
# print(df[df.industry == "Hollywood" ].imdb_rating.max())
print(df.columns)
print(df.industry.unique())
print(df['language'].unique())
# print(df(df['industry'] == "Bollywood").size)
#count each available language
print(df.language.value_counts())

#filtering specific column
# print(df[["title", "industry", "imdb_rating"]])
# print(df[(df.release_year > 2000) & (df.release_year < 2010)])
# print(df[df.studio == "Marvel Studios"])

#getting statistics of the numerical column
print(df.describe())

#it gives us infor about the index no, the theading  the num of non -null and the data type
print(df.info())

# fetch out detail of max rating
print(df[df.imdb_rating == df.imdb_rating.max()])
# df["age"] = df['release_year'].apply(lambda x: 2023 - x)
# print(df.head(4))
# df["profit"] = df.apply(lambda x: x['revenue'] - x['budget'], axis=1)

# print(df.head(3))
#the title' first column headimh
print(df.index)
# df['title'] = df['title'].astype(str).str.strip()
df = df.set_index('title')
print(df)
#print the column of the table column description based on the title 
# print(df.loc['Pather Panchali'])

# #we can get for multiple too
print(df.loc[['Pather Panchali', 'Doctor Strange in the Multiverse of Madness']])
# print(dir(df))
#like the heading
print(df.columns)

#integer based location
print(df.iloc[:2])
print(df.reset_index().head(3))
# print(df.head(3))
