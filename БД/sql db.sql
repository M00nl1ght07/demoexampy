--таблица партнеров 
create table partners_import (
partners_type nchar(3) not null,
partners_name nchar(50) primary key not null,
partners_director nchar(70) not null,
partners_email nchar(100) not null,
partners_phone nchar(13) not null,
partners_ur_adress nchar(300) not null,
partners_inn nchar(10) not null,
partners_rate int not null
);

--таблица типа материалов 
create table material_type_import (
material_type nchar(50) not null primary key,
material_percent_brack nchar(7) not null
);

--таблица типа продуктов
create table product_type_import (
product_type_name nchar(30) primary key not null,
product_type_kef real not null
);

--таблица продукции
create table products_import (
 products_import_name_fk nchar(50) not null,
 FOREIGN KEY (products_import_name_fk) REFERENCES product_type_import(product_type_name),
 product_import_name nchar(250) primary key not null,
 products_import_articul bigint not null,
 products_minimal_cost real not null
);

--таблица продукции партнеров
create table partner_products_import (
partner_product_name_fk nchar(250) not null,
FOREIGN KEY (partner_product_name_fk) REFERENCES products_import (product_import_name),
partner_name_fk nchar(50) not null,
FOREIGN KEY (partner_name_fk) REFERENCES partners_import (partners_name),
partner_products_count bigint not null,
partners_sale_date date not null
)