
# 🎬 Movie Recommendation System

A simple command-line based **popularity-based movie recommender** using the [MovieLens dataset](https://grouplens.org/datasets/movielens/).

This project filters movies by genre and recommends the highest-rated ones with enough user ratings.

---

## 📂 Project Structure

```
.
├── movies.py                  # Main script for the recommendation system
├── movies.csv                 # Movie metadata including titles and genres
├── ratings.csv                # User ratings of movies
├── screenshots of the output/ # Folder with screenshots (optional)
```

---

## 🚀 How It Works

1. **Merges** movie metadata (`movies.csv`) with ratings (`ratings.csv`)
2. **Filters** movies by genre (e.g., Action, Comedy, etc.)
3. **Applies rating threshold** to ignore rarely rated movies
4. **Calculates average rating** and shows top N movies

---

## 📥 Requirements

- Python 3.x
- pandas

Install dependencies:

```bash
pip install pandas
```

---

## ▶️ Usage

Run the recommender:

```bash
python movies.py
```

Then enter:
- A genre from the list shown (e.g., `Comedy`, `Action`)
- Minimum number of ratings (e.g., `50`)
- Number of top recommendations to return (e.g., `10`)

---

## 📸 Sample Output

```bash
Available genres:
Action, Adventure, Animation, Biography, Comedy, ...

Enter the genre: Comedy
Enter the minimum ratings threshold: 50
Enter the number of recommendations: 5

Top 5 movies in the genre 'Comedy':
1. Life Is Beautiful (1997) - 4.53
2. The Big Lebowski (1998) - 4.47
...
```

---

## 📌 Notes

- Movies with no genres listed are excluded
- Genre filtering is case-sensitive (e.g., enter `Comedy`, not `comedy`)
- Output is printed to console, but can be exported to CSV if desired

---

## 🛠 Future Ideas

- Content-based filtering using TF-IDF or cosine similarity
- Convert to a web app with Flask or Streamlit
- Dockerize the app
