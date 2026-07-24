import pytest
from dto.portfolios_dto import PortfoliosDTO


class TestPortfoliosDTO:
    """Test PortfoliosDTO functionality."""

    def test_create_portfolio_with_all_fields(self):
        """Test creating a portfolio with all fields."""
        portfolio = PortfoliosDTO(
            portfolio_name="My Portfolio",
            portfolio_balance=50000.00,
            portfolio_id=1
        )
        assert portfolio.portfolio_id == 1
        assert portfolio.portfolio_name == "My Portfolio"
        assert portfolio.portfolio_balance == 50000.00

    def test_create_portfolio_with_required_field_only(self):
        """Test creating a portfolio with only portfolio_name."""
        portfolio = PortfoliosDTO(portfolio_name="Growth")
        assert portfolio.portfolio_name == "Growth"
        assert portfolio.portfolio_balance == 0
        assert portfolio.portfolio_id is None

    def test_portfolio_to_dict(self):
        """Test converting portfolio to dictionary."""
        portfolio = PortfoliosDTO(portfolio_name="Conservative", portfolio_balance=25000.00, portfolio_id=2)
        result = portfolio.to_dict()

        assert isinstance(result, dict)
        assert result["portfolio_name"] == "Conservative"
        assert result["portfolio_balance"] == 25000.00
        assert result["portfolio_id"] == 2

    def test_portfolio_str_representation(self):
        """Test string representation of portfolio."""
        portfolio = PortfoliosDTO(portfolio_name="Risky", portfolio_balance=100000.00, portfolio_id=3)
        str_repr = str(portfolio)

        assert "Risky" in str_repr
        assert "PortfoliosDTO" in str_repr
