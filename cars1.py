from vega_datasets import data
df_cars = data.cars()

import altair as alt

df_cars.columns

interval = alt.selection_interval()

chart1 = alt.Chart(df_cars).mark_point().encode(
    x = 'Horsepower',
    y = 'Miles_per_Gallon',
    color = alt.condition(interval, 'Origin', alt.value('lightgrey')),
    tooltip = ['Name', 'Horsepower', 'Miles_per_Gallon', 'Origin']
).add_params(interval)
chart1

## podemos observar que entre mayor la potencia, menor es la cantidad de millas por galón

hist = alt.Chart(df_cars).mark_bar().encode(
    x = alt.X('Weight_in_lbs', bin = alt.Bin(maxbins=20)),
    y = 'count()')

mean = alt.Chart(df_cars).mark_rule(color='red', size=2).encode(
    x = 'mean(Weight_in_lbs)'
)

# Superponer ambas capas
chart2 = alt.layer(hist, mean).facet('Origin')
chart2

chart2.to_dict()