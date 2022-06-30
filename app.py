from server import *

db = "my_data_base"
connect_db()
create_db(db)
engine = use_db(db)
engine.execute("""CREATE TABLE IF NOT EXISTS `employees` (
  `employeeID` INT NOT NULL AUTO_INCREMENT,
  `employeeName` VARCHAR(255) NULL,
  `employeeAge` INT NULL,
  `address` VARCHAR(255) NULL,
  PRIMARY KEY (`employeeID`))
""")

engine.execute(
    "INSERT INTO `employees` (`employeeName`, `employeeAge`, `address`) VALUES ('testemployee', '25', 'testPlace')")

result = engine.execute("SELECT * FROM `employees`")

for r in result:
    print(r)

result = engine.execute(
    "SELECT COUNT(*) FROM `employees`")
print(list(result)[0][0])
