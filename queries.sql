-- create database 'map_weather'

CREATE DATABASE map_weather_test
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;

-- create table 'historical'       

CREATE TABLE historical
(
  id serial NOT NULL,
  stations_id integer,
  stationsname character(100),
  stationshoehe integer,
  geogr_breite numeric(10,5),
  geogr_laenge numeric(10,5),
  von_datum integer,
  bis_datum integer,
  geom_4326 geometry(Point,4326),
  CONSTRAINT pk_historical_id PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE historical
  OWNER TO postgres;      
       
-- create table 'recent'

CREATE TABLE recent
(
  id serial NOT NULL,
  stations_id integer,
  stationsname character(100),
  stationshoehe integer,
  geogr_breite numeric(10,5),
  geogr_laenge numeric(10,5),
  von_datum integer,
  bis_datum integer,
  geom_4326 geometry(Point,4326),
  CONSTRAINT pk_recent_id PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE recent
  OWNER TO postgres;

-- create table 'historical_data'  

CREATE TABLE historical_data
(
  id serial NOT NULL,
  stations_id integer,
  mess_datum integer,
  qualitaets_niveau numeric(10,5),
  lufttemperatur numeric(10,5),
  dampfdruck numeric(10,5),
  bedeckungsgrad numeric(10,5),
  luftdruck_stationshoehe numeric(10,5),
  rel_feuchte numeric(10,5),
  windgeschwindigkeit numeric(10,5),
  lufttemperatur_maximum numeric(10,5),
  lufttemperatur_minimum numeric(10,5),
  lufttemp_am_erdb_minimum numeric(10,5),
  windspitze_maximum numeric(10,5),
  niederschlagshoehe numeric(10,5),
  niederschlagshoehe_ind numeric(10,5),
  sonnenscheindauer numeric(10,5),
  schneehoehe numeric(10,5),
  CONSTRAINT pk_historical_data_id PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE historical_data
  OWNER TO postgres; 
  
  
  
-- query to detect errors by adding the text files to database

SELECT COUNT(stationsname), stationsname FROM recent GROUP BY stationsname

-- update the geometry column

UPDATE recent SET geom_4326 = (SELECT ST_Point(geogr_laenge, geogr_breite) FROM recent)

SELECT ST_SRID(ST_Point(geogr_laenge, geogr_breite))