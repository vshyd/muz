-- Populate Artysta
INSERT INTO Artysta (imie_nazwisko, data_urodzenia, data_smierci)
VALUES 
('Leonardo da Vinci', '1452-04-15', '1519-05-02'),
('Vincent van Gogh', '1853-03-30', '1890-07-29'),
('Pablo Picasso', '1881-10-25', NULL),
('Claude Monet', '1840-11-14', '1926-12-05'),
('Salvador Dalí', '1904-05-11', '1989-01-23'),
('Frida Kahlo', '1907-07-06', '1954-07-13'),
('Rembrandt van Rijn', '1606-07-15', '1669-10-04');

-- Populate Eksponat
INSERT INTO Eksponat (tytul, artysta_id, status_wyp, wysokosc, szerokosc, waga)
VALUES 
('Mona Lisa', 1, FALSE, 77.0, 53.0, 18.0),
('Starry Night', 2, FALSE, 73.7, 92.1, 15.0),
('Guernica', 3, FALSE, 349.0, 776.0, 60.0),
('Water Lilies', 4, FALSE, 100.0, 200.0, 25.0),
('The Persistence of Memory', 5, FALSE, 24.0, 33.0, 5.0),
('The Two Fridas', 6, FALSE, 173.5, 173.0, 40.0),
('The Night Watch', 7, FALSE, 363.0, 437.0, 150.0);

-- Populate Instytucja
INSERT INTO Instytucja (nazwa, miasto)
VALUES 
('Louvre', 'Paris'),
('Museum of Modern Art', 'New York'),
('Prado Museum', 'Madrid'),
('Tate Modern', 'London'),
('National Gallery of Art', 'Washington'),
('Rijksmuseum', 'Amsterdam'),
('Museo Frida Kahlo', 'Coyoacán');

-- Populate Sala
INSERT INTO Sala (nazwa_galerii)
VALUES 
('Galeria Renesansu'),
('Galeria Impresjonistów'),
('Galeria Współczesna'),
('Galeria Baroku'),
('Galeria Surrealizmu'),
('Galeria Klasyczna'),
('Galeria Latynoamerykańska');
