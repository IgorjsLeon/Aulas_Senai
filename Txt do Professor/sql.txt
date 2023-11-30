Vamos dividir os exercícios em quatro partes:

**Parte 1: Operações CRUD (Create, Read, Update, Delete) no Banco de Dados "Estoque"**

**Tema 1: CREATE (Inserir dados)**

**Teoria:**
A operação CREATE é usada para inserir novos registros em uma tabela. Você pode usar a instrução SQL INSERT para realizar essa operação.

**Exercício 1: Inserir um novo produto no banco de dados.**
Enunciado: Inclua um novo produto na tabela "Produtos" no banco de dados "Estoque". O produto deve ter um nome, preço e quantidade.

**Código:**
```sql
INSERT INTO Produtos (Nome, Preco, Quantidade) VALUES ('Produto1', 10.99, 100);
```

**Exercício 2: Inserir mais produtos no banco de dados.**
Enunciado: Inclua mais produtos na tabela "Produtos" no banco de dados "Estoque" até ter 20 registros no total.

**Tema 2: READ (Ler dados)**

**Teoria:**
A operação READ é usada para recuperar dados de uma tabela. Você pode usar a instrução SQL SELECT para realizar essa operação.

**Exercício 3: Selecionar todos os produtos na tabela.**
Enunciado: Escreva uma consulta SQL para selecionar todos os produtos da tabela "Produtos" no banco de dados "Estoque".

**Código:**
```sql
SELECT * FROM Produtos;
```

**Exercício 4: Selecionar produtos com um preço específico.**
Enunciado: Escreva uma consulta SQL para selecionar todos os produtos da tabela "Produtos" que têm um preço superior a $20.

**Tema 3: UPDATE (Atualizar dados)**

**Teoria:**
A operação UPDATE é usada para modificar registros existentes em uma tabela. Você pode usar a instrução SQL UPDATE para realizar essa operação.

**Exercício 5: Atualizar o preço de um produto.**
Enunciado: Atualize o preço do produto com o nome "Produto1" na tabela "Produtos" para $12.99.

**Código:**
```sql
UPDATE Produtos SET Preco = 12.99 WHERE Nome = 'Produto1';
```

**Exercício 6: Atualizar a quantidade de um produto.**
Enunciado: Atualize a quantidade do produto com o nome "Produto2" na tabela "Produtos" para 150 unidades.

**Tema 4: DELETE (Excluir dados)**

**Teoria:**
A operação DELETE é usada para remover registros de uma tabela. Você pode usar a instrução SQL DELETE para realizar essa operação.

**Exercício 7: Excluir um produto.**
Enunciado: Exclua o produto com o nome "Produto3" da tabela "Produtos" no banco de dados "Estoque".

**Código:**
```sql
DELETE FROM Produtos WHERE Nome = 'Produto3';
```

**Exercício 8: Excluir todos os produtos com preço abaixo de $10.**
Enunciado: Exclua todos os produtos da tabela "Produtos" no banco de dados "Estoque" que têm um preço inferior a $10.

**Parte 2: Operações INNER JOIN**

**Tema 5: INNER JOIN (Junção interna de tabelas)**

**Teoria:**
INNER JOIN é usado para combinar registros de duas ou mais tabelas com base em uma chave comum. Isso é útil para obter dados de tabelas relacionadas.

**Exercício 9: Listar produtos e suas categorias.**
Enunciado: Escreva uma consulta SQL para listar os produtos e suas respectivas categorias da tabela "Produtos" e "Categorias" no banco de dados "Estoque".

**Código:**
```sql
SELECT P.Nome, C.Nome AS Categoria
FROM Produtos P
INNER JOIN Categorias C ON P.CategoriaID = C.CategoriaID;
```

**Exercício 10: Listar clientes e seus pedidos.**
Enunciado: Escreva uma consulta SQL para listar os nomes dos clientes e os produtos que eles pediram a partir das tabelas "Clientes", "Pedidos" e "Produtos" no banco de dados "Estoque".

**Código:**
```sql
SELECT C.Nome AS Cliente, P.Nome AS Produto
FROM Clientes C
INNER JOIN Pedidos Pe ON C.ClienteID = Pe.ClienteID
INNER JOIN Produtos P ON Pe.ProdutoID = P.ProdutoID;
```

**Parte 3: Stored Procedures**

**Tema 6: Stored Procedures (Procedimentos Armazenados)**

**Teoria:**
Stored Procedures são programas SQL pré-compilados que podem ser chamados para realizar tarefas específicas no banco de dados.

**Exercício 11: Criar uma stored procedure para listar todos os produtos.**
Enunciado: Crie uma stored procedure chamada `ListarProdutos` que retorna todos os produtos na tabela "Produtos" no banco de dados "Estoque".

**Código:**
```sql
DELIMITER //
CREATE PROCEDURE ListarProdutos()
BEGIN
    SELECT * FROM Produtos;
END //
DELIMITER ;
```

**Exercício 12: Chamar a stored procedure para listar produtos.**
Enunciado: Chame a stored procedure `ListarProdutos` que você criou no exercício anterior.

**Código:**
```sql
CALL ListarProdutos();
```

**Parte 4: Functions**

**Tema 7: Functions (Funções)**

**Teoria:**
Functions são pequenos programas SQL que podem receber parâmetros e retornar valores calculados.

**Exercício 13: Criar uma função para calcular o preço total de um pedido.**
Enunciado: Crie uma função chamada `CalcularPrecoTotal` que recebe o PedidoID como parâmetro e retorna o preço total de um pedido, somando o preço de todos os produtos no pedido.

**Código:**
```sql
DELIMITER //
CREATE FUNCTION CalcularPrecoTotal(PedidoID INT)
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE preco_total DECIMAL(10, 2);
    SELECT SUM(Preco) INTO preco_total FROM Produtos
    WHERE ProdutoID IN (SELECT ProdutoID FROM Pedidos WHERE PedidoID = PedidoID);
    RETURN preco_total;
END //
DELIMITER ;
```

**Exercício 14: Usar a função para calcular o preço total de um pedido.**
Enunciado: Use a função `CalcularPrecoTotal` que você criou no exercício anterior para calcular o preço total do pedido com o PedidoID 1.

**Código:**
```sql
SELECT CalcularPrecoTotal(1);
```
