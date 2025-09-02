interval = alt.selection_interval()

base = alt.Chart(df_iris).mark_point().encode(
    y = 'petalLength',
    color = alt.condition(interval, 'species', alt.value('lightgrey'))
).add_params(interval)

hist = alt.Chart(df_iris).mark_bar().encode(
    x = 'count()', y = 'species', color = 'species').properties(
    width = 800, height = 80).transform_filter(interval)

scatter = alt.hconcat(base.encode(x = 'petalWidth'), base.encode(x = 'sepalWidth'))

alt.vconcat(scatter, hist)