CREATE DATABASE Portfolio;

USE Portfolio;

CREATE TABLE Assets
(
   asset_id          int 	           auto_increment,
   asset_symbol      varchar(20)       NOT NULL,
   asset_name        varchar(40)       NOT NULL,
   asset_type        varchar(20)       NOT NULL DEFAULT 'UNKNOWN',
   asset_sector      varchar(40)       NOT NULL DEFAULT 'UNKNOWN',
   asset_industry    varchar(20)       NOT NULL DEFAULT 'UNKNOWN',

   PRIMARY KEY(asset_id)
);

CREATE TABLE Portfolios
(
   portfolio_id          int 	           auto_increment,
   portfolio_name        varchar(40)       NOT NULL,

   PRIMARY KEY (portfolio_id)
);

CREATE TABLE Transactions
(
   transaction_id    int               auto_increment,
   portfolio_id      int               NOT NULL,
   asset_id          int 	           NOT NULL,
   transaction_type  varchar(20)       NOT NULL DEFAULT 'UNKNOWN',
   transaction_quantity  int           NOT NULL DEFAULT 0,
   transaction_price     int           NOT NULL DEFAULT 0,
   transaction_date      date          NOT NULL,

   PRIMARY KEY(transaction_id),
   FOREIGN KEY(portfolio_id) REFERENCES Portfolios(portfolio_id),
   FOREIGN KEY(asset_id) REFERENCES Assets(asset_id)
);