# Staking Protocol

## Minimum Stake Size

The minimum stake size is 1,000,000.00 Brass Razoos.

## Stake Management Rules

**Ownership and Financial Guarantee**
*   The ownership of the Brass Razoos always remains with the individual who staked them.
*   The stake holder provides a financial guarantee that the associated record adheres to all stipulated rules.

**Transaction Rules**
*   A staked amount cannot be spent until it has been successfully de-staked.

**De-Staking**
*   to initiate the de-staking process the stake holder lists the stake as unavailable
*   Once the last block the stake was used on has been crtified by 5 or more servers, a staked amount can be considerd de-staked and returned to the stake holder as usable funds.

**Security and Recovery**
*   Staking servers will validate the entire block chain on startup
*   Staking servers will validate the proposed blocks as they are received and broadcast to the shard block IDs that failed validation along with the record IDs that triggered the failure
*   Staking servers will validate the proposed block before before creating a new block based on that proposed block
*   Staking servers will validate the blocks the proposed block is based on are valid or have had any invalid records corrected in subsequent blocks
*   Should a subsequent staking server identify a record in the chain as invalid, the server will attempt to reverse the record. If reversal fails, the stake is utilised to provide any necessary refunds.
*   By proprosing a new block the staking server is certifying all the previous blocks in the chain have been validated
*   Once a block is certified by 2 or more servers a reversal requires a vote to determine it as invalid

**Incentives**
*   The stake holder will receive a commission on every block generated using their stake.

**Stake Holder Prerequisite**
*   Stake holders must exercise due diligence and trust the server with whom they are staking their funds.