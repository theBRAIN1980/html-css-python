#import the module
import config
# creating database_cursor to perform SQL operation
#make connection to database
con = config.connect()
#open cursor
db_cursor = con.cursor(dictionary=True)
# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE IF NOT EXISTS probaproba")
# get list of all databases
db_cursor.execute("SHOW DATABASES")
#print all databases
for db in db_cursor:
	print(db)
db_cursor.execute('CREATE TABLE IF NOT EXISTS `probaproba`.`test` (`idtest` int unsigned NOT NULL AUTO_INCREMENT, `testcol` varchar(45) DEFAULT NULL, `testcol1` varchar(45) DEFAULT NULL, `testcol2` varchar(45) DEFAULT NULL, `testcol3` varchar(45) DEFAULT NULL, `testcol4` varchar(45) DEFAULT NULL, `testcol5` varchar(45) DEFAULT NULL, `testcol6` varchar(45) DEFAULT NULL, PRIMARY KEY (`idtest`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;')
db_cursor.execute('CREATE TABLE IF NOT EXISTS `probaproba`.`fest` (`idfest` int unsigned NOT NULL AUTO_INCREMENT, `festcol` varchar(45) DEFAULT NULL, `festcol1` varchar(45) DEFAULT NULL, `festcol2` varchar(45) DEFAULT NULL, `festcol3` varchar(45) DEFAULT NULL, `festcol4` varchar(45) DEFAULT NULL, `festcol5` varchar(45) DEFAULT NULL, `festcol6` varchar(45) DEFAULT NULL, PRIMARY KEY (`idfest`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;')

for entry in db_cursor:
	db_cursor.execute('INSERT INTO `probaproba`.`test` VALUES (Gicu, Georgescu, Romana, 1791203834296, M, 12)')