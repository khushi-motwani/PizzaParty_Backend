-- Assets Table CRUD Operations
USE Portfolio;

-- ==================== GETTER OPERATIONS ====================

-- def getAllAssets()
SELECT * FROM Assets ORDER BY asset_id;

-- def getAssetById(asset_id)
SELECT * FROM Assets WHERE asset_id = ?;

-- def getAllFavouriteAssets()
SELECT * FROM Assets WHERE is_favourite = TRUE ORDER BY asset_name;

-- def getAssetsByType(asset_type)
SELECT * FROM Assets WHERE asset_type = ? ORDER BY asset_name;

-- def getAssetsBySector(asset_sector)
SELECT * FROM Assets WHERE asset_sector = ? ORDER BY asset_name;

-- def getAssetsByIndustry(asset_industry)
SELECT * FROM Assets WHERE asset_industry = ? ORDER BY asset_name;

-- def getAssetCount()
SELECT COUNT(*) as total_assets FROM Assets;

-- def getFavouriteAssetCount()
SELECT COUNT(*) as favourite_count FROM Assets WHERE is_favourite = TRUE;

-- ==================== SETTER OPERATIONS ====================

-- def insertAsset(asset_id, asset_name, asset_type, asset_sector, asset_industry, is_favourite)
INSERT INTO Assets (asset_id, asset_name, asset_type, asset_sector, asset_industry, is_favourite)
VALUES (?, ?, ?, ?, ?, ?);

-- def updateAsset(asset_id, asset_name, asset_type, asset_sector, asset_industry)
UPDATE Assets
SET asset_name = ?,
    asset_type = ?,
    asset_sector = ?,
    asset_industry = ?
WHERE asset_id = ?;

-- def updateAssetFavouriteStatus(asset_id, is_favourite)
UPDATE Assets
SET is_favourite = ?
WHERE asset_id = ?;

-- def deleteAsset(asset_id)
DELETE FROM Assets
WHERE asset_id = ?;
