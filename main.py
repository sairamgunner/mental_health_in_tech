import cleaning_service as cs
import analysis_service as ansv
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 50)

cs.dropUnwantedColumns(['Timestamp', 'comments', 'state'])
cs.cleanGenderColumn()
cs.cleanAgeColumn()
cs.cleanNoEmployeesColumn()
clean_df = cs.removeNullData()
# print(clean_df)
# print(clean_df.info())

# s.printUniqueValues() # Calling this function will print all the unique values in all of the columns of the df

required_df = ansv.procuringRequiredDataFrame(clean_df)

# Analyzing mental illness family history per geographic region
fam_history_per_geo_region = ansv.analyzingFamilyHistoryPerRegion(required_df)
print(fam_history_per_geo_region)

fam_history_per_geo_region.plot.bar(x="geographic_region", y="family_history")
plt.show()



