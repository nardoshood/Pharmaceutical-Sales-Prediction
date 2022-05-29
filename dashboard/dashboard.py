import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import re
from wordcloud import WordCloud, STOPWORDS
import plotly.express as px
from utils import (remove_mentions,
remove_hashtags,
remove_unfinished_letters,
remove_RT)

st.title(' Pharmaceutical Sales prediction ')
