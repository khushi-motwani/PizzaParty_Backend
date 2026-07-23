-- Transactions Table CRUD Operations
USE Portfolio;

-- ==================== GETTER OPERATIONS ====================

-- Get all transactions
SELECT * FROM Transactions ORDER BY transaction_date DESC;

-- Get transaction by ID
SELECT * FROM Transactions WHERE transaction_id = 1;

-- Get all transactions for a portfolio
SELECT * FROM Transactions
WHERE portfolio_id = 1
ORDER BY transaction_date DESC;

-- Get transactions for a specific asset in a portfolio
SELECT * FROM Transactions
WHERE portfolio_id = 1 AND asset_id = 'ASSET001'
ORDER BY transaction_date DESC;

-- Get transactions by type (BUY, SELL, etc.)
SELECT * FROM Transactions
WHERE transaction_type = 'BUY'
ORDER BY transaction_date DESC;

-- Get transactions within a date range
SELECT * FROM Transactions
WHERE transaction_date BETWEEN '2024-01-01' AND '2024-12-31'
ORDER BY transaction_date DESC;

-- Get transactions for a portfolio within a date range
SELECT * FROM Transactions
WHERE portfolio_id = 1
AND transaction_date BETWEEN '2024-01-01' AND '2024-12-31'
ORDER BY transaction_date DESC;

-- Get transaction count
SELECT COUNT(*) as total_transactions FROM Transactions;

-- Get transaction count for a portfolio
SELECT COUNT(*) as transaction_count FROM Transactions
WHERE portfolio_id = 1;

-- Get total transaction value for a portfolio
SELECT SUM(transaction_total) as total_value FROM Transactions
WHERE portfolio_id = 1;

-- Get average transaction price for an asset
SELECT AVG(transaction_price) as avg_price FROM Transactions
WHERE asset_id = 'ASSET001';

-- Get buy vs sell summary for a portfolio
SELECT
    transaction_type,
    COUNT(*) as count,
    SUM(transaction_quantity) as total_quantity,
    SUM(transaction_total) as total_value,
    AVG(transaction_price) as avg_price
FROM Transactions
WHERE portfolio_id = 1
GROUP BY transaction_type;

-- ==================== SETTER OPERATIONS ====================

-- Insert a new transaction
INSERT INTO Transactions (portfolio_id, asset_id, transaction_type, transaction_quantity, transaction_price, transaction_date, transaction_total, balance_after_transaction)
VALUES (1, 'ASSET001', 'BUY', 10, 150.5000, '2024-01-15 10:30:00', 1505.00, 8495.00);

-- Update transaction
UPDATE Transactions
SET transaction_type = 'SELL',
    transaction_quantity = 5,
    transaction_price = 155.2500,
    transaction_total = 776.25,
    balance_after_transaction = 9271.25
WHERE transaction_id = 1;

-- Delete a transaction
DELETE FROM Transactions
WHERE transaction_id = 1;

-- Delete all transactions for a portfolio
DELETE FROM Transactions
WHERE portfolio_id = 1;
