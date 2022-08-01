import cleaning_service as cs
import analysis_service as ansv
import pandas as pd

pd.set_option("display.max_columns", 50)

cs.dropUnwantedColumns(['Timestamp', 'comments', 'state'])
cs.cleanGenderColumn()
cs.cleanAgeColumn()
cs.cleanNoEmployeesColumn()
clean_df = cs.removeNullData()
# s.printUniqueValues()

ansv.procuringRequiredDataFrame(clean_df)

# print(clean_df)
# print(clean_df.info())

