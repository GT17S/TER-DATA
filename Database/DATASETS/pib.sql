CREATE TABLE pib_import (
	country text NOT NULL,
	iso3 char(3),
    year integer NOT NULL,
    value numeric
);

copy pib_import from 'pib_import.csv' with (format csv);


SELECT DISTINCT country
  FROM pib_import
 WHERE country NOT IN (SELECT nicename FROM countries);

UPDATE pib_import SET country = 'Iran, Islamic Republic of' WHERE country = 'Iran, Islamic Rep.';
UPDATE pib_import SET country = 'Saint Lucia' WHERE country = 'St. Lucia';
UPDATE pib_import SET country = 'Cote D''Ivoire' WHERE country = 'Cote d''Ivoire';
UPDATE pib_import SET country = 'Congo' WHERE country = 'Congo, Rep.';
UPDATE pib_import SET country = 'Micronesia, Federated States of' WHERE country = 'Micronesia, Fed. Sts.';
UPDATE pib_import SET country = 'Sint Maarten' WHERE country = 'Sint Maarten (Dutch part)';
UPDATE pib_import SET country = 'Libyan Arab Jamahiriya' WHERE country = 'Libya';
UPDATE pib_import SET country = 'Venezuela' WHERE country = 'Venezuela, RB';
UPDATE pib_import SET country = 'Congo, the Democratic Republic of the' WHERE country = 'Congo, Dem. Rep.';
UPDATE pib_import SET country = 'Slovakia' WHERE country = 'Slovak Republic';
UPDATE pib_import SET country = 'Egypt' WHERE country = 'Egypt, Arab Rep.';
UPDATE pib_import SET country = 'Hong Kong' WHERE country = 'Hong Kong SAR, China';
UPDATE pib_import SET country = 'Moldova, Republic of' WHERE country = 'Moldova';
UPDATE pib_import SET country = 'Saint Kitts and Nevis' WHERE country = 'St. Kitts and Nevis';
UPDATE pib_import SET country = 'Cape Verde' WHERE country = 'Cabo Verde';
UPDATE pib_import SET country = 'Gambia' WHERE country = 'Gambia, The';
UPDATE pib_import SET country = 'Bahamas' WHERE country = 'Bahamas, The';
UPDATE pib_import SET country = 'Viet Nam' WHERE country = 'Vietnam';
UPDATE pib_import SET country = 'Kyrgyzstan' WHERE country = 'Kyrgyz Republic';
UPDATE pib_import SET country = 'Yemen' WHERE country = 'Yemen, Rep.';
UPDATE pib_import SET country = 'Korea, Republic of' WHERE country = 'Korea, Rep.';
UPDATE pib_import SET country = 'Saint Vincent and the Grenadines' WHERE country = 'St. Vincent and the Grenadines';
UPDATE pib_import SET country = 'Tanzania, United Republic of' WHERE country = 'Tanzania';

SELECT DISTINCT country
  FROM pib_import
 WHERE country NOT IN (SELECT nicename FROM countries);



CREATE TABLE pib (
	country_id int ,
        year integer NOT NULL,
        value numeric
);




INSERT INTO pib 
SELECT countries.id, year , value
  FROM pib_import
  JOIN
       countries ON pib_import.country = nicename;


ALTER TABLE pib
  ADD PRIMARY KEY (country_id, year);

ALTER TABLE pib
  ADD FOREIGN KEY (country_id) REFERENCES countries(id);



drop table if exists pib_import ;