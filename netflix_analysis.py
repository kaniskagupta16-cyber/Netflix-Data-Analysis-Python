import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Title     Type     Genre  Release Year Rating   Duration      Country
df = pd.read_excel(r"D:\Excel\netflix_big_dataset.xlsx")
#print(df)

#Bar plot
data = df.dropna(subset=["Title", "Type", "Genre", "Release Year", "Rating", "Duration"])
types_count = df["Type"].value_counts()
plt.figure(figsize=(6,4), facecolor='lightblue')
plt.gca().set_facecolor('white')
plt.bar(types_count.index, types_count.values, color=["blue","red"],label=["Count Of Movie","Count of TVshow"])
plt.xlabel("Types",fontsize="12")
plt.ylabel("Count",fontsize="12")

plt.legend(loc="upper right")
plt.title("Number of Movies and TV Shows on Netflix")
plt.show()

#Pie plot
rating_count = df["Rating"].value_counts()
plt.figure(figsize=(6,4), facecolor='lightblue')
plt.gca().set_facecolor('white')
plt.pie(rating_count, labels=rating_count.index, autopct="%1.1f%%",startangle=90,
explode = (0, 0.1, 0, 0),shadow=True, wedgeprops={'edgecolor':'black'})
plt.title("Number of Tvshow and Movie on netflix")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

#Histogram
movie_df = df[df['Type'] == 'Movie'].copy()
movie_df['duration_int'] = (
    movie_df['Duration']
    .str.replace(' min', '', regex=False)
    .str.strip()
)
movie_df = movie_df[movie_df['duration_int'].str.isnumeric()]
movie_df['duration_int'] = movie_df['duration_int'].astype(int)
plt.figure(figsize=(6,4), facecolor='lightblue')
plt.gca().set_facecolor('white')
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black',label="Movie")
plt.title('Distribution of Movie Duration')
plt.xlabel("Duration (minutes)",fontsize="12")
plt.ylabel("Number of Movies",fontsize="12")
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()

#Scatter plot
release_count = df['Release Year'].dropna().astype(int).value_counts().sort_index()
plt.figure(figsize=(6,4), facecolor='lightblue')
plt.gca().set_facecolor('white')
plt.scatter(release_count.index, release_count.values,color='blue',label="Shows")
plt.title("Relese year vs Number of Shows")
plt.xlabel("Release Year",fontsize="12")
plt.ylabel("Number of shows",fontsize="12")
plt.grid(True)
plt.legend(loc="upper right")

plt.tight_layout()
plt.show()

#Hbar
contnent_by_year = df.groupby(['Release Year','Type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5), facecolor='lightblue')
ax[0].set_facecolor('white')
ax[1].set_facecolor('white')


#first subplot movie
ax[0].plot(contnent_by_year.index,contnent_by_year['Movie'],color='blue',label="Movie",marker="*",linewidth="2",linestyle=":")
ax[0].set_title("Movie show releted Per Year")
ax[0].set_xlabel("Year",fontsize="12")
ax[0].legend()
ax[0].set_ylabel("Numbers of Movie",fontsize="12")

#second subplot tvshow
ax[1].plot(contnent_by_year.index,contnent_by_year['TV Show'],color='red',label="TV Show",marker="o",linewidth=2)
ax[1].set_title("TV Shows releted Per Year")
ax[1].set_xlabel("Year",fontsize="12")
ax[1].legend()
ax[1].set_ylabel("Numbers of TV Show",fontsize="12")

fig.suptitle("Comparison of Movie and TV Show Related Over Years")
plt.tight_layout()
plt.show()









