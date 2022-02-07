from scripts.helpful_scripts import get_account, SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qme72SJca9yPyVcCH8smUovatM2Mwbgq5Tr8YGPoKicbuK?filename=0wotwizard.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button.")
