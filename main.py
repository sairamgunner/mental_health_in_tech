import services as s

s.dropUnwantedColumns(['Timestamp', 'comments', 'state'])
s.cleanGenderColumn()
s.cleanAgeColumn()
s.cleanNoEmployeesColumn()
s.removeNullData()
# s.printUniqueValues()

