# Netflix Dashboard

Small data viz exercise: load the public Netflix titles dataset and chart a few things about it with Plotly inside a Streamlit app — top directors by title count, series vs. movies split, and the top content categories.

## Stack

Python, pandas for the data wrangling, Plotly for the charts, Streamlit for the app shell.

## Running it

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Scope

This is a practice project, not a production dashboard — one data source, three static charts, no filters or interactivity beyond what Streamlit gives you for free. `app/utils.py` has the actual data-shaping functions (`get_top_directors`, `get_type_counts`, `get_top_categories`) if you want to see how the aggregations work.

## Data

`data/netflix-titles.csv` is the "Netflix Movies and TV Shows" dataset by Shivam Bansal on Kaggle (https://www.kaggle.com/datasets/shivamb/netflix-shows), the 2019 snapshot. It's included only so the app runs out of the box; the dataset keeps its own license on Kaggle, and the MIT license in this repo covers my code, not the data. Netflix is a trademark of Netflix, Inc.; this project isn't affiliated with it.
