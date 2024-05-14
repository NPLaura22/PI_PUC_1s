create database piControleEstoque character set utf8mb4;
use piControleEstoque;

create table Produtos (
CodProduto int,
Nome varchar (50) not null,
Descricao varchar(150) not null,
CustoProduto decimal(10, 2) not null,
CustoFixo decimal(10,2) not null,
ComissaoVendas decimal(10,2) not null,
Impostos decimal(10,2) not null,
Rentabilidade decimal(10,2) not null,
primary key (CodProduto)
) default charset = utf8mb4;

select * from Produtos;

insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) 
values (1, 'Roda', 'Tamanho médio', 36.00, 11.25, 3.75, 9.00, 15.00);

insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) 
values (2, 'Pneu', 'Pneu para carros de passeio', 80.00, 20.00, 5.00, 10.00, 15.00);

insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) 
values (3, 'Óleo de Motor', 'Óleo sintético para motor', 25.00, 5.00, 3.00, 5.00, 10.00);

insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) 
values (4, 'Bateria de Carro', 'Bateria de 60Ah 12V', 150.00, 30.00, 7.50, 15.00, 25.00);

insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) 
values (5, 'Pastilhas de Freio', 'Pastilhas para veículos leves', 70.00, 15.00, 4.50, 9.00, 15.00);

insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) 
values (6, 'Filtro de Ar', 'Filtro para veículos a gasolina', 20.00, 5.00, 2.00, 4.00, 10.00);

insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) 
values (7, 'Lâmpada de Farol', 'Lâmpada H4 12V', 10.00, 2.50, 1.00, 2.00, 7.50);

insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) 
values (8, 'Correia Dentada', 'Correia para motor 1.6', 100.00, 25.00, 6.25, 12.50, 20.00);