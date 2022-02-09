from scripts.helpful_scripts import OPENSEA_URL, get_school, get_account
from brownie import network, AdvancedCollectible

wiz_metadata_dic = {
    "SOT": "https://ipfs.io/ipfs/QmaEyQqx64mVBdZnYAiPsirytBkh9J4Dgu8JjXYm9SNKFW",
    "DOT": "https://ipfs.io/ipfs/QmZwXAaVw8QBEvrrYHZxz1nWoMvDBEP1wWisCdiX6r5RVm",
    "FOT": "https://ipfs.io/ipfs/QmUFMjYARd7WXnzfpumxYcEMkGGC2KukzLT3Zd56uaoENp",
    "WOT": "https://ipfs.io/ipfs/QmZUYM62AfVoEQYUa6Rn26GCvhnJc2bsJ8RCbW3aq4JHRd",
}


def main():
    print(f"working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} token Ids")
    for token_id in range(number_of_collectibles):
        school = get_school(advanced_collectible.tokenIdToSchool(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, wiz_metadata_dic[school])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Good job! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and refresh the metadata")
