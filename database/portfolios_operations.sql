-- Portfolios Table CRUD Operations
USE Portfolio;

-- ==================== GETTER OPERATIONS ====================

-- Get all portfolios
SELECT * FROM Portfolios ORDER BY portfolio_id;

-- Get portfolio by ID
SELECT * FROM Portfolios WHERE portfolio_id = 1;

-- Get portfolio balance
SELECT portfolio_id, portfolio_name, portfolio_balance
FROM Portfolios
WHERE portfolio_id = 1;

-- Get total balance across all portfolios
SELECT SUM(portfolio_balance) as total_balance FROM Portfolios;

-- Get portfolio count
SELECT COUNT(*) as total_portfolios FROM Portfolios;

-- Get portfolios sorted by balance (highest first)
SELECT * FROM Portfolios ORDER BY portfolio_balance DESC;

-- Get portfolios sorted by balance (lowest first)
SELECT * FROM Portfolios ORDER BY portfolio_balance ASC;

-- ==================== SETTER OPERATIONS ====================

-- Insert a new portfolio
INSERT INTO Portfolios (portfolio_name, portfolio_balance)
VALUES ('My Portfolio', 10000.00);

-- Update portfolio name
UPDATE Portfolios
SET portfolio_name = 'New Portfolio Name'
WHERE portfolio_id = 1;

-- Update portfolio balance
UPDATE Portfolios
SET portfolio_balance = 15000.00
WHERE portfolio_id = 1;

-- Increment portfolio balance
UPDATE Portfolios
SET portfolio_balance = portfolio_balance + 5000.00
WHERE portfolio_id = 1;

-- Decrement portfolio balance
UPDATE Portfolios
SET portfolio_balance = portfolio_balance - 2000.00
WHERE portfolio_id = 1;

-- Delete a portfolio
DELETE FROM Portfolios
WHERE portfolio_id = 1;
