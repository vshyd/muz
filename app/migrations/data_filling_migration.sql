-- Populate Artysta
INSERT INTO Artysta (id, imie_nazwisko, data_urodzenia, data_smierci)
VALUES 
(1, 'Leonardo da Vinci', '1452-04-15', '1519-05-02'),
(2, 'Vincent van Gogh', '1853-03-30', '1890-07-29'),
(3, 'Pablo Picasso', '1881-10-25', NULL),
(4, 'Claude Monet', '1840-11-14', '1926-12-05'),
(5, 'Salvador Dalí', '1904-05-11', '1989-01-23'),
(6, 'Frida Kahlo', '1907-07-06', '1954-07-13'),
(7, 'Rembrandt van Rijn', '1606-07-15', '1669-10-04');

-- Populate Eksponat
INSERT INTO Eksponat (id, tytul, artysta_id, status_wyp, wysokosc, szerokosc, waga)
VALUES 
(1, 'Mona Lisa', 1, FALSE, 77.0, 53.0, 18.0),
(2, 'Starry Night', 2, FALSE, 73.7, 92.1, 15.0),
(3, 'Guernica', 3, FALSE, 349.0, 776.0, 60.0),
(4, 'Water Lilies', 4, FALSE, 100.0, 200.0, 25.0),
(5, 'The Persistence of Memory', 5, FALSE, 24.0, 33.0, 5.0),
(6, 'The Two Fridas', 6, FALSE, 173.5, 173.0, 40.0),
(7, 'The Night Watch', 7, FALSE, 363.0, 437.0, 150.0);

-- Populate Instytucja
INSERT INTO Instytucja (id, nazwa, miasto)
VALUES 
(1, 'Louvre', 'Paris'),
(2, 'Museum of Modern Art', 'New York'),
(3, 'Prado Museum', 'Madrid'),
(4, 'Tate Modern', 'London'),
(5, 'National Gallery of Art', 'Washington'),
(6, 'Rijksmuseum', 'Amsterdam'),
(7, 'Museo Frida Kahlo', 'Coyoacán');


-- Populate Sala
INSERT INTO Sala (id, nazwa_galerii)
VALUES 
(1, 'Galeria Renesansu'),
(2, 'Galeria Impresjonistów'),
(3, 'Galeria Współczesna'),
(4, 'Galeria Baroku'),
(5, 'Galeria Surrealizmu'),
(6, 'Galeria Klasyczna'),
(7, 'Galeria Latynoamerykańska');