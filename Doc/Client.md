# Brass Razoo Client

The Brass Razoo Client is planned for development using [Kivy](https://kivy.org/), enabling its deployment as an application for Android, iOS, and desktop environments (Mac, Windows, and Linux).

## QR Codes Workflow

The client features the generation of QR codes for records. If a user wishes to request payment, the following workflow is followed:

1.  The user completes the details of the desired record.
2.  A QR code is generated and presented to the buyer.
3.  The buyer uses their camera to scan the QR code, which loads the record onto their device.
4.  The buyer then confirms or completes the record transaction and makes the payment.

Upon successful completion, both parties will be able to view the finalised record in their respective record lists, along with details of any funds transferred.