DROP TABLE IF EXISTS Artysta;
DROP TABLE IF EXISTS Eksponat;
DROP TABLE IF EXISTS Historia;
DROP TABLE IF EXISTS Instytucja;
DROP TABLE IF EXISTS Sala;	
	

CREATE TABLE Artysta (
    id SERIAL  NOT NULL,
    imie_nazwisko varchar(30)  NOT NULL,
    data_urodzenia date  NULL  CHECK (data_urodzenia IS NULL OR data_urodzenia > '0001-01-01'),
    data_smierci date  NULL  CHECK (data_smierci IS NULL OR data_smierci > data_urodzenia),
    CONSTRAINT Artysta_pk PRIMARY KEY (id),
    UNIQUE(id, imie_nazwisko)
);

CREATE TABLE Eksponat (
    id SERIAL  NOT NULL,
    tytul varchar(50)  NOT NULL,
    artysta_id int  NOT NULL,
    status_wyp boolean  NOT NULL,
    wysokosc decimal(100,2)  NOT NULL CHECK (wysokosc > 0),
    szerokosc decimal(100,2)  NOT NULL CHECK (szerokosc > 0),
    waga decimal(100,2)  NOT NULL CHECK (waga > 0),
    CONSTRAINT Eksponat_pk PRIMARY KEY (id)
);

CREATE TABLE Historia (
    id SERIAL  NOT NULL,
    eksponat_id int  NOT NULL,
    sala_id int  NULL,
    instytucja_id int  NULL,
    data_pocz date  NOT NULL CHECK (data_pocz > '2025-01-01'),
    data_kon date  NULL CHECK (data_kon > data_pocz OR data_kon is NULL),
    CONSTRAINT Historia_pk PRIMARY KEY (id)
);

CREATE TABLE Instytucja (
    id SERIAL  NOT NULL,
    nazwa varchar(50)  NOT NULL,
    miasto varchar(20)  NOT NULL,
    CONSTRAINT Instytucja_pk PRIMARY KEY (id)
);

CREATE TABLE Sala (
    id SERIAL  NOT NULL,
    nazwa_galerii varchar(50)  NOT NULL,
    CONSTRAINT Sala_pk PRIMARY KEY (id)
);

ALTER TABLE Eksponat ADD CONSTRAINT Eksponat_Artysta
    FOREIGN KEY (artysta_id)
    REFERENCES Artysta (id)  
;

ALTER TABLE Historia ADD CONSTRAINT Historia_Eksponat
    FOREIGN KEY (eksponat_id)
    REFERENCES Eksponat (id)
;

ALTER TABLE Historia ADD CONSTRAINT Historia_Galeria
    FOREIGN KEY (sala_id)
    REFERENCES Sala (id)
;

ALTER TABLE Historia ADD CONSTRAINT Historia_Instytucja
    FOREIGN KEY (instytucja_id)
    REFERENCES Instytucja (id)
;

CREATE OR REPLACE FUNCTION sprawdz_dni_poza_muzeum() RETURNS TRIGGER AS $$
DECLARE
    dni_poza_muzeum INT;
BEGIN
    SELECT COALESCE(SUM(COALESCE(data_kon, CURRENT_DATE) - data_pocz), 0)
    INTO dni_poza_muzeum
    FROM Historia
    WHERE eksponat_id = NEW.eksponat_id
      AND instytucja_id IS NOT NULL
      AND DATE_PART('year', data_pocz) = DATE_PART('year', CURRENT_DATE);
      
    IF dni_poza_muzeum + (COALESCE(NEW.data_kon, CURRENT_DATE) - NEW.data_pocz) > 30 THEN
        RAISE EXCEPTION 'Eksponat nie może znajdować się poza muzeum przez więcej niż 30 dni w ciągu roku.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_sprawdz_dni_poza_muzeum
BEFORE INSERT OR UPDATE ON Historia
FOR EACH ROW
EXECUTE FUNCTION sprawdz_dni_poza_muzeum();
