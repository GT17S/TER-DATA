#Dans ce fichier vous trouvez le nombre de serveurs sécurisés par million d’habitants
#Ce fichier sera utile pour comparer le taux de piratage en fonction dévolution des serveurs sécurisé

CREATE TABLE serveur_securise_import (
	Country text NOT NULL,
	ISO char(3),
    year integer NOT NULL,
    value numeric
);

copy serveur_securise_import from 'serveur_securise_import.csv' WITH DELIMITER ';' CSV HEADER;

UPDATE serveur_securise_import SET country = 'Saint Martin' WHERE country = 'St. Martin (French part)';
UPDATE serveur_securise_import SET country = 'Korea, Republic of' WHERE country = 'Korea';
UPDATE serveur_securise_import SET country = 'Saint Lucia' WHERE country = 'St. Lucia';
UPDATE serveur_securise_import SET country = 'Libyan Arab Jamahiriya' WHERE country = 'Libya';
UPDATE serveur_securise_import SET country = 'Slovakia' WHERE country = 'Slovak Republic';
UPDATE serveur_securise_import SET country = 'Moldova, Republic of' WHERE country = 'Moldova';
UPDATE serveur_securise_import SET country = 'Saint Kitts and Nevis' WHERE country = 'St. Kitts and Nevis';
UPDATE serveur_securise_import SET country = 'Congo, the Democratic Republic of the' WHERE country = 'Congo,the Democratic Republic of the';
UPDATE serveur_securise_import SET country = 'Cape Verde' WHERE country = 'Cabo Verde';
UPDATE serveur_securise_import SET country = 'Estonia' WHERE country = 'Eswatini';
UPDATE serveur_securise_import SET country = 'Iran, Islamic Republic of' WHERE country = 'Iran';
UPDATE serveur_securise_import SET country = 'Cape Verde' WHERE country = 'Cabo Verde';
UPDATE serveur_securise_import SET country = 'Micronesia, Federated States of' WHERE country = 'Micronesia';
UPDATE serveur_securise_import SET country = 'Viet Nam' WHERE country = 'Vietnam';
UPDATE serveur_securise_import SET country = 'Kyrgyzstan' WHERE country = 'Kyrgyz Republic';
UPDATE serveur_securise_import SET country = 'Saint Vincent and the Grenadines' WHERE country = 'St. Vincent and the Grenadines';
UPDATE serveur_securise_import SET country = 'Tanzania, United Republic of' WHERE country = 'Tanzania';
UPDATE serveur_securise_import SET country = 'Hong Kong' WHERE country = 'Hong Kong SAR';
UPDATE serveur_securise_import SET country = 'Cote D''Ivoire' WHERE country = 'Cote d''Ivoire';


CREATE TABLE serveur_securise (
	country_id int ,
    year integer NOT NULL,
    value numeric
);

INSERT INTO serveur_securise
SELECT countries.id, year , value
  FROM serveur_securise_import
  JOIN
       countries ON serveur_securise_import.country = nicename;

DELETE FROM serveur_securise
WHERE country_id=113 and (value=0.0393236566989717 or value=0.0)
DELETE FROM serveur_securise
WHERE country_id=67

ALTER TABLE serveur_securise
  ADD PRIMARY KEY (country_id, year);

ALTER TABLE serveur_securise
  ADD FOREIGN KEY (country_id) REFERENCES countries(id);

insert into serveur_securise(country_id,year,value) values(67,2010,535.496348035074);
insert into serveur_securise(country_id,year,value) values(67,2011,730.730376311077);
insert into serveur_securise(country_id,year,value) values(67,2021,1255.76852126263);
insert into serveur_securise(country_id,year,value) values(67,2013,1613.81247453522);
insert into serveur_securise(country_id,year,value) values(67,2014,2194.67572430004);
insert into serveur_securise(country_id,year,value) values(67,2015,3120.70712714772);
insert into serveur_securise(country_id,year,value) values(67,2016,10786.6756853297);
insert into serveur_securise(country_id,year,value) values(67,2017,29131.217625233);
insert into serveur_securise(country_id,year,value) values(67,2018,48893.4376316683);
insert into serveur_securise(country_id,year,value) values(67,2019,83332.453885526);
insert into serveur_securise(country_id,year,value) values(67,2020,84642.2641509434)


drop table if exists serveur_securise_import ;