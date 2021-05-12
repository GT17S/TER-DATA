#internet_usage_population
#Sur ce fichier vous trouvez comment ajouter la tabe IPU (INTERNET POPULATION USAGE) dans laquelle on a le pourcentage de la population de chaque pays utulisant internet au cours des 30 denrieres années
#use please ICT_USAGE_import.csv

CREATE TABLE internet_usage_population_import (
	Country text NOT NULL,
	ISO char(3),
        year integer NOT NULL,
        value numeric
);

#si le fichier csv est delimiter avec un delimiter=; lors de sa sauvegarde
copy internet_usage_population_import from 'ICT_USAGE_import.csv' WITH DELIMITER ';' CSV HEADER;   
#sinon
#copy internet_usage_population_import from 'ICT_USAGE_import.csv' WITH (format csv);   



UPDATE internet_usage_population_import SET country = 'Cape Verde' WHERE country = 'Cabo Verde';
UPDATE internet_usage_population_import SET country = 'Congo, the Democratic Republic of the' WHERE country = 'CONGO';
UPDATE internet_usage_population_import SET country = 'Cote D''Ivoire' WHERE country = 'Cote d''Ivoire';
UPDATE internet_usage_population_import SET country = 'Hong Kong' WHERE country = 'Hong Kong SAR';
UPDATE internet_usage_population_import SET country = 'Iran, Islamic Republic of' WHERE country = 'Iran';
UPDATE internet_usage_population_import SET country = 'Korea, Republic of' WHERE country = 'Korea';
UPDATE internet_usage_population_import SET country = 'Kyrgyzstan' WHERE country = 'Kyrgyz Republic';
UPDATE internet_usage_population_import SET country = 'Lao People''s Democratic Republic' WHERE country = 'Lao PDR';
UPDATE internet_usage_population_import SET country = 'Libyan Arab Jamahiriya' WHERE country = 'Libya';
UPDATE internet_usage_population_import SET country = 'Micronesia, Federated States of' WHERE country = 'Micronesia';
UPDATE internet_usage_population_import SET country = 'Moldova, Republic of' WHERE country = 'Moldova';
UPDATE internet_usage_population_import SET country = 'Korea, Democratic People''s Republic of' WHERE country = 'North Korea';
UPDATE internet_usage_population_import SET country = 'Slovakia' WHERE country = 'Slovak Republic';
UPDATE internet_usage_population_import SET country = 'Saint Kitts and Nevis' WHERE country = 'St. Kitts and Nevis';
UPDATE internet_usage_population_import SET country = 'Saint Lucia' WHERE country = 'St. Lucia';
UPDATE internet_usage_population_import SET country = 'Saint Vincent and the Grenadines' WHERE country = 'St. Vincent and the Grenadines';
UPDATE internet_usage_population_import SET country = 'Tanzania, United Republic of' WHERE country = 'Tanzania';
UPDATE internet_usage_population_import SET country = 'Viet Nam' WHERE country = 'Vietnam';
UPDATE internet_usage_population_import SET country = 'Virgin Islands, U.s.' WHERE country = 'Virgin Islands (U.S.)';


CREATE TABLE IPU (
	country_id int ,
    year integer NOT NULL,
    value numeric
);


INSERT INTO IPU 
SELECT countries.id, year , value
  FROM internet_usage_population_import
       JOIN
       countries ON internet_usage_population_import.country = nicename;


ALTER TABLE IPU
  ADD PRIMARY KEY (country_id, year);

ALTER TABLE IPU
  ADD FOREIGN KEY (country_id) REFERENCES countries(id);


drop table if exists internet_usage_population_import;
