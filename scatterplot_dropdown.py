options = list(df_iris.species.unique())
colors_ = ['steelblue', '#FF8c00', 'FireBrick']
labels = [option + ' ' for option in options]
# dropdown: alt.binding_select   radio: alt.binding_radio
input_dropdown = alt.binding_select( options = options + [None], 
                                     labels = labels + ['All'], name = 'Species: ')
selection = alt.selection_point(fields=['species'], bind = input_dropdown)

chart = alt.Chart(df_iris, 
                  title = alt.Title('Iris dataset',
                                    subtitle = ['Scatterplot: Petal length vs Petal Width'],
                                    anchor = 'start',
                                    orient = 'top',
                                    offset = 14,
                                    fontSize = 20,
                                    subtitleFontSize = 16)).mark_point().encode(

    
    x = alt.X('petalLength:Q', scale = alt.Scale(domain = (1, 7), clamp = True)
             ).axis(title = 'Petal length', titleAngle = 0, titleAlign = 'center'), 
 
    y = alt.X('petalWidth:Q', scale = alt.Scale(domain = (0, 2.6), clamp = True)
             ).axis(title = 'Petal width', titleAngle = 0, titleAlign = 'left', 
                    titleX = -25, titleY = -15),
    color = alt.Color('species:N').scale(domain = options, range = colors_).title(
        'Species by color')).add_params(selection).transform_filter(selection).interactive()

chart