from brownie import AdvancedCollectible, accounts, network, config, interface
import json


def main():
    flatten()


def flatten():
    file = open("./AdvancedCollectible_flattened.json", "w")
