import pytest
from unittest.mock import MagicMock, patch
from dao.assets_dao import AssetsDao


class TestAssetsDao:
    """Test AssetsDao functionality."""

    @patch('dao.assets_dao.get_db_connection')
    def test_count_assets(self, mock_get_db):
        """Test counting total assets."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(5,)]

        dao = AssetsDao()
        result = dao.count()

        assert result == 5
        assert dao.total == 5

    @patch('dao.assets_dao.get_db_connection')
    def test_get_all_assets(self, mock_get_db):
        """Test retrieving all assets."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            (1, "Apple", "STOCK", "Technology", "Hardware", 1),
            (2, "Tesla", "STOCK", "Consumer", "Auto", 0)
        ]

        dao = AssetsDao()
        result = dao.get_all()

        assert len(result) == 2
        assert result[0].asset_name == "Apple"
        assert result[1].asset_name == "Tesla"

    @patch('dao.assets_dao.get_db_connection')
    def test_get_all_empty_table(self, mock_get_db):
        """Test retrieving assets from empty table."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []

        dao = AssetsDao()
        result = dao.get_all()

        assert result == []
        assert len(result) == 0
