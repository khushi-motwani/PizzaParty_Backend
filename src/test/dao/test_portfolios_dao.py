from unittest.mock import Mock
from dao.portfolios_dao import PortfoliosDao


def test_count_portfolios():
    mock_cursor = Mock()
    mock_connection = Mock()
    mock_cursor.fetchall.return_value = [(3,)]
    mock_connection.cursor.return_value = mock_cursor

    dao = PortfoliosDao(mock_connection)
    result = dao.count()

    assert result == 3
    assert dao.total == 3


def test_get_all_portfolios():
    mock_cursor = Mock()
    mock_connection = Mock()
    mock_cursor.fetchall.return_value = [
        (1, "My Portfolio", 50000.00),
        (2, "Growth Portfolio", 100000.00)
    ]
    mock_connection.cursor.return_value = mock_cursor

    dao = PortfoliosDao(mock_connection)
    result = dao.get_all()

    assert len(result) == 2
    assert result[0].portfolio_name == "My Portfolio"
    assert result[1].portfolio_name == "Growth Portfolio"


def test_get_all_empty_table():
    mock_cursor = Mock()
    mock_connection = Mock()
    mock_cursor.fetchall.return_value = []
    mock_connection.cursor.return_value = mock_cursor

    dao = PortfoliosDao(mock_connection)
    result = dao.get_all()

    assert result == []
