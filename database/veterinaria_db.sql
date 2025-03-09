-- Activa soporte de llaves secundarias
PRAGMA foreign_keys = ON;

-- Create Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    DNI TEXT PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) <= 50),
    surname TEXT NOT NULL CHECK(length(surname) <= 50),
    email TEXT NOT NULL CHECK(length(email) <= 320),
    telephone TEXT CHECK(length(telephone) = 9 AND telephone GLOB '[0-9]*')
);

-- Create Clinicas (moved before Veterinario)
CREATE TABLE IF NOT EXISTS Clinicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Municipio TEXT NOT NULL CHECK(length(Municipio) <= 50),
    Provincia TEXT NOT NULL CHECK(length(Provincia) <= 50),
    name TEXT NOT NULL CHECK(length(name) <= 50)
);

-- Create Veterinario (now after Clinicas)
CREATE TABLE IF NOT EXISTS Veterinario (
    DNI TEXT PRIMARY KEY,
    name TEXT CHECK(length(name) <= 50),
    surname TEXT CHECK(length(surname) <= 50),
    email TEXT NOT NULL CHECK(length(email) <= 320),
    telephone TEXT NOT NULL CHECK(length(telephone) = 9 AND telephone GLOB '[0-9]*'),
    password TEXT NOT NULL,
    location INTEGER,
    FOREIGN KEY (location) REFERENCES Clinicas(id)
);

-- Create Animales
CREATE TABLE IF NOT EXISTS Animales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL CHECK(length(name) <= 50),
    species TEXT NOT NULL CHECK(length(species) <= 50),
    description TEXT CHECK(length(description) <= 2000),
    owner TEXT NOT NULL,
    FOREIGN KEY (owner) REFERENCES Clientes(DNI)
);

-- Create Recetas
CREATE TABLE IF NOT EXISTS Recetas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    treatment TEXT NOT NULL CHECK(length(treatment) <= 50),
    start_date DATE NOT NULL,
    finalized BOOLEAN,
    pacient INTEGER NOT NULL,
    FOREIGN KEY (pacient) REFERENCES Animales(id)
);

-- Create Cita
CREATE TABLE IF NOT EXISTS Cita (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    price REAL NOT NULL,
    reason TEXT NOT NULL CHECK(length(reason) <= 200),
    animal INTEGER NOT NULL,
    professional TEXT NOT NULL,
    FOREIGN KEY (animal) REFERENCES Animales(id),
    FOREIGN KEY (professional) REFERENCES Veterinario(DNI)
);

-- Ejemplo Clinicas
INSERT OR IGNORE INTO Clinicas (id, Municipio, Provincia, name) VALUES
(1,'Madrid', 'Madrid', 'VetCare Central'),
(2,'Barcelona', 'Barcelona', 'PetHealth Barcelona');

-- Ejemplo Veterinarios
INSERT OR IGNORE INTO Veterinario (DNI, name, surname, email, telephone, password, location) VALUES
('12345678A', 'Ana', 'Garcia', 'ana.garcia@vetclinic.com', '612345678', 'securepass123', 1),
('87654321B', 'Carlos', 'Lopez', 'carlos.lopez@vetclinic.com', '687654321', 'mypassword456', 2);

-- Ejemplo Clientes
INSERT OR IGNORE INTO Clientes (DNI, name, surname, email, telephone) VALUES
('11111111X', 'Maria', 'Rodriguez', 'maria@email.com', '611111111'),
('22222222Y', 'Juan', 'Fernandez', 'juan@email.com', '622222222');

-- Ejemplo Animales
INSERT OR IGNORE INTO Animales (id, name, species, description, owner) VALUES
(1,'Luna', 'Perro', 'Labrador retriever de color negro, 5 anyos de edad', '11111111X'),
(2,'Max', 'Gato', 'Gato siames de 3 anyos, vacunas al día', '11111111X'),
(3,'Toby', 'Perro', 'Yorkshire terrier de 2 anyos, castrado', '22222222Y');

-- Ejemplo Recetas
INSERT OR IGNORE INTO Recetas (id, treatment, start_date, finalized, pacient) VALUES
(1,'Antibiotico Amoxicilina', '2025-01-15', TRUE, 1),
(2,'Antiparasitario', '2025-02-10', FALSE, 2),
(3,'Antiinflamatorio', '2025-02-05', TRUE, 3);

-- Ejemplo Citas
INSERT OR IGNORE INTO Cita (id, date, price, reason, animal, professional) VALUES
(1,'2025-01-15', 50.00, 'Consulta por infeccion cutanea', 1, '12345678A'),
(2,'2025-02-10', 35.00, 'Revision y vacunacion anual', 2, '87654321B'),
(3,'2025-02-05', 65.00, 'Tratamiento dental y limpieza', 3, '12345678A');