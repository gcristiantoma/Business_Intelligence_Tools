create database ftse_mib;
use ftse_mib;
	-- drop database ftse;
    -- drop table names_;
    drop table prices_and_others_vars;
truncate prices_and_others_vars;
CREATE TABLE companies (
    Nome VARCHAR(30) PRIMARY KEY
);
CREATE TABLE prices_and_others_vars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `Nome` VARCHAR(30),
    `Prezzo` DOUBLE,
    `Var %` FLOAT,
    `Data/ora` TIME,
    `Apertura` DOUBLE,
    `Min` DOUBLE,
    `Max` DOUBLE,
    `Qt Odierna` INT,
    `Categoria` VARCHAR(60),
    `ISIN` VARCHAR(60),
    `Prezzo Rif Prec` DOUBLE,
    `Ufficiale Prec` DOUBLE,
    `Fase Mercato` VARCHAR(10),
    `Teorico Chiusura` DOUBLE,
    `Prezzo Riferimento` varchar(30),
    `Prezzo Ufficiale` DOUBLE,
    `Data` DATETIME,
    
    FOREIGN KEY (`Nome`)
        REFERENCES companies (`Nome`)
        ON UPDATE CASCADE ON DELETE CASCADE
);

select * from companies;
select * from prices_and_others_vars;
describe prices_and_others_vars;
describe companies;
ALTER TABLE records CHANGE student_id id INT(6) NOT NULL AUTO_INCREMENT;
SET FOREIGN_KEY_CHECKS=1;
alter table companies change name_company `Nome` varchar(30);
alter table prices_and_others_vars drop FOREIGN KEY  name_company;
show engine innodb status;
insert into prices_and_others_vars(
	`Nome`,
    `Prezzo`,
    `Var %` ,
    `Data/ora`,
    `Apertura`,
    `Min`,
    `Max`,
    `Qt Odierna`,
    `Categoria` ,
    `ISIN` ,
    `Prezzo Rif Prec` ,
    `Ufficiale Prec` ,
    `Fase Mercato` ,
    `Teorico Chiusura` ,
    `Prezzo Riferimento` ,
    `Prezzo Ufficiale` ,
    `Data` ) 
 values( "A2a",	1.083,	"-0.96",	"15:41",	"1.096",	1.0725,	1.1035,	10132461,	"Servizi pubblici",	"IT0001233417",	1.0935,	1.0935,	"NEG",	1.0935,	"-",	1.11,	"2020-03-03 16:05:50"),( "A2a",	1.083,	"-0.96",	"15:41",	"1.096",	1.0725,	1.1035,	10132461,	"Servizi pubblici",	"IT0001233417",	1.0935,	1.0935,	"NEG",	1.0935,	"-",	1.11,	"2020-0prices_and_others_vars3-03 16:05:50");

/* Problems to be solved:
remove the %
tranform the column date as YEar-month-day

*/
select * from prices_and_others_vars;
DELETE FROM prices_and_others_vars WHERE Nome is null ;

/*

1. Find the Min and Max prices for each Company from all available data
2. Wich stock has the biggest variation, also distunguish the variation by industry
3. Trace a histogram for all stocks and trendline
*/
