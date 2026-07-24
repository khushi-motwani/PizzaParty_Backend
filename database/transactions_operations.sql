-- Transactions Table CRUD Operations
USE Portfolio;

-- ==================== GETTER OPERATIONS ====================

-- def getAllTransactions()
SELECT * FROM Transactions ORDER BY transaction_date DESC;

-- def getTransactionById(transaction_id)
SELECT * FROM Transactions WHERE transaction_id = ?;

-- def getTransactionsByPortfolio(portfolio_id)
SELECT * FROM Transactions
WHERE portfolio_id = ?
ORDER BY transaction_date DESC;

-- def getTransactionsByAsset(portfolio_id, asset_id)
SELECT * FROM Transactions
WHERE portfolio_id = ? AND asset_id = ?
ORDER BY transaction_date DESC;

-- def getTransactionsByType(transaction_type)
SELECT * FROM Transactions
WHERE transaction_type = ?
ORDER BY transaction_date DESC;

-- def getTransactionsByDateRange(start_date, end_date)
SELECT * FROM Transactions
WHERE transaction_date BETWEEN ? AND ?
ORDER BY transaction_date DESC;

-- def getTransactionsByPortfolioAndDateRange(portfolio_id, start_date, end_date)
SELECT * FROM Transactions
WHERE portfolio_id = ?
AND transaction_date BETWEEN ? AND ?
ORDER BY transaction_date DESC;

-- def getTransactionCount()
SELECT COUNT(*) as total_transactions FROM Transactions;

-- def getTransactionCountByPortfolio(portfolio_id)
SELECT COUNT(*) as transaction_count FROM Transactions
WHERE portfolio_id = ?;

-- def getTotalTransactionValueByPortfolio(portfolio_id)
SELECT SUM(transaction_total) as total_value FROM Transactions
WHERE portfolio_id = ?;

-- def getAverageTransactionPriceByAsset(asset_id)
SELECT AVG(transaction_price) as avg_price FROM Transactions
WHERE asset_id = ?;

-- def getTransactionSummaryByPortfolio(portfolio_id)
SELECT
    transaction_type,
    COUNT(*) as count,
    SUM(transaction_quantity) as total_quantity,
    SUM(transaction_total) as total_value,
    AVG(transaction_price) as avg_price
FROM Transactions
WHERE portfolio_id = ?
GROUP BY transaction_type;

-- ==================== SETTER OPERATIONS ====================

-- def insertTransaction(portfolio_id, asset_id, transaction_type, transaction_quantity, transaction_price, transaction_date, transaction_total, balance_after_transaction)
INSERT INTO Transactions (portfolio_id, asset_id, transaction_type, transaction_quantity, transaction_price, transaction_date, transaction_total, balance_after_transaction)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);

-- def updateTransaction(transaction_id, transaction_type, transaction_quantity, transaction_price, transaction_total, balance_after_transaction)
UPDATE Transactions
SET transaction_type = ?,
    transaction_quantity = ?,
    transaction_price = ?,
    transaction_total = ?,
    balance_after_transaction = ?
WHERE transaction_id = ?;

-- def deleteTransaction(transaction_id)
DELETE FROM Transactions
WHERE transaction_id = ?;

-- def deleteTransactionsByPortfolio(portfolio_id)
DELETE FROM Transactions
WHERE portfolio_id = ?;
