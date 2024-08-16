'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 

def scatterplot_felony_vs_nonfelony(merged_df):
    '''
    Creates a scatter plot where the x-axis is the prediction for felony and the y-axis is the prediction for nonfelony.
    The plot is colored by whether the current charge is a felony.
    
    Args:
    - `merged_df`: The dataframe resulting from merging `felony_charge` with `pred_universe`

    Returns:
    - scatterplot
    '''
    
    sns.lmplot(data=merged_df, 
               x='prediction_felony', 
               y='prediction_nonfelony', 
               hue='current_charge_felony', 
               fit_reg=False)
    plt.savefig('./data/part5_plots/scatterplot_felony_vs_nonfelony.png', bbox_inches='tight')

# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?

    # i cannot access this data

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.

def scatterplot_felony_rearrest(merged_df):
    '''
    Creates a scatter plot where the x-axis is the prediction for felony rearrest and the y-axis is whether someone was actually rearrested
    
    Args:
    - `merged_df`: The dataframe resulting from merging `felony_charge` with `pred_universe`

    Returns:
    - scatterplot
    '''
    
    sns.scatterplot(data=merged_df, 
                    x='prediction_felony_rearrest', 
                    y='actual_felony_rearrest')
    plt.savefig('./data/part5_plots/scatterplot_felony_rearrest.png', bbox_inches='tight')

# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

    # i cannot access this data