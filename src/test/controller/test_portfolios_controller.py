from unittest.mock import Mock
from controller.portfolios_controller import get_all_portfolios, get_portfolios_count, set_portfolios_service
from dto.portfolios_dto import PortfoliosDTO


def test_get_all_portfolios(app_context):
    portfolio1 = PortfoliosDTO("My Portfolio", 50000.00)
    portfolio2 = PortfoliosDTO("Growth Portfolio", 100000.00)

    mock_service = Mock()
    mock_service.get_all.return_value = [portfolio1, portfolio2]

    set_portfolios_service(mock_service)
    result = get_all_portfolios()

    data = result.json
    assert len(data) == 2
    assert data[0]["portfolio_name"] == "My Portfolio"
    assert data[1]["portfolio_name"] == "Growth Portfolio"
    mock_service.get_all.assert_called_once()


def test_get_all_portfolios_empty(app_context):
    mock_service = Mock()
    mock_service.get_all.return_value = []

    set_portfolios_service(mock_service)
    result = get_all_portfolios()

    data = result.json
    assert len(data) == 0
    mock_service.get_all.assert_called_once()


def test_get_portfolios_count(app_context):
    mock_service = Mock()
    mock_service.count.return_value = 3

    set_portfolios_service(mock_service)
    result = get_portfolios_count()

    data = result.json
    assert data["count"] == 3
    mock_service.count.assert_called_once()
