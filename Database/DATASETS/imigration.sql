#imigration
#Sur ce fichier vous trouvez comment ajouter la tabe imgration dans laquelle on trouve les different taux et nombres d'imigrants 
#dans chaque pays depuis 1960 j'ausqu'a 2015, avec un ecart de 5 ans pour chaque nouvelle valeur.
#use please imigration.csv

CREATE TABLE imigration_import (
	country text NOT NULL,
        year integer NOT NULL,
        Migrant_Population numeric not null ,
        Percentage_Of_Total_Population numeric not null 

);

#si le fichier csv est delimiter avec un delimiter=; lors de sa sauvegarde
copy imigration_import from 'imigration.csv' WITH DELIMITER ';' CSV HEADER;   
#sinon
#copy imigration_import from 'imigration.csv' WITH (format csv);   

SELECT DISTINCT country
  FROM imigration_import
 WHERE country NOT IN (SELECT nicename FROM countries) order by country asc;


UPDATE imigration_import SET country = 'Brunei Darussalam' WHERE country = 'Brunei';
UPDATE imigration_import SET country = 'Czech Republic' WHERE country = 'Czech';
UPDATE imigration_import SET country = 'Liechtenstein' WHERE country = 'Lechtenstein';
UPDATE imigration_import SET country = 'New Caledonia' WHERE country = 'New Calidonia';
UPDATE imigration_import SET country = 'United Arab Emirates' WHERE country = 'UAE';
UPDATE imigration_import SET country = 'United States' WHERE country = 'USA';
UPDATE imigration_import SET country = 'Korea, Republic of' WHERE country = 'South Korea';


CREATE TABLE imigration (
	country_id int ,
  year integer NOT NULL,
  Migrant_Population numeric not null ,
  Percentage_Of_Total_Population numeric not null 
);


INSERT INTO imigration 
SELECT countries.id, ii.year , ii.Migrant_Population, ii.Percentage_Of_Total_Population
  FROM imigration_import ii
       JOIN
       countries ON ii.country = nicename;


ALTER TABLE imigration
  ADD PRIMARY KEY (country_id, year);

ALTER TABLE imigration
  ADD FOREIGN KEY (country_id) REFERENCES countries(id);


drop table if exists imigration_import;
