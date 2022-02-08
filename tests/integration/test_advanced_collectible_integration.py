from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
)
from brownie import network
import pytest
import time
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():
    # Deploy
    # Create NFT
    # Get a random breed
    # Arrang
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # Act
    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
