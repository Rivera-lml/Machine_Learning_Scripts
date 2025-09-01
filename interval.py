import altair as alt
from vega_datasets import data
df_iris = data.iris()
df_iris

interval = alt.selection_interval()

base = alt.Chart(df_iris).mark_point().encode(
    y = 'petalWidth',
    color = alt.condition(interval, 'species', alt.value('lightgrey'))
).add_params(interval)
alt.hconcat(base.encode(x = 'petalLength'), base.encode(x = 'sepalLength'))