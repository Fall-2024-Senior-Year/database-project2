#import MySQLdb
import pymysql.cursors

DB_USERNAME = 'root'
DB_PASSWORD = 'gallery123'
DB_NAME = 'photogallerydb'

#conn = MySQLdb.connect (host = "photogallerydb.chuw1cahpjrd.us-east-1.rds.amazonaws.com",
#                        user = DB_USERNAME,
#                        passwd = DB_PASSWORD,
#                        db = DB_NAME, 
#            port = 3306)

conn = pymysql.connect(host='photogallerydb1.chuw1cahpjrd.us-east-1.rds.amazonaws.com',
                             user=DB_USERNAME,
                             password=DB_PASSWORD,
                             db=DB_NAME,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor ()
cursor.execute ("SELECT VERSION()")

cursor.execute ("CREATE TABLE photogallery2 ( \
    PhotoID int PRIMARY KEY NOT NULL AUTO_INCREMENT, \
    CreationTime TEXT NOT NULL, \
    Title TEXT NOT NULL, \
    Description TEXT NOT NULL, \
    Tags TEXT NOT NULL, \
    URL TEXT NOT NULL,\
    EXIF TEXT NOT NULL\
    );")

cursor.close ()
conn.close ()