from unittest.mock import Mock
from controller.assets_controller import get_all_assets, get_assets_count, set_assets_service
from dto.assets_dto import AssetsDTO


def test_get_all_assets(app_context):
    asset1 = AssetsDTO("Apple", "STOCK", "Technology", "Hardware", 1)
    asset2 = AssetsDTO("Tesla", "STOCK", "Consumer", "Auto", 0)

    mock_service = Mock()
    mock_service.get_all.return_value = [asset1, asset2]

    set_assets_service(mock_service)
    result = get_all_assets()

    data = result.json
    assert len(data) == 2
    assert data[0]["asset_name"] == "Apple"
    assert data[1]["asset_name"] == "Tesla"
    mock_service.get_all.assert_called_once()


def test_get_all_assets_empty(app_context):
    mock_service = Mock()
    mock_service.get_all.return_value = []

    set_assets_service(mock_service)
    result = get_all_assets()

    data = result.json
    assert len(data) == 0
    mock_service.get_all.assert_called_once()


def test_get_assets_count(app_context):
    mock_service = Mock()
    mock_service.count.return_value = 5

    set_assets_service(mock_service)
    result = get_assets_count()

    data = result.json
    assert data["count"] == 5
    mock_service.count.assert_called_once()
