import streamlit as st
import plotly.express as px
from utils import *

# --- Config ---
st.set_page_config(page_title="Netflix Dashboard", layout="wide")

# --- Load data ---
df = load_data("data/netflix-titles.csv")

st.title("📊 Netflix Dashboard")

# =============================
# 🔹 Top Directores
# =============================
top_directors = get_top_directors(df)

fig1 = px.bar(
    x=top_directors.values,
    y=top_directors.index,
    orientation='h',
    title="Top 10 Directores con más títulos"
)

st.plotly_chart(fig1, use_container_width=True)

# =============================
# 🔹 Series vs Películas
# =============================
type_counts = get_type_counts(df)

fig2 = px.pie(
    names=type_counts.index,
    values=type_counts.values,
    title="Series vs Películas"
)

st.plotly_chart(fig2, use_container_width=True)

# =============================
# 🔹 Top Categorías
# =============================
top_categories = get_top_categories(df)

cats = [x[0] for x in top_categories]
values = [x[1] for x in top_categories]

fig3 = px.bar(
    x=values,
    y=cats,
    orientation='h',
    title="Top 5 Categorías (listed_in)"
)

st.plotly_chart(fig3, use_container_width=True)