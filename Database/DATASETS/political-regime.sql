#political-regime
#Sur ce fichier vous trouvez comment ajouter la tabe political_regime (regime politiques des pays de monde) dans laquelle 
#on trouve les differentes politiques depuis 1816 j'ausqu'a 2015, avec le scalling de 'Polity IV and Wimmer & Min', tel que
#çà part de -20 à 10:
#pays entre: -10 à -6 = autocracie
#pays entre: -5 à O = closed anocracie
#pays entre: 1 à 5 = open anocracie
#pays entre: 6 à 10 = democracie
#pays avec -20 colonisé.
#et y'a des pays sans données.on a le pourcentage de la population de chaque pays utulisant internet au cours des 30 denrieres années
#use please political_regime.csv

CREATE TABLE political_regime_import (
	Entity text NOT NULL,
	Code char(3),
        Year integer NOT NULL,
        Political_Regime numeric
);

#si le fichier csv est delimiter avec un delimiter=; lors de sa sauvegarde
copy political_regime_import from 'political-regime.csv' WITH DELIMITER ';' CSV HEADER;   
#sinon
#copy political_regime_import from 'political-regime.csv' WITH (format csv);   

SELECT DISTINCT Entity
  FROM political_regime_import
 WHERE Entity NOT IN (SELECT nicename FROM countries) order by Entity asc;


UPDATE political_regime_import SET Entity = 'Congo, the Democratic Republic of the' WHERE Entity = 'Democratic Republic of Congo';
UPDATE political_regime_import SET Entity = 'Cote D''Ivoire' WHERE Entity = 'Cote d''Ivoire';
UPDATE political_regime_import SET Entity = 'Czech Republic' WHERE Entity = 'Czechia';
UPDATE political_regime_import SET Entity = 'Iran, Islamic Republic of' WHERE Entity = 'Iran';
UPDATE political_regime_import SET Entity = 'Lao People''s Democratic Republic' WHERE Entity = 'Laos';
UPDATE political_regime_import SET Entity = 'Libyan Arab Jamahiriya' WHERE Entity = 'Libya';
UPDATE political_regime_import SET Entity = 'Moldova, Republic of' WHERE Entity = 'Moldova';
UPDATE political_regime_import SET Entity = 'Korea, Democratic People''s Republic of' WHERE Entity = 'North Korea';
UPDATE political_regime_import SET Entity = 'Korea, Republic of' WHERE Entity = 'South Korea';
UPDATE political_regime_import SET Entity = 'Russian Federation' WHERE Entity = 'Russia';
UPDATE political_regime_import SET Entity = 'Syrian Arab Republic' WHERE Entity = 'Syria';
UPDATE political_regime_import SET Entity = 'Taiwan, Province of China' WHERE Entity = 'Taiwan';
UPDATE political_regime_import SET Entity = 'Tanzania, United Republic of' WHERE Entity = 'Tanzania';
UPDATE political_regime_import SET Entity = 'Viet Nam' WHERE Entity = 'Vietnam';
UPDATE political_regime_import SET Entity = 'Timor-Leste' WHERE Entity = 'Timor';


CREATE TABLE political_regime (
	country_id int ,
    year integer NOT NULL,
    value numeric
);


INSERT INTO political_regime 
SELECT countries.id, Year , Political_Regime
  FROM political_regime_import
       JOIN
       countries ON political_regime_import.Entity = nicename;


ALTER TABLE political_Regime
  ADD PRIMARY KEY (country_id, year);

ALTER TABLE political_regime
  ADD FOREIGN KEY (country_id) REFERENCES countries(id);


drop table if exists political_regime_import;
