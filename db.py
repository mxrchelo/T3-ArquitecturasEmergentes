import sqlite3
DATABASE_NAME = "IOT"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    conn=get_db()
    c= conn.cursor()
    c.executescript(
    """BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "companies" (
	"id"	INTEGER,
	"name"	TEXT,
	"api_key"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sensors" (
	"id"	INTEGER,
	"location_id"	INTEGER,
	"name"	TEXT,
	"category"	TEXT,
	"meta"	TEXT,
	"api_key"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
	FOREIGN KEY (location_id) REFERENCES locations(id)
);
CREATE TABLE IF NOT EXISTS "sensor_data" (
	"id"	INTEGER,
	"sensor_id"	INTEGER,
	"data"	TEXT,
	"fecha"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
	FOREIGN KEY (sensor_id) REFERENCES sensors(id)
);
CREATE TABLE IF NOT EXISTS "locations" (
	"id"	INTEGER,
	"company_id"	INTEGER,
	"name"	TEXT,
	"country"	TEXT,
	"city"	TEXT,
	"meta"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
	FOREIGN KEY (company_id) REFERENCES companies(id)
);
CREATE TABLE IF NOT EXISTS "admin" (
	"idusuario"	TEXT UNIQUE,
	"contrasena"	INTEGER
);
INSERT INTO "admin" VALUES ('ola15','pass15');
INSERT INTO "companies" VALUES (1,'oxus','oxus_key');
INSERT INTO "locations" VALUES (1,1,'las vegas','chile','santiago','peña');
INSERT INTO "locations" VALUES (2,1,'el chuncho','chile','santiago','san jose');
INSERT INTO "sensors" VALUES (1,1,'t3000','proximidad','meta de t3000','t3000_key');
INSERT INTO "sensors" VALUES (2,1,'t600','calor','meta_t600','t600_key');
INSERT INTO "sensor_data" VALUES (1,1,NULL,NULL);


COMMIT;"""
    )

    conn.commit()
    conn.close()
    #for table in tables:
    #    cursor.execute(table)