# K-Pop Sonic Evolution: A Spotify Data Analysis

![Project Banner](https://user-images.githubusercontent.com/93233240/143892209-e4328d9e-5d35-47b0-b3e3-f641c7a46268.gif)

## Introduction
This project analyzes the sonic evolution of Korean Popular Music (K-Pop) over the last three decades. By segmenting the genre into four distinct chronological "generations," this analysis aims to objectively quantify stylistic shifts using audio features derived from the Spotify Web API. The goal is to determine if statistical differences exist between eras, moving beyond subjective observation to data-driven insights.

## Technologies & Resources
*   **Python 3.8+**: Used for data extraction and exploratory analysis.
    *   Libraries: `pandas`, `matplotlib`, `seaborn`, `spotipy`
*   **R 4.0+**: Used for advanced visualizations (Chord Diagrams).
    *   Libraries: `tidyverse`, `circlize`, `viridis`
*   **Data Source**: [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

## Context: The Four Generations
To categorize the data, artists were grouped into the industry-standard "Generations," which mark significant shifts in marketing, sound, and global reach.

*   **1st Gen (1996–2004):** The establishment of the modern "idol" system.
    *   *Rep. Artists:* H.O.T, S.E.S, Shinhwa.
*   **2nd Gen (2005–2012):** The era of initial international expansion.
    *   *Rep. Artists:* Big Bang, Girls' Generation, SHINee, 2NE1.
*   **3rd Gen (2013–2018):** Mainstream global success and digital proliferation.
    *   *Rep. Artists:* BTS, EXO, TWICE, BLACKPINK.
*   **4th Gen (2019–Present):** The current era of digital-native groups.
    *   *Rep. Artists:* Stray Kids, ITZY, aespa, ATEEZ.

## Methodology

### 1. Data Extraction
Using the `Spotipy` wrapper, discography data was extracted for a curated list of representative artists from each generation. The dataset comprises approximately **17,000 songs**.
*   **Scope:** Albums, EPs, and Singles.
*   **Filtering:** To ensure data consistency, the following were excluded:
    *   Duplicates and Re-releases
    *   Remixes and Instrumentals
    *   Japanese and Chinese language releases (to focus on the primary market sound)

### 2. Feature Engineering
For every track, the following Audio Features were retrieved via the Spotify API:
*   **Rhythmic:** Tempo, Time Signature, Danceability
*   **Tonal:** Key, Mode, Valence (musical positiveness)
*   **Sonic:** Loudness, Energy, Acousticness, Instrumentalness

### 3. Exploratory Analysis
A correlation matrix was generated to identify relationships between audio variables across the entire dataset.

**Key Findings:**
*   **Tempo:** 4th Generation tracks display the highest average tempo, while 1st Generation tracks are the slowest.
*   **Duration:** There is a clear, statistically significant downward trend in song length over time, correlating with the rise of streaming.
*   **Correlations:** Strong positive correlations were observed between **Energy/Loudness** and **Valence/Danceability**, consistent with the genre's focus on performance.

## Visualizations

### Correlation Heatmap
An analysis of how audio features interact within the genre.
![Heat Map](https://user-images.githubusercontent.com/93233240/145100365-775da3e4-1173-4370-8c96-876a3d02b472.png)

### Feature Chord Diagram
Generated using R (`circlize`), this diagram visualizes the strongest correlations between the 13 distinct audio features, providing a graphical representation of the "K-Pop Sound."
![Chord Diagrams](https://github.com/RachaelKilonzo/Music-Evolution/blob/main/chord_diagram.png)

## Future Work
*   **Cluster Analysis:** Implement K-Means clustering or PCA to group songs by sonic similarity rather than release year.
*   **Popularity Metrics:** Integrate Spotify popularity scores to analyze which audio features correlate with commercial success.
*   **Comparative Analysis:** Compare these K-Pop metrics against Western Pop datasets to identify genre-specific sonic signatures.
