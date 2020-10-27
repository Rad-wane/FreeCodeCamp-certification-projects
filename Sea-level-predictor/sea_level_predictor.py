import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    
    plt.plot(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    
    slope, y_intercept, r_value, p_value, std_err = stats.linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x=np.linspace(1880,2050,171)
    y=slope*x+y_intercept
    
    plt.plot(x,y)

    # Create second line of best fit
    df_n=df[df['Year']>=2000]
   
    slope, y_intercept, r_value, p_value, std_err = stats.linregress(df_n['Year'],df_n['CSIRO Adjusted Sea Level'])
    x=np.linspace(2000,2050,51)
    y=slope*x+y_intercept
    
    plt.plot(x,y)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()