from vega_datasets import data
df_iris = data.iris()


import altair as alt

interval = alt.selection_interval()

chart1 = alt.Chart(df_iris).mark_point().encode(
    x = 'petalLength',
    y = 'sepalLength',
    color = alt.condition(interval, 'species', alt.value('lightgrey')),
    tooltip = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species']
).add_params(interval)
chart1

hist = alt.Chart(df_iris).mark_bar().encode(
    x = alt.X('petalWidth', bin = alt.Bin(maxbins=20)),
    y = 'count()')

mean = alt.Chart(df_iris).mark_rule(color='red', size=2).encode(
    x = 'mean(petalWidth)'
)

# Superponer ambas capas
chart2 = alt.layer(hist, mean).facet('species')
chart2