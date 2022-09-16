
# A simple script to calculate BMI
import pywebio
import plotly.express as px
import pandas as pd
import numpy as np
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table


def page():
    # height = input("Input your height(cm)：", type=FLOAT)
    # weight = input("Input your weight(kg)：", type=FLOAT)

    # BMI = weight / (height / 100) ** 2

    # top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
    #               (25, 'Normal'), (30, 'Overweight'),
    #               (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    # for top, status in top_status:
    #     if BMI <= top:
    #         put_markdown('# **Results**')
    #         put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
    #         put_html('<br><br>')
    #         put_markdown('Your BMI: `%.1f`. Category: `%s`' % (BMI, status))
    #         put_html('<hr>')
    #         put_table([
    #             ['Your BMI', 'Category'],
    #             [BMI, status],
    #         ])

    #         break

    # df = px.data.gapminder().query("country=='Canada'")
    # fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    # html = fig.to_html(include_plotlyjs="require", full_html=False)
    # put_html(html)
    
    # data = dict(
    # character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    # parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    # value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

    # fig =px.sunburst(
    #     data,
    #     names='character',
    #     parents='parent',
    #     values='value',
    #     )

    cols=['distance', 'unknow1', 'unknow2', 'unknow3','times'] 
    df = pd.read_csv('output.csv',names=cols, header=None)
    df['times'] = np.arange(df.shape[0])
    fig = px.line(df, x = 'times', y = "distance", title='Matrix profile of stream flow')
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    put_html(html)
    
if __name__ == '__main__':
    pywebio.start_server(page, port=80) #your local default port is 80