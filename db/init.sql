CREATE DATABASE citiesData;
use citiesData;

CREATE TABLE IF NOT EXISTS tblCitiesImport (
    `fldName` VARCHAR(21) CHARACTER SET utf8,
    `fldLat` NUMERIC(6, 4),
    `fldLong` NUMERIC(7, 4),
    `fldCountry` VARCHAR(19) CHARACTER SET utf8,
    `fldAbreviation` VARCHAR(3) CHARACTER SET utf8,
    `fldCapitalStatus` VARCHAR(7) CHARACTER SET utf8,
    `fldPopulation` INT
);