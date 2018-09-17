# Crime-Probem-Encryption-through-compression-
Python code for extracting secret data from compression oracles such as those exploited by the BREACH and CRIME attacks.

# Problem statement

Some criminals are running a message encryption service at crime.cse545.rev.fish:30925. You, as an intelligent hacker, should talk to that service and recover the plain text message from the encrypted message it gives you.


Our intelligence team infiltrated their server and leaked a page from their manual. It seems that this service appends your message to their secret message before it compresses the entire message and then encrypts the compressed message.
Our intelligence team believes that the crypto algorithm involved is secure.
The original, unencrypted message only contains printable ASCII characters (or string.printable in Python 2).
The length of the secret message is 75.
