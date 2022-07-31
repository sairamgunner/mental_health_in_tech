import pandas as pd
import numpy as np

df = pd.read_csv('survey-csv.csv')

def cleanGenderColumn():
    df['Gender'] = df['Gender'].replace(['Male-ish','maile', 'something kinda male?', 'Mal', 'Make'
                                        'Guy (-ish) ^_^', 'Man', 'msle', 'Mail', 'Malr',
                                        'ostensibly male, unsure what that really means'], 'Male')
    # print('Step 2', df['Gender'].unique())

    df['Gender'] = np.where((df['Gender'].str.contains('Cis')) | (df['Gender'].str.contains('Trans'))
                            | (df['Gender'].str.contains('queer')) | (df['Gender'].str.contains('-'))
                            | (df['Gender'].str.contains('fluid')) | (df['Gender'].str.contains('A'))
                            | (df['Gender'].str.contains('Neuter')) | (df['Gender'].str.contains(' ')), 
                            'Non-binary', df['Gender']) 

    # print('Step 3', df['Gender'].unique())

    df['Gender'] = np.where((df['Gender'] != 'Male') & (df['Gender'] != 'Non-binary'), 
                            'Female', df['Gender'])

    print('The Gender column has been cleaned')
    print('The values of the Gender column are: \n', df['Gender'].unique())


