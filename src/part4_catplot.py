'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.

def catplot_felony_rearrest(merged_df):
    '''
    Creates a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest
    
    Args:
     - `merged_df`: The dataframe resulting from merging `felony_charge` with `pred_universe`

    Returns:
    - catplot
    '''
    sns.catplot(data=merged_df, 
                x='charge_type', 
                y='prediction_felony_rearrest', 
                kind='bar')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest.png', bbox_inches='tight')

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest

def catplot_nonfelony_rearrest(merged_df):
    '''
    + x-axis is the charge type and the y-axis is the prediction for nonfelony rearrest
    
    Args:
     - `merged_df`: The dataframe resulting from merging `felony_charge` with `pred_universe`

    Returns:
    - catplot
    '''
    sns.catplot(data=merged_df, 
                x='charge_type', 
                y='prediction_nonfelony_rearrest', 
                kind='bar')
    plt.savefig('./data/part4_plots/catplot_nonfelony_rearrest.png', bbox_inches='tight')

# In a print statement, answer the following question: What might explain the difference between the plots?

    # i cannot access data

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime

def catplot_felony_rearrest_hue(merged_df):
    '''
    + the hue represents whether the person actually got rearrested for a felony crime.
    
    Args:
     - `merged_df`: The dataframe resulting from merging `felony_charge` with `pred_universe`
     
    Returns:
    - catplot
    '''
    sns.catplot(data=merged_df, 
                x='charge_type', 
                y='prediction_felony_rearrest', 
                hue='actual_felony_rearrest', 
                kind='bar')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest_hue.png', bbox_inches='tight')

# In a print statement, answer the following question: 

    # i cannot access data
    
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?