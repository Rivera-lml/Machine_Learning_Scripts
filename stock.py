df_stocks = data.stocks()
print(df_stocks.head(), df_stocks.symbol.unique(), df_stocks.min(), df_stocks.max(), sep = '\n\n')

chart1 = alt.Chart(df_stocks).mark_line().encode(
    x = 'date:T', y = 'price:Q', color = 'symbol').transform_filter("datum.symbol == 'MSFT' ").properties(width = 200, height = 200)

df_stocks_msft = df_stocks.query("symbol == 'MSFT' ")

chart2 = alt.Chart(df_stocks_msft).mark_line().encode(
    x = 'date:T', y = 'price:Q', color = 'symbol').properties(width = 200, height = 200)

chart3 = alt.Chart(df_stocks_msft).mark_line().encode(
    x = 'date:T', y = alt.Y('price:Q', scale = alt.Scale(type='log')), color = 'symbol').properties(width = 200, height = 200)

chart1 | chart2 | chart3