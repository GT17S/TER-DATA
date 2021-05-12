#Dans ce fichier vous trouvez le pourcentage des non employees pour chaque pays pendant les dernières années
#Ce fichier sera utile pour comparer le taux de piratage et l,augmentation ou diminution des non employees
CREATE TABLE sjr_import (
	country text NOT NULL,
    year integer NOT NULL,
    value numeric
);

copy sjr_import from 'sans_job_import.csv' WITH DELIMITER ';' CSV HEADER;

SELECT DISTINCT country
  FROM sjr_import
 WHERE country NOT IN (SELECT nicename FROM countries);

UPDATE sjr_import SET country = 'United Arab Emirates' WHERE country = 'UAE';
UPDATE sjr_import SET country = 'Saint Lucia' WHERE country = 'St. Lucia';

UPDATE sjr_import SET country = 'Sao Tome and Principe' WHERE country = 'Sao Tome And Principe';
UPDATE sjr_import SET country = 'Cape Verde' WHERE country = 'Cabo Verde';

UPDATE sjr_import SET country = 'Brunei Darussalam' WHERE country = 'Brunei';
UPDATE sjr_import SET country = 'Korea, Democratic People''s Republic of' WHERE country = 'North Korea';

UPDATE sjr_import SET country = 'Congo, the Democratic Republic of the' WHERE country = 'Congo, Rep.';
UPDATE sjr_import SET country = 'Libyan Arab Jamahiriya' WHERE country = 'Libya';

UPDATE sjr_import SET country = 'Tanzania, United Republic of' WHERE country = 'Tanzania';
UPDATE sjr_import SET country = 'Moldova, Republic of' WHERE country = 'Moldova';
UPDATE sjr_import SET country = 'Lao People''s Democratic Republic' WHERE country = 'Lao PDR';
UPDATE sjr_import SET country = 'Bosnia and Herzegovina' WHERE country = 'Bosnia';
UPDATE sjr_import SET country = 'Virgin Islands, U.s.' WHERE country = 'Virgin Islands (U.S.)';
UPDATE sjr_import SET country = 'Trinidad and Tobago' WHERE country = 'Trinidad And Tobago';
UPDATE sjr_import SET country = 'Russian Federation' WHERE country = 'Russia';
UPDATE sjr_import SET country = 'Iran, Islamic Republic of' WHERE country = 'Iran';
UPDATE sjr_import SET country = 'Viet Nam' WHERE country = 'Vietnam';
UPDATE sjr_import SET country = 'Kyrgyzstan' WHERE country = 'Kyrgyz Republic';
UPDATE sjr_import SET country = 'Saint Vincent and the Grenadines' WHERE country = 'St. Vincent And The Grenadines';
UPDATE sjr_import SET country = 'Slovakia' WHERE country = 'Slovak Republic';
UPDATE sjr_import SET country = 'Palestinian Territory, Occupied' WHERE country = 'West Bank And Gaza';
UPDATE sjr_import SET country = 'Korea, Republic of' WHERE country = 'South Korea';
UPDATE sjr_import SET country = 'Congo' WHERE country = 'Congo, Dem. Rep.';

SELECT DISTINCT country
  FROM sjr_import
 WHERE country NOT IN (SELECT nicename FROM countries);



CREATE TABLE SJR (
	country_id int ,
    year integer NOT NULL,
    value numeric
);

INSERT INTO SJR
SELECT countries.id, year , value
  FROM sjr_import
  JOIN
       countries ON sjr_import.country = nicename;



ALTER TABLE SJR
  ADD PRIMARY KEY (country_id, year);

ALTER TABLE SJR
  ADD FOREIGN KEY (country_id) REFERENCES countries(id);

drop table if exists sjr_import;
