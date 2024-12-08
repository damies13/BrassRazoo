# Concepts

## Proof of Stake

Bitcoin and Etherium are proof of work coins, these become very cpu / gpu intensive as the work algorithm becomes more difficult, there are many people criticising proof of work coins for their environmental impact and their lack of sustainability

Brass Razoo is by comparison is more like Etherium2 in that it's a proof of stake coin, coin owners can stake them with a server and a server with 1 or more stakes is selected to create the next block. Stake owners receive a commission on the block as a reward for tying up and risking their coins as the guarantee behind the records in the block.

This Proof of Stake model can run for a long time with each server only using a amount of power.

The design decisions of using python and Proof of Stake, mean that small low power SBC's like a Rasberry Pi or a RISC-V equivalent should be able to run as a Brass Razoo server using a battery and small solar panel.

## Records

A record can be anything, i.e. a sale, an employment contract, a user account, the creation of a piece of art, a rule, etc

There will be rules to verify each type of record (see [Action Engine](Action_Engine.md)), the intention is the rules get created and voted on in the chain, when voted into operation then the rules will verify and enforce the records are created correctly.
