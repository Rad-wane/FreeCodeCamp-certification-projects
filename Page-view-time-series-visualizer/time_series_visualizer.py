import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=[0],index_col='date')

# Clean data
df = df[
    (df['value']>df['value'].quantile(0.025))&
    (df['value']<df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig=plt.figure(figsize=(16, 6))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.plot(df)
    plt.xlabel("Date")
    plt.ylabel("Page Views")  




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_c=df.copy(deep="True")
    df_c=df_c.reset_index()
    df_c['year'] = pd.DatetimeIndex(df_c['date']).year
    df_c['month'] = pd.DatetimeIndex(df_c['date']).month
    df_c=df_c.groupby(['year','month']).mean().sort_values(['year','month'])
    df_c=df_c.reset_index()
    df_c=df_c.rename(columns={'value': 'Average Page Views','month': 'Months','year': 'Years'})

    mon = ['January','February','March','April','May','June','July','August','September','October','November','December']
    dict_mon={}
    for i in range(12):
        dict_mon[i+1]=mon[i]

    df_c["Months"].replace(dict_mon, inplace=True)
    # Draw bar plot
    sns.set_style("ticks")

    g=sns.catplot(data=df_c,x='Years',y='Average Page Views',hue='Months',hue_order=mon,kind='bar',palette="tab10", legend=False)
    fig = g.fig
    fig.set_figheight(10)
    fig.set_figwidth(11)
    ax = g.ax
    plt.xticks(rotation=90)
    plt.legend(loc='upper left',title="Months")
    plt.setp(ax.get_legend().get_texts(), fontsize='12')
    plt.setp(ax.get_legend().get_title(), fontsize='12')





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    def fixed_boxplot(*args, label=None, **kwargs):
        sns.boxplot(*args, **kwargs, labels=[label])
        # https://github.com/mwaskom/seaborn/issues/915
        # TypeError: box() got an unexpected keyword argument 'label'
    df_box.sort_values(by=['year','date'], ascending=[False, True], inplace=True)
    df_box=df_box.rename(columns={'value': 'Page Views','month': 'Month','year': 'Year'})
    g = sns.PairGrid(df_box, y_vars=["Page Views"], x_vars=["Year", "Month"])
    g.map(fixed_boxplot)
    fig = g.fig
    fig.set_figheight(6)
    fig.set_figwidth(16)
    fig.axes[0].set_ylabel('Page Views')
    fig.axes[1].set_ylabel('Page Views')
    fig.axes[0].set_title('Year-wise Box Plot (Trend)')
    fig.axes[1].set_title('Month-wise Box Plot (Seasonality)')
    plt.tight_layout()




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
