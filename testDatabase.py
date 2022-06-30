from server import *

dataBase = "my_data_base"
connect_db()
create_db(dataBase)
engine = use_db(dataBase)
engine.execute("""CREATE TABLE IF NOT EXISTS `testemployees` (
  `employeeID` INT NOT NULL AUTO_INCREMENT,
  `employeeName` VARCHAR(255) NULL,
  `employeeAge` INT NULL,
  `address` VARCHAR(255) NULL,
  PRIMARY KEY (`employeeID`))
""")


def test_database_result():
    result = engine.execute(
        "SELECT COUNT(*) FROM `testemployees`")

    row_num = int(list(result)[0][0])
    if row_num == 0:
        engine.execute(
            "INSERT INTO `testemployees` (`employeeName`, `employeeAge`, `address`) VALUES ('testemployees', '18', 'testPlace')")
    result = engine.execute(
        "SELECT * FROM `testemployees`")
    result_converted = str(list(result)[0][1])
    assert result_converted == "testemployees"


test_database_result()
print("success")
