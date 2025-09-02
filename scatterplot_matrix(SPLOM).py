fields = list(df_iris.iloc[:, 0:4].columns)
interval = alt.selection_interval()
chart = alt.Chart(df_iris).mark_point().encode(
    alt.X(alt.repeat('column'), type = 'quantitative'),
    alt.Y(alt.repeat('row'), type = 'quantitative'),
    color = alt.condition(interval, 'species', alt.value('lightgrey'))
).add_params(interval).properties(width = 200, height = 200).repeat(
        row = fields, column = fields[::-1])
chart