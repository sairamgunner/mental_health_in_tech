import pandas as pd
import numpy as np

df = pd.read_csv('mental_health_in_tech\survey-csv.csv')

def cleanGenderColumn():
    '''
    In this function, we will replace the unwanted values in the 'Gender' column
    '''
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

def cleanAgeColumn():
    '''
    In this function, we will remove the rows with age values having dirty data and remove megation signs from
    some negative age values.
    '''
    df['Age'] = df['Age'].abs()
    df.drop(df[df['Age'] > 99].index, inplace=True)
    print(df['Age'].unique())

def printUniqueValues():
    for col in df.columns:
        print(col, df[col].unique())

# cleanGenderColumn()
# cleanAgeColumn()
# printUniqueValues()


