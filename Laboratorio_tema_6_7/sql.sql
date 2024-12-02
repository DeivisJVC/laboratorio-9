-- Actividad 2
--paso 1
CREATE TABLE `Estudiante`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `nombres` VARCHAR(50) NOT NULL,
    `apellidos` VARCHAR(50) NOT NULL,
    `edad` INT,
    `ciudad` VARCHAR(50)
);
INSERT INTO Estudiante VALUE(1,"Deivis","Yance",18,"Santa Marta");
INSERT INTO Estudiante VALUE(2,"Luis","Rodriguez",19,"Barranquilla");
INSERT INTO Estudiante VALUE(3,"Maria","Cabana",20,"Cartagena");
INSERT INTO Estudiante VALUE(4,"Yudis","Rosado",35,"Medellin");
INSERT INTO Estudiante VALUE(5,"Jose","Yance",40,"Amazonas");
INSERT INTO Estudiante VALUE(6,"Emiliano","Suarez",50,"Huila");
INSERT INTO Estudiante VALUE(7,"Laura","Martinez",25,"Santa Marta");

SELECT * FROM Estudiante;

SELECT * FROM Estudiante 
  WHERE ciudad="Santa Marta";

SELECT * FROM Estudiante
  WHERE edad>20;

