import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

df = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
share = df.groupby(['Course Name'])['Rating'].count()


chart_def = """ {
    chart: {
        type: 'pie',
        plotShadow: false,
        
    },
    title: {
        text: 'Course reviews, pie chart'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}

"""


def app():
        wp = jp.QuasarPage()
        h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
        p1 = jp.QDiv(a=wp, text="This Graph Represents Course Reviews", classes="text-h5 q-pl-md")
        hc = jp.HighCharts(a=wp, options= chart_def)
        hc.options = chart_def


        hc_data = [{"name":v1, "data":v2 }for v1, v2 in zip(share.index,share)]
        #hc_data = [{"name": v1, "y": int(share[v1])} for v1 in course_count.index] 
        hc.options.series[0] = hc_data
        return wp
     
jp.justpy(app)
