# PROJECT: communication_encryptor

This is a program to encrypt our communication.

## BEFORE START

'communication_encryptor' is licensed under [MIT](./LICENSE).

Copyright © 2024 by Creeper32767

requirements:

1. python environment (no extra libraries is required.)

## HOW TO USE

1. Enter which base system should we use(2 ~ 35).
2. Enter "e" to encode, "d" to decode, or "q" to quit.
3. Enter the content you want to encode or decode.

### EXAMPLE

```
[initialization] Enter which base system should we use(2 ~ 35): 16
++++++++++++++++++++
[command] Enter e(ncode)/d(ecode)/q(uit): e
[content] Input: hello world!
68 65 6C 6C 6F 20 77 6F 72 6C 64 21 


++++++++++++++++++++
[command] Enter e(ncode)/d(ecode)/q(uit): d
[content] Input: 68 65 6C 6C 6F 20 77 6F 72 6C 64 21
hello world!


++++++++++++++++++++
[command] Enter e(ncode)/d(ecode)/q(uit): q
```

## PRINCIPLE

It's completed by getting every character's order in the Unicode Charset and transforming base systems.

## ISSUES

Please give us your ideas through 'issues' part in GitHub.
