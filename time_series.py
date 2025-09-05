## series de tiempo

df_cars = data.cars()
df_cars.head()

chart = alt.Chart(df_cars).mark_area(opacity = 0.3).encode(
    x = alt.X('Year', timeUnit='year'), 
    y  = alt.Y('ci0(Miles_per_Gallon)', axis = alt.Axis(title='Miles_per_Gallon')), 
    y2  = 'ci1(Miles_per_Gallon)',
    color = 'Origin')
chart