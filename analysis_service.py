import pandas as pd

north_america = ['United States', 'Canada']
south_america = ['Brazil', 'Costa Rica', 'Colombia', 'Uruguay']
central_america = ['Mexico', 'Bahamas, The']
asia = ['India', 'Singapore', 'Japan', 'Thailand', 'China', 'Philippines']
europe = ['United Kingdom', 'Bulgaria', 'France', 'Portugal', 'Netherlands', 'Switzerland', 'Poland',
            'Germany', 'Russia', 'Austria', 'Ireland', 'Italy', 'Sweden', 'Latvia', 'Romania', 'Belgium',
            'Spain', 'Finland', 'Bosnia and Herzegovina', 'Hungary', 'Croatia', 'Norway', 'Denmark',
            'Greece', 'Moldova', 'Georgia', 'Czech Republic']
africa = ['South Africa', 'Zimbabwe', 'Israel', 'Nigeria']
australia_nz = ['Australia', 'New Zealand']

def procuringRequiredDataFrame(df):
    requiredDF = df
    requiredDF['geographic_region'] = ['North America' if x in north_america else 'South America' if x in south_america 
                                       else 'Central America' if x in central_america else 'Asia' if x in asia
                                       else 'Europe' if x in europe else 'Africa' if x in africa
                                       else 'Australia NZ' for x in requiredDF['Country']]

    groupedDF = requiredDF.groupby('geographic_region')
    groupedDF.apply(lambda x: x[x['treatment'] == 'Yes'].count()).reset_index()
    print(groupedDF)