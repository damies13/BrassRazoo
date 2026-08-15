# Brass Razoo Client

The Brass Razoo Client is planned for development using [Kivy](https://kivy.org/), enabling its deployment as an application for Android, iOS, and desktop environments (Mac, Windows, and Linux).

## QR Codes Workflow

The client features the generation of QR codes for records. If a user wishes to request payment, the following workflow is followed:

1.  The user completes the details of the desired record.
2.  A QR code is generated and presented to the buyer.
3.  The buyer uses their camera to scan the QR code, which loads the record onto their device.
4.  The buyer then confirms or completes the record transaction and makes the payment.

Upon successful completion, both parties will be able to view the finalised record in their respective record lists, along with details of any funds transferred.

## Private Data

A record may contain Private Data and Algorithm keys, these are used for storing data that should not be public. 

The client will encrypt the data on the client side and put the encrypted data in the Private Data field with the encryption algorithm used in the Algorithm field.

For a user record the user's passphrase should be used to encrypt the private data, this pass phrase should remain on the client.

For other record types the pass phrases used to encrypt the private data may be stored in the user's private data.

It is recomended that clients use AES-256-GCM or higher encryption levels for data security. Some encryption algorithms suggest/require a Nonce (Initialisation Vector) for the encryption, if used this should be included in the record's data.

The server is only responsible for storing this data not for extracting it.

## The Key Lifecycle

The client is responsible for generating private / public key pairs, as private keys should not be made public they can be stored in the users private data. The users's public keys can be stored in the base record.

## Logging In

Brass Razoo servers don't prvide authentication, to "Log In" a client will download and cache a users record, use the users pass phase to unlock the users Private data and gain access to the private keys needed for signing records.

The server does not need to validate users, the signature, signed with the private key is the validation and can be checked with the users known public key.

## Shared Private Data

In situations where records have private data that needs to be shared between 2 or more users, the private data should be encrypted with a passpharse that has been previously agreeed between the parties (not the same as the users own pass phrase). This record specific pass phrase may be storesd in the users private data with the record ID that it applies to.

Some examples where this may appliy:
 - Employment contracts where employee details such as date of birth and home address are included but should not be made public
 - Sale of a house or car where the buyer and sellers details should not be public
 - A family photo album where the photos should only be viewable by family members but not by the public, in this case for improved perfromance, each photo should be a seperate record, but the pass phrase could be the same for all photos records, Each photo record should carry a Group ID field and the users private data would contain the pass phrase stored with the Group ID rather than storring the pass phrase repetativly for every photo record.
