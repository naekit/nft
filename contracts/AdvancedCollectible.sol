// SPDX-License-Identifier: MIT

// NFT CONTRACT
// The tokenURI can be on of 3 different images
// Randomly selected

pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    enum School {
        WOT,
        FOT,
        DOT,
        SOT
    }
    mapping(uint256 => School) public tokenIdToSchool;
    mapping(bytes32 => address) public requestIdToSender;

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 _fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("wizard", "WIZ")
    {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible(string memory tokenURI)
        public
        returns (bytes32)
    {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        School school = School(randomNumber % 4);
        uint256 newTokenId = tokenCounter;
        tokenIdToSchool[newTokenId] = school;
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        // _setTokenURI(newTokenId, tokenURI);
        tokenCounter = tokenCounter + 1;
    }
}
