-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema metacritic
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema metacritic
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `metacritic` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `metacritic` ;

-- -----------------------------------------------------
-- Table `metacritic`.`games`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `metacritic`.`games` (
  `Metascore` BIGINT NULL DEFAULT NULL,
  `Userscore` DOUBLE NULL DEFAULT NULL,
  `Title` TEXT NULL DEFAULT NULL,
  `Genres` TEXT NULL DEFAULT NULL,
  `Section` TEXT NULL DEFAULT NULL,
  `Publisher` TEXT NULL DEFAULT NULL,
  `Platforms` TEXT NULL DEFAULT NULL,
  `Release` TEXT NULL DEFAULT NULL,
  `Summary` TEXT NULL DEFAULT NULL,
  `Game_url` TEXT NULL DEFAULT NULL,
  `Publisher_url` TEXT NULL DEFAULT NULL,
  `Reviews` BIGINT NULL DEFAULT NULL,
  `Positive` BIGINT NULL DEFAULT NULL,
  `Neutral` BIGINT NULL DEFAULT NULL,
  `Negative` BIGINT NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
