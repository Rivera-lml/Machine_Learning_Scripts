import altair as alt
from vega_datasets import data

df_cars = data.cars()

chart = alt.Chart(df_cars).mark_circle(size=60).encode(
    x = 'Horsepower',
    y = 'Miles_per_Gallon',
    color = 'Origin',
    tooltip = ['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

chart