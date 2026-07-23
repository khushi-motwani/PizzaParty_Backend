import pytest
from unittest.mock import MagicMock, patch
from dao.portfolios_dao import PortfoliosDao


class TestPortfoliosDao:
    """Test PortfoliosDao functionality."""

    @patch('dao.portfolios_dao.get_db_connection')
    def test_count_portfolios(self, mock_get_db):
        """Test counting total portfolios."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(3,)]

        dao = PortfoliosDao()
        result = dao.count()

        assert result == 3
        assert dao.total == 3

    @patch('dao.portfolios_dao.get_db_connection')
    def test_get_all_portfolios(self, mock_get_db):
        """Test retrieving all portfolios."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            (1, "My Portfolio", 50000.00),
            (2, "Growth Portfolio", 100000.00)
        ]

        dao = PortfoliosDao()
        result = dao.get_all()

        assert len(result) == 2
        assert result[0].portfolio_name == "My Portfolio"
        assert result[1].portfolio_name == "Growth Portfolio"

    @patch('dao.portfolios_dao.get_db_connection')
    def test_get_all_empty_table(self, mock_get_db):
        """Test retrieving portfolios from empty table."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []

        dao = PortfoliosDao()
        result = dao.get_all()

        assert result == []
