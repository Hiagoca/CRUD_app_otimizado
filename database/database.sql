DROP DATABASE IF EXISTS cadtrecos;
CREATE DATABASE cadtrecos
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE cadtrecos;

CREATE TABLE owner (
    o_id INT PRIMARY KEY AUTO_INCREMENT,
    o_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    o_birth DATE,
    o_name VARCHAR(127) NOT NULL,
    o_email VARCHAR(255) NOT NULL,
    o_pass VARCHAR(63) NOT NULL,
    o_status ENUM('on', 'off', 'del') DEFAULT 'on'
);

CREATE TABLE thing (
    t_id INT PRIMARY KEY AUTO_INCREMENT,
    t_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    t_owner INT NOT NULL,
    t_photo VARCHAR(255),
    t_name VARCHAR(127) NOT NULL,
    t_description TEXT,
    t_location VARCHAR(255),
    t_status ENUM('on', 'off', 'del') DEFAULT 'on',
    FOREIGN KEY (t_owner) REFERENCES owner (o_id)
);


INSERT INTO owner (
    o_birth,
    o_name,
    o_email,
    o_pass
) VALUES (
    '2000-10-28',
    'Joca da Silva',
    'jocasilva@email.com',
    SHA1('Senha123')
), (
    '1999-10-11',
    'Marineuza Siriliano',
    'marineuza@email.com',
    SHA1('Senha123')
);

INSERT INTO thing (t_owner, t_photo, t_name, t_description, t_location) VALUES
(1, 'https://picsum.photos/196', 'peteca', 'Cheia de penas velhas', 'Caixa de sapato sob a cama'),
(2, 'https://picsum.photos/197', 'caneca', 'Caneca de cerâmica verde', 'Prateleira da cozinha'),
(1, 'https://picsum.photos/198', 'livro', 'Livro de capa dura', 'Estante do escritório'),
(2, 'https://picsum.photos/199', 'relógio', 'Relógio de parede antigo', 'Sala de estar'),
(1, 'https://picsum.photos/200', 'ferramenta', 'Martelo de carpinteiro', 'Caixa de ferramentas na garagem'),
(2, 'https://picsum.photos/201', 'vaso', 'Vaso de vidro transparente', 'Mesa da sala de jantar'),
(1, 'https://picsum.photos/202', 'brinquedo', 'Carrinho de brinquedo', 'Quarto das crianças'),
(2, 'https://picsum.photos/203', 'guitarra', 'Guitarra elétrica vermelha', 'Estúdio de música'),
(1, 'https://picsum.photos/204', 'pintura', 'Quadro abstrato colorido', 'Parede do corredor'),
(2, 'https://picsum.photos/205', 'cadeira', 'Cadeira de escritório ergonômica', 'Home office');
