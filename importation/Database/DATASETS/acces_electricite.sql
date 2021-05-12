#L'accès à l'électricité est le pourcentage de la population ayant accès à l'électricité.

CREATE TABLE acces_electricite_import (
	country text NOT NULL,
    year integer NOT NULL,
    value numeric
);

copy acces_electricite_import from 'acces_electricite_import.csv' WITH DELIMITER ',' CSV HEADER;


SELECT DISTINCT country
  FROM acces_electricite_import
 WHERE country NOT IN (SELECT nicename FROM countries);



UPDATE acces_electricite_import SET country = 'United Arab Emirates' WHERE country = 'UAE';
UPDATE acces_electricite_import SET country = 'Saint Lucia' WHERE country = 'St. Lucia';
UPDATE acces_electricite_import SET country = 'Sao Tome and Principe' WHERE country = 'Sao Tome And Principe';
UPDATE acces_electricite_import SET country = 'Cape Verde' WHERE country = 'Cabo Verde';
UPDATE acces_electricite_import SET country = 'Brunei Darussalam' WHERE country = 'Brunei';
UPDATE acces_electricite_import SET country = 'Korea, Democratic People''s Republic of' WHERE country = 'North Korea';
UPDATE acces_electricite_import SET country = 'Congo, the Democratic Republic of the' WHERE country = 'Congo Rep.';
UPDATE acces_electricite_import SET country = 'Libyan Arab Jamahiriya' WHERE country = 'Libya';
UPDATE acces_electricite_import SET country = 'Tanzania, United Republic of' WHERE country = 'Tanzania';
UPDATE acces_electricite_import SET country = 'Moldova, Republic of' WHERE country = 'Moldova';
UPDATE acces_electricite_import SET country = 'Lao People''s Democratic Republic' WHERE country = 'Lao PDR';
UPDATE acces_electricite_import SET country = 'Bosnia and Herzegovina' WHERE country = 'Bosnia';
UPDATE acces_electricite_import SET country = 'Virgin Islands, U.s.' WHERE country = 'Virgin Islands (U.S.)';
UPDATE acces_electricite_import SET country = 'Trinidad and Tobago' WHERE country = 'Trinidad And Tobago';
UPDATE acces_electricite_import SET country = 'Russian Federation' WHERE country = 'Russia';
UPDATE acces_electricite_import SET country = 'Iran, Islamic Republic of' WHERE country = 'Iran';
UPDATE acces_electricite_import SET country = 'Viet Nam' WHERE country = 'Vietnam';
UPDATE acces_electricite_import SET country = 'Kyrgyzstan' WHERE country = 'Kyrgyz Republic';
UPDATE acces_electricite_import SET country = 'Saint Vincent and the Grenadines' WHERE country = 'St. Vincent And The Grenadines';
UPDATE acces_electricite_import SET country = 'Slovakia' WHERE country = 'Slovak Republic';
UPDATE acces_electricite_import SET country = 'Palestinian Territory, Occupied' WHERE country = 'West Bank And Gaza';
UPDATE acces_electricite_import SET country = 'Korea, Republic of' WHERE country = 'South Korea';
UPDATE acces_electricite_import SET country = 'Congo' WHERE country = 'Congo Dem. Rep.';
UPDATE acces_electricite_import SET country = 'Saint Martin' WHERE country = 'St. Martin (French Part)';
UPDATE acces_electricite_import SET country = 'Sint Maarten' WHERE country = 'Sint Maarten (Dutch Part)';
UPDATE acces_electricite_import SET country = 'Micronesia, Federated States of' WHERE country = 'Micronesia';



SELECT DISTINCT country
  FROM acces_electricite_import
 WHERE country NOT IN (SELECT nicename FROM countries);



CREATE TABLE acces_electricite (
	country_id int ,
    year integer NOT NULL,
    value numeric
);

INSERT INTO acces_electricite
SELECT countries.id, year , value
  FROM acces_electricite_import
  JOIN
  countries ON acces_electricite_import.country = nicename;


ALTER TABLE acces_electricite
  ADD PRIMARY KEY (country_id, year);

ALTER TABLE acces_electricite
  ADD FOREIGN KEY (country_id) REFERENCES countries(id);

DROP TABLE if exists acces_electricite_import;

