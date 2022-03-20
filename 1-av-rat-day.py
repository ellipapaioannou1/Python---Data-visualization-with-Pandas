import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
df = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
df['Day'] = df['Timestamp'].dt.date
daily_ratings = df.groupby(['Day']).mean()


chart_def = """
 {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
 }
"""

def app():
        wp = jp.QuasarPage()
        h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
        p1 = jp.QDiv(a=wp, text="This Graph Represent Course Reviews", classes="text-h5 q-pl-md")
        hc = jp.HighCharts(a=wp, classes='m-2 p-2 border')
        hc.options = chart_def
        hc.options.title.text = "Average Rating by Day"
        hc.options = chart_def
        
        
        hc.options.xAxis.categories = list(daily_ratings.index)
        hc.options.series[0].data = list(daily_ratings['Rating'])
        return wp
     
jp.justpy(app)