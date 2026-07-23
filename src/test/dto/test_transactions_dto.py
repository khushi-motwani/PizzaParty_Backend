import pytest
from dto.transactions_dto import TransactionsDTO


class TestTransactionsDTO:
    """Test TransactionsDTO functionality."""

    def test_create_transaction_with_all_fields(self):
        """Test creating a transaction with all fields."""
        trans = TransactionsDTO(
            portfolio_id=1,
            asset_id=1,
            transaction_type="BUY",
            transaction_quantity=10,
            transaction_price=150.00,
            transaction_date="2024-01-15",
            transaction_total=1500.00,
            balance_after_transaction=48500.00,
            transaction_id=1
        )
        assert trans.transaction_id == 1
        assert trans.portfolio_id == 1
        assert trans.transaction_type == "BUY"
        assert trans.transaction_quantity == 10

    def test_create_transaction_with_required_field_only(self):
        """Test creating a transaction with only portfolio_id."""
        trans = TransactionsDTO(portfolio_id=1)
        assert trans.portfolio_id == 1
        assert trans.transaction_type == "UNKNOWN"
        assert trans.transaction_quantity == 0
        assert trans.transaction_id is None

    def test_transaction_to_dict(self):
        """Test converting transaction to dictionary."""
        trans = TransactionsDTO(
            portfolio_id=2,
            asset_id=2,
            transaction_type="SELL",
            transaction_quantity=5,
            transaction_id=2
        )
        result = trans.to_dict()

        assert isinstance(result, dict)
        assert result["portfolio_id"] == 2
        assert result["transaction_type"] == "SELL"
        assert result["transaction_quantity"] == 5

    def test_transaction_str_representation(self):
        """Test string representation of transaction."""
        trans = TransactionsDTO(
            portfolio_id=1,
            transaction_type="BUY",
            transaction_quantity=10,
            transaction_id=1
        )
        str_repr = str(trans)

        assert "BUY" in str_repr
        assert "TransactionsDTO" in str_repr
