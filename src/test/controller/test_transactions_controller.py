from unittest.mock import patch
from controller.transactions_controller import get_all_transactions, get_transactions_count
from dto.transactions_dto import TransactionsDTO


@patch('controller.transactions_controller.transactions_service')
def test_get_all_transactions(mock_service, app_context):
    transaction1 = TransactionsDTO(1, "BUY", 10, "2024-01-15", 1500.00, 48500.00)
    transaction2 = TransactionsDTO(2, "SELL", 5, "2024-01-20", 1250.00, 49750.00)

    mock_service.get_all.return_value = [transaction1, transaction2]

    result = get_all_transactions()

    data = result.json
    assert len(data) == 2
    assert data[0]["transaction_type"] == "BUY"
    assert data[1]["transaction_type"] == "SELL"
    mock_service.get_all.assert_called_once()


@patch('controller.transactions_controller.transactions_service')
def test_get_all_transactions_empty(mock_service, app_context):
    mock_service.get_all.return_value = []

    result = get_all_transactions()

    data = result.json
    assert len(data) == 0
    mock_service.get_all.assert_called_once()

@patch('controller.transactions_controller.transactions_service')
def test_get_transactions_count(mock_service, app_context):
    mock_service.count.return_value = 10

    result = get_transactions_count()

    data = result.json
    assert data["count"] == 10
    mock_service.count.assert_called_once()
