-- Assets Table CRUD Operations
USE Portfolio;

-- ==================== GETTER OPERATIONS ====================

-- Get all assets
SELECT * FROM Assets ORDER BY asset_id;

-- Get asset by ID
SELECT * FROM Assets WHERE asset_id = 'ASSET_ID';

-- Get all favourite assets
SELECT * FROM Assets WHERE is_favourite = TRUE ORDER BY asset_name;

-- Get assets by type
SELECT * FROM Assets WHERE asset_type = 'STOCK' ORDER BY asset_name;

-- Get assets by sector
SELECT * FROM Assets WHERE asset_sector = 'TECHNOLOGY' ORDER BY asset_name;

-- Get assets by industry
SELECT * FROM Assets WHERE asset_industry = 'SOFTWARE' ORDER BY asset_name;

-- Get count of assets
SELECT COUNT(*) as total_assets FROM Assets;

-- Get count of favourite assets
SELECT COUNT(*) as favourite_count FROM Assets WHERE is_favourite = TRUE;

-- ==================== SETTER OPERATIONS ====================

-- Insert a new asset
INSERT INTO Assets (asset_id, asset_name, asset_type, asset_sector, asset_industry, is_favourite)
VALUES ('ASSET001', 'Apple Inc', 'STOCK', 'TECHNOLOGY', 'SOFTWARE', FALSE);

-- Update asset details
UPDATE Assets
SET asset_name = 'New Name',
    asset_type = 'STOCK',
    asset_sector = 'TECHNOLOGY',
    asset_industry = 'SOFTWARE'
WHERE asset_id = 'ASSET001';

-- Update favourite status
UPDATE Assets
SET is_favourite = TRUE
WHERE asset_id = 'ASSET001';

-- Delete an asset
DELETE FROM Assets
WHERE asset_id = 'ASSET001';
