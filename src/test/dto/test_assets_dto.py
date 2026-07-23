import pytest
from dto.assets_dto import AssetsDTO


class TestAssetsDTO:
    """Test AssetsDTO functionality."""

    def test_create_asset_with_all_fields(self):
        """Test creating an asset with all fields."""
        asset = AssetsDTO(
            asset_name="Apple Inc.",
            asset_type="STOCK",
            asset_sector="Technology",
            asset_industry="Hardware",
            is_favourite=True,
            asset_id=1
        )
        assert asset.asset_id == 1
        assert asset.asset_name == "Apple Inc."
        assert asset.asset_type == "STOCK"

    def test_create_asset_with_required_field_only(self):
        """Test creating an asset with only asset_name."""
        asset = AssetsDTO(asset_name="Tesla")
        assert asset.asset_name == "Tesla"
        assert asset.asset_type == "UNKNOWN"
        assert asset.asset_id is None

    def test_asset_to_dict(self):
        """Test converting asset to dictionary."""
        asset = AssetsDTO(asset_name="Bitcoin", asset_type="CRYPTO", asset_id=1)
        result = asset.to_dict()

        assert isinstance(result, dict)
        assert result["asset_name"] == "Bitcoin"
        assert result["asset_type"] == "CRYPTO"
        assert result["asset_id"] == 1

    def test_asset_str_representation(self):
        """Test string representation of asset."""
        asset = AssetsDTO(asset_name="Google", asset_type="STOCK", asset_id=2)
        str_repr = str(asset)

        assert "Google" in str_repr
        assert "AssetsDTO" in str_repr
