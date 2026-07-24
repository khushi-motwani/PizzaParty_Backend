-- Portfolios Table CRUD Operations
USE Portfolio;

-- ==================== GETTER OPERATIONS ====================

-- def getAllPortfolios()
SELECT * FROM Portfolios ORDER BY portfolio_id;

-- def getPortfolioById(portfolio_id)
SELECT * FROM Portfolios WHERE portfolio_id = ?;

-- def getPortfolioBalance(portfolio_id)
SELECT portfolio_id, portfolio_name, portfolio_balance
FROM Portfolios
WHERE portfolio_id = ?;

-- def getTotalBalance()
SELECT SUM(portfolio_balance) as total_balance FROM Portfolios;

-- def getPortfolioCount()
SELECT COUNT(*) as total_portfolios FROM Portfolios;

-- def getPortfoliosSortedByBalanceDesc()
SELECT * FROM Portfolios ORDER BY portfolio_balance DESC;

-- def getPortfoliosSortedByBalanceAsc()
SELECT * FROM Portfolios ORDER BY portfolio_balance ASC;

-- ==================== SETTER OPERATIONS ====================

-- def insertPortfolio(portfolio_name, portfolio_balance)
INSERT INTO Portfolios (portfolio_name, portfolio_balance)
VALUES (?, ?);

-- def updatePortfolioName(portfolio_id, portfolio_name)
UPDATE Portfolios
SET portfolio_name = ?
WHERE portfolio_id = ?;

-- def updatePortfolioBalance(portfolio_id, portfolio_balance)
UPDATE Portfolios
SET portfolio_balance = ?
WHERE portfolio_id = ?;

-- def incrementPortfolioBalance(portfolio_id, amount)
UPDATE Portfolios
SET portfolio_balance = portfolio_balance + ?
WHERE portfolio_id = ?;

-- def decrementPortfolioBalance(portfolio_id, amount)
UPDATE Portfolios
SET portfolio_balance = portfolio_balance - ?
WHERE portfolio_id = ?;

-- def deletePortfolio(portfolio_id)
DELETE FROM Portfolios
WHERE portfolio_id = ?;
