[![Build Status](https://travis-ci.org/0x64746b/ctx_parser.svg?branch=master)](https://travis-ci.org/0x64746b/ctx_parser)
[![Coverage Status](https://img.shields.io/coveralls/0x64746b/ctx_parser.svg)](https://coveralls.io/r/0x64746b/ctx_parser)

About
=====

`ctx_parser` is a parser written with
[pyparsing](http://pyparsing.wikispaces.com/) for the `.ctx` format used by
[AqBanking](http://www.aquamaniac.de/sites/aqbanking/cli.php).

Usage
=====

```
In [1]: from ctx_parser import parser

In [2]: accounts = parser.LIST.parseFile('accounts.ctx')

In [3]: accounts.accountInfoList[0].accountNumber
Out[3]: '987654300'

In [4]: accounts.accountInfoList[0].accountId
Out[4]: 0

In [5]: accounts.accountInfoList[0].statusList[0].bookedBalance.value.value
Out[5]: 23.42

In [6]: accounts.accountInfoList[0].statusList[0].bookedBalance.time
Out[6]: datetime.datetime(2014, 5, 4, 1, 42, 23)
```

where `accounts.ctx` contains a `LIST` of (more or less) complex elements:

```
% cat accounts.ctx
accountInfoList {
  accountInfo {
    char bankCode="12345678"
    char bankName="Bad Bank"
    char accountNumber="987654300"
    char accountName="personal account"
    char iban="CC42123456780987654300"
    char bic="COUNCOBB423"
    char owner="Smith, John"
    char currency="USD"
    int  accountType="0"
    int  accountId="0"

    statusList {
      status {
        int  time="1399068000"

        bankLine {
          char value="1000"
          char currency="USD"
        } #bankLine

        bookedBalance {
          value {
            char value="2342%2F100"
            char currency="USD"
          } #value

          int  time="1399068000"
        } #bookedBalance
      } #status
    } #statusList
  } #accountInfo
} #accountInfoList
%
```

Disclaimer
==========

The grammar for this parser has been extrapolated from example files and may,
although tending to underfit the perceived rules, be unable to describe
constructs I didn't foresee/encounter.

If you come across an unparsable `.ctx` file, feel free to file an issue,
providing a reproducing example. Better yet, fork, add a reproducing test,
extend the parser and send a pull request :)

Let me know how it goes,
dtk
