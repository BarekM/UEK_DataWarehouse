from modules.load import DatabaseConnection

bazka = DatabaseConnection()

# query = 'INSERT INTO tbl_owner2(OwnerName) VALUES("Barek")'
# bazka.input_one(query)

query = 'SELECT * FROM tbl_city'
print(bazka.select(query))