CREATE TABLE `Empleados`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `nombres` VARCHAR(255) NOT NULL,
    `apellido` VARCHAR(255) NOT NULL,
    `puesto` VARCHAR(255) NOT NULL,
    `salario` VARCHAR(255) NOT NULL,
    `edad` BIGINT NOT NULL,
    `celular` BIGINT NOT NULL,
    `direccion` VARCHAR(255) NOT NULL
   
);

INSERT INTO Empleados VALUE(1,"Deivis","Sanchez","Dev Full Stack",8000000,35,315986998,"calle22 #45-9");
INSERT INTO Empleados VALUE(2,"Luis","Yance"," Dev Backend",5000000,24,318898465,"calle24 #50-7");
INSERT INTO Empleados VALUE(3,"Laura","Rodriguez","Dev frontend",4500000,23,31854486998,"calle28 #609");
INSERT INTO Empleados VALUE(4,"Digna","Urbina"," Dev Frontend",4500000,23,31885498,"calle87 #699");
INSERT INTO Empleados VALUE(5,"Andres","Felipe"," Dev Frontend",4500000,19,31895498,"calle89 #554"); 
INSERT INTO Empleados VALUE(6,"Valeria","Galindo","Dev Frontend",4500000,19,314545498,"calle99 #9099");
INSERT INTO Empleados VALUE(7,"Yudis","Rosado","Dev Full Stack",8000000,42,3014548,"calle88 #9459");
INSERT INTO Empleados VALUE(8,"Jorge","Guzman","Dev Backend",5000000,63,325984148,"calle645 #54499");
INSERT INTO Empleados VALUE(9,"Luis","Enrique","Dev Frontend",4500000,41,316548797,"calle548 #45455");
INSERT INTO Empleados VALUE(10,"Laura","Martinez","Dev Frontend",4500000,18,456454545498,"calle99 #454");
-- Consultas
SELECT salario FROM Empleados WHERE salario=4500000;
SELECT puesto FROM Empleados WHERE edad>30;
--Actualizacion
UPDATE Empleados Set salario=6000000
WHERE id=6 or id=2
