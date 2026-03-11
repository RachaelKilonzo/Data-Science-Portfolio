# K-Pop Sonic Evolution: A Spotify Data Analysis

![Project Banner](https://user-images.githubusercontent.com/93233240/143892209-e4328d9e-5d35-47b0-b3e3-f641c7a46268.gif)

## Introduction
This project investigates the evolution of Korean Popular Music (K-Pop) over the last three decades. By segmenting the genre into its four distinct chronological "generations," this analysis seeks to objectively quantify stylistic shifts using audio features extracted via the Spotify Web API. The primary objective is to determine if statistical differences exist between eras, moving beyond subjective nostalgia to provide data-driven insights into the genre's changing soundscape.

## Technologies Used
*   **Python 3.8+**: Data extraction and statistical analysis.
    *   *Libraries:* `pandas`, `matplotlib`, `seaborn`, `spotipy`
*   **R 4.0+**: Advanced visualization (Chord Diagrams).
    *   *Libraries:* `tidyverse`, `circlize`, `viridis`
*   **Data Source**: [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

## Context: The Four Generations
To categorize the dataset, artists were grouped into industry-standard "Generations," which mark significant shifts in marketing, production style, and global reach.

*   **1st Gen (1996–2004):** Establishment of the idol system (e.g., H.O.T, S.E.S).
*   **2nd Gen (2005–2012):** International expansion (e.g., Big Bang, Girls' Generation).
*   **3rd Gen (2013–2018):** Global mainstream success (e.g., BTS, TWICE).
*   **4th Gen (2019–Present):** Digital-native era (e.g., Stray Kids, aespa).

## Methodology

### 1. Data Extraction & Cleaning
Using the `Spotipy` wrapper, discography data was extracted for a curated list of representative artists. The final dataset comprises approximately **17,000 songs**.
*   **Scope:** Albums, EPs, and Singles.
*   **Preprocessing:** To ensure sonic consistency, the dataset was filtered to exclude remixes, instrumentals, and non-Korean language releases (Japanese/Chinese versions).

### 2. Feature Engineering
The following Audio Features were retrieved for every track:
*   **Rhythmic:** Tempo, Time Signature, Danceability
*   **Tonal:** Key, Mode, Valence (musical positiveness)
*   **Sonic:** Loudness, Energy, Acousticness, Instrumentalness

---

## Exploratory Data Analysis & Insights

### 1. Generational Trends (Tempo & Duration)
The analysis reveals distinct shifts in song structure over time.
*   **Tempo:** A gradual increase in speed is observed. 4th Generation tracks display the highest average tempo, while 1st Generation tracks are the slowest.
*   **Duration:** There is a statistically significant downward trend in song length. 4th Generation songs are drastically shorter than their predecessors, likely a response to the economics of modern streaming platforms.

![Pie Charts](https://github.com/RachaelKilonzo/Music-Evolution/blob/main/pie.png)

### 2. Feature Correlations
A correlation matrix was generated to identify how audio variables interact within the genre.
*   **Energy vs. Loudness:** A strong positive correlation exists across all generations, consistent with the genre's focus on high-impact production.
*   **Valence vs. Danceability:** As songs become more "danceable" (rhythmically stable), they tend to have higher valence (happier sound), aligning with the industry's focus on upbeat performance tracks.

![Heat Map](https://user-images.githubusercontent.com/93233240/145100365-775da3e4-1173-4370-8c96-876a3d02b472.png)

### 3. Generation Clustering
Scatter plots highlight how specific attributes cluster by generation. The data suggests that while the relationships between features (like Loudness and Energy) remain linear, the density and placement of 4th Gen tracks (yellow) often occupy the extreme ends of the spectrum compared to 1st Gen tracks (green).

![Scatter Plots](https://github.com/RachaelKilonzo/Music-Evolution/blob/main/scatter.png)

### 4. The "K-Pop Sound" (Chord Diagram)
Generated using R (`circlize`), this diagram visualizes the strongest positive correlations between the 13 distinct audio features. The ribbons connect features that frequently co-occur, providing a graphical representation of the formulaic elements that define the modern K-Pop sound.

![Chord Diagrams](https://github.com/RachaelKilonzo/Music-Evolution/blob/main/chord_diagram.png)

---

## Future Work
*   **Cluster Analysis:** Implement K-Means clustering or PCA to identify sub-genres and group songs by sonic similarity rather than release year.
*   **Popularit
