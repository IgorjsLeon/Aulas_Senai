use loja_II;

CREATE TABLE produto
(`id` INT(5) PRIMARY KEY NOT NULL AUTO_INCREMENT,
`nome` VARCHAR(45) NOT NULL, `quantidade` INT(5) NOT NULL,
`preco` DECIMAL(4) NOT NULL, `tipo` VARCHAR(20));



INSERT INTO clientes(nome, endereco, telefone, e_mail, cpf)
VALUES ('Igor Jesus Silva Leon', 'Rua ao infinito e Além', '123456', 'igor@igor', '123456789');
INSERT INTO clientes(nome, endereco, telefone, e_mail, cpf)
VALUES ('Joelma Edmara do Nascimento Leon', 'Rua ao infinito e Além', '654321', 'joh@joh', '987654321');
INSERT INTO clientes(nome, endereco, telefone, e_mail, cpf)
VALUES ('Cassio de Albuquerque', 'Rua Infinity', '546132', 'cassio@cassio', '876543219');
INSERT INTO clientes(nome, endereco, telefone, e_mail, cpf)
VALUES ('Fabio Antunes e Silva', 'Rua dos bobos', '543216', 'fabio@fabio', '765432189');
INSERT INTO clientes(nome, endereco, telefone, e_mail, cpf)
VALUES ('Luciana Antunes e Silva', 'Rua dos bobos', '526336', 'luciana@luciana', '654321987');
INSERT INTO clientes(nome, endereco, telefone, e_mail, cpf)
VALUES ('Luciano Antunes e Silva', 'Rua das liunias', '987654', 'luciano@luciano', '321654987');
INSERT INTO clientes(nome, endereco, telefone, e_mail, cpf)
VALUES ('Lucas Antunes e Silva', 'Rua das Vielas', '741852', 'lucas@lucas', '752369741');

INSERT INTO produto(nome, quantidade, preco, tipo)
VALUES ('Samsung_galaxy', '10', '1.300', 'eletronico');

CREATE TABLE compras
(`ipproduto` INT(5) NOT NULL, `idcliente` INT(5) NOT NULL, `quantidade` INT(5), `valor` DECIMAL(4));