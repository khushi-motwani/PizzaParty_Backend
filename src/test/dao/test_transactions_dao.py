import pytest
from unittest.mock import MagicMock, patch
from dao.transactions_dao import TransactionsDao


class TestTransactionsDao:
    """Test TransactionsDao functionality."""

    @patch('dao.transactions_dao.get_db_connection')
    def test_count_transactions(self, mock_get_db):
        """Test counting total transactions."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(10,)]

        dao = TransactionsDao()
        result = dao.count()

        assert result == 10
        assert dao.total == 10

    @patch('dao.transactions_dao.get_db_connection')
    def test_get_all_transactions(self, mock_get_db):
        """Test retrieving all transactions."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            (1, 1, 1, "BUY", 10, 150.00, "2024-01-15", 1500.00, 48500.00),
            (2, 1, 2, "SELL", 5, 250.00, "2024-01-20", 1250.00, 49750.00)
        ]

        dao = TransactionsDao()
        result = dao.get_all()

        assert len(result) == 2
        assert result[0].transaction_type == "BUY"
        assert result[1].transaction_type == "SELL"

    @patch('dao.transactions_dao.get_db_connection')
    def test_get_all_empty_table(self, mock_get_db):
        """Test retrieving transactions from empty table."""
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []

        dao = TransactionsDao()
        result = dao.get_all()

        assert result == []
