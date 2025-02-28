-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema air_qualityDB
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `air_qualityDB` ;

-- -----------------------------------------------------
-- Schema air_qualityDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `air_qualityDB` ;
USE `air_qualityDB` ;

-- -----------------------------------------------------
-- Table `air_qualityDB`.`Constituents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `air_qualityDB`.`Constituents` (
  `ct_id` INT NOT NULL,
  `ct_mp` VARCHAR(255) NULL,
  `ct_name` VARCHAR(45) NULL,
  PRIMARY KEY (`ct_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `air_qualityDB`.`Sites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `air_qualityDB`.`Sites` (
  `st_id` INT NOT NULL AUTO_INCREMENT,
  `st_no` INT NOT NULL,
  `st_name` VARCHAR(255) NULL,
  `st_lat` FLOAT NULL,
  `st_long` FLOAT NULL,
  `ct_id` INT NOT NULL,
  PRIMARY KEY (`st_id`, `ct_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `air_qualityDB`.`Measurements`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `air_qualityDB`.`Measurements` (
  `ms_id` INT NOT NULL AUTO_INCREMENT,
  `date_time` DATETIME(4) NULL,
  `st_id` INT NOT NULL,
  `band` VARCHAR(45) NULL,
  PRIMARY KEY (`ms_id`, `st_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `air_qualityDB`.`WeatherReadings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `air_qualityDB`.`WeatherReadings` (
  `wt_id` INT NOT NULL AUTO_INCREMENT,
  `pressure` FLOAT NULL,
  `temperature` FLOAT NULL,
  `r_humidity` FLOAT NULL,
  `ms_id` INT NOT NULL,
  PRIMARY KEY (`wt_id`, `ms_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `air_qualityDB`.`Pollutants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `air_qualityDB`.`Pollutants` (
  `pol_id` INT NOT NULL AUTO_INCREMENT,
  `pol_type` VARCHAR(45) NOT NULL,
  `pol_value` FLOAT NULL,
  `ms_id` INT NOT NULL,
  PRIMARY KEY (`pol_id`, `ms_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
