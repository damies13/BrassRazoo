
# Brass Razoo Server

The Brass Razoo Server, written purely in python so that it can be run on any OS and any hardware, it should run just as well on a Raspberry Pi as it does on a Xeon server in a data centre.

## First Run

On first run the server will generate it's configuration file, in this file will be the server's ID (a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)), from this point forward this UUID will be used to identify this server.

## OS Upgrade / Moving to new hardware

If you want to move a server, you only need to save and migrate the configuration file and the server will retain the identity of the old server. you will need to ensure the old server is shutdown before starting the new server and ensure the old server cannot be brought back up with it's same UUID.

> [!WARNING]
> Need to determine an method for detecting duplicate servers and determining which is the "original" server with that UUID

## Staking Server

A Staking Server is a server who has had a Brass Razoo stake allocated to it.
