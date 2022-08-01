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

#------------------------------------------------------------------------------------------------------------------------------------#
def procuringRequiredDataFrame(df):
    requiredDF = df
    requiredDF['geographic_region'] = ['North America' if x in north_america else 'South America' if x in south_america 
                                       else 'Central America' if x in central_america else 'Asia' if x in asia
                                       else 'Europe' if x in europe else 'Africa' if x in africa
                                       else 'Australia NZ' for x in requiredDF['Country']]

    return requiredDF

#------------------------------------------------------------------------------------------------------------------------------------#
def analyzingFamilyHistoryPerRegion(requiredDF):
    family_history_df = requiredDF.loc[requiredDF['family_history'] == 'Yes']
    grouped_fam_history_geo_df = family_history_df.groupby('geographic_region')['family_history'].count().reset_index()

    return grouped_fam_history_geo_df

#------------------------------------------------------------------------------------------------------------------------------------#
def analyzingWorkInterferenceInTechAndNonTechPerRegion(requiredDF):
    grouped_work_not_in_tech_per_region_df = requiredDF.loc[(requiredDF['tech_company'] != 'Yes') & (requiredDF['work_interfere'] == 'Often')]
    grouped_work_not_in_tech_per_region_df = grouped_work_not_in_tech_per_region_df.groupby(['geographic_region', 'work_interfere'])['tech_company'].count().reset_index()
    print(grouped_work_not_in_tech_per_region_df)

    grouped_work_in_tech_per_region_df = requiredDF.loc[(requiredDF['tech_company'] == 'Yes') & (requiredDF['work_interfere'] == 'Often')]
    grouped_work_in_tech_per_region_df = grouped_work_in_tech_per_region_df.groupby(['geographic_region', 'work_interfere'])['tech_company'].count().reset_index()
    print(grouped_work_in_tech_per_region_df)
