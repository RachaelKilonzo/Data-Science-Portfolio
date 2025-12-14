# Spotify Music Data Analysis
![0_fjF0J_aXhcvIdGBH](https://user-images.githubusercontent.com/93233240/143892209-e4328d9e-5d35-47b0-b3e3-f641c7a46268.gif)


##
## INTRODUCTION
A heated arguement one evening with a couple of friends who share the same taste of kpop as a music genre inspired this simple short project. The arguement was on the evolution on the genre over the years, differences in generations (I'll soon get to that for any kpop noobs), the faux nostalgia and perhaps condescending attitude that earlier listeners tend to exhihibit for newer generations' sounds.

##
## Resources Used
- Jupyter Notebook Version 6.3.0
- Python libraries used: matplotlib, pandas, spotipy
- Spotify Web API: https://developer.spotify.com/documentation/web-api/
- Rstudio version 1.4.1717
- Rstudio libraries used: tidyverse, viridisLite, viridis, patchwork, hrbrthemes, circlize, chorddiag

##
## What is Kpop?
Korean popular music, abbreviated as K-pop or Kpop is mainstream music that originates from South Korea. It includes many different musical elements and genres under its umbrella unlike what pop music is viewed as in western markets of the Americas and Europe . Along with Korean pop, it includes Korean rock music, hip hop, and electronic music. It is a fairly new form of music, particularly formed around the 1990s. Interestingly, contemporary Kpop is a genre whose origins can definively be pointed to a certain date: 11th April 1992 when Seo Taiji and Boys performed their music on TV for the first time and changed the country's music scene. From ballads and trot to this unique amalgamation of music sounds.

##
## Distinctive features of K-pop?
1. Different genres used to create different K-pop music concepts.
2. Choreographies that rely on hard-hitting, synchronized movements, with members switching positions multiple times in a routine: “formation changing” . The movements are repetitive and addicting to look.

##
## Kpop Generations
![pie charts](https://user-images.githubusercontent.com/93233240/145102471-ac9602f8-37d6-4def-9a53-b5ecf9cc5514.png)
### First Generation
Years: 1996-2004
The first generation began after disbanded and retired. In 1996, SM Entertainment, inspired by Seo Taiji and Boys, American boy bands, and Japanese idol production decided to create the first K-pop idol group, H.O.T. After, groups such as Sechs Kies, g.o.d, Shinhwa, S.E.S, Fin.K.L, and Baby V.O.X were created among others.
### Second Generation
Years: 2005-2012
Popular Artists: TVXQ, Super Junior, Big Bang, SS501, SHINee, 2PM, Girls' Generation, Wonder Girls, KARA, BEAST (now Highlight), Infinite, MBLAQ, B1A4, 2NE1, 4Minute, T-ara, f(x), Secret, Miss A, Apink, Girl's Day, Sistar.
The transition from the first generation to the second generation was very distinct as towards the end of the generation, most of it's idols had retired and left the music scene in its entirety.
### Third Generation
Years: 2013-2017
Popular Artists: BTS, EXO, Seventeen, NU'EST, VIXX, GOT7, WINNER, iKON, MONSTA X, NCT, BLACKPINK, TWICE, Red Velvet, AOA, EXID, Mamamoo, Lovelyz, GFRIEND, OH MY GIRL, WJSN.
The transition between the second and third generations wasn't as distinct as the first and second generations because the second generation idols were active during this period.
### Fourth Generation
Years: 2019-Present
Popular Artists: TOMORROW X TOMORROW, TREASURE, ENHYPEN, Stray Kids, ATEEZ, The Boyz, Verivery, ITZY, aespa, (G)I-DLE, STAYC, NiziU, Everglow
There is the suggestion that says that the fourth generation idols are yet to come because third-generation idols are still at the top. However, since the K-pop idol industry is very saturated, it seems that the current third-generation idols at the top today won't be changing any time soon. And there's an undeniable difference between these groups and third generation ones whether it be soundwise or performancewise.

##
## Data Collection and cleaning
I extracted data from Spotify's Web API using artists names ot their uri/url to get musical characteristics of about 17000 songs of a list of artists' discographies while exluding the chinese and japanese versions plus instrumentation of title tracks. For each artist, I extracted their albums, EPs and singles and removing repeated albums and songs, duplicate songs and versions of the same song. The characteristics derived were: 
- Name
- Album
- Track ID
- Acousticness
- Danceability
- Duration
- Energy
- Instrumentalness
- Key
- Liveness
- Loudness
- Mode
- Speechiness
- Tempo
- Time Signature
- Valence
- uri 

##
## Exploratory Analysis
I tried to look at the correlation between various variables as well as relationships between variables to gain some overall insights of what the genre is like. 

![Heat Map](https://user-images.githubusercontent.com/93233240/145100365-775da3e4-1173-4370-8c96-876a3d02b472.png)

High positive correlation exists between: 
- Danceablity & Valence 
- Danceability & Loudness 
- Energy & Loudness 
- Energy & Valence 
- Loudness & Valence 
- Energy & Liveness
Of these 6 pairings, their scatter plots across generation are: 
![scatter plots](https://user-images.githubusercontent.com/93233240/145101043-4ae79bf9-7150-446f-8448-72d8b4a3cda9.png)


With more visualizations and description to be found in the Jupyter Notebook.

## 
## Chord Diagrams
I always wanted to learn how to plot chord diagrams and managed to do so for the feature analysis of the characteristics. So here is a chord diagram based on the correlation matrix of the 13 features of the songs.
![Chord Diagrams](https://github.com/RachaelKilonzo/Music-Evolution/blob/main/chord_diagram.png)

##
## Needs more work
- Try to do cluster Analysis and Pca
- Add Artist names and popularity characteristics and see what you may learn
- Comparative analysis of the features with western music.

