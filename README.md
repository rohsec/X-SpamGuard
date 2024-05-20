![xspamguardbanner]()

# X-SpamGuard

X-SpamGuard is a command-line utility tool designed for mass muting/blocking of engaggment spammers, reply spammers without the requirment of any premium/paid Twitter API.
The project uses publicly curated list of known enggament spammers who are actively clickbaiting and spamming the comment section with completely unrelated videos from the [X-SpamWatch](https://github.com/rohsec/X-SpamWatch) dataset

## Getting Started

### Prerequisites

X-SpamGuard is built using Python scripting language and requires the following tools to be installed on your system:

- Python3
- requests (pip install requests)

### Installation

Via PyPi:
```
pip install xspamguard
```

### Usage

```
xspamguard -c cookiefile.txt -t Auth_token -m [mute/block]
```
#### Options:
```
X(Twitter) Mass Spam Blocker

options:
  -h, --help            show this help message and exit
  -m {mute,block}, --mode {mute,block}
                        Spam Fight Mode (default: mute)
  -c C, --cookie C      File containing valid cookies
  -t TOKEN, --token TOKEN
                        Your Auth Bearer token

```

## Screnshots


## License

X-SpamGuard is licensed under the [MIT License](https://github.com/<username>/<repo>/blob/main/LICENSE).

## Contributing

If you would like to contribute to X-SpamGuard, please feel free to fork the repository, make your changes, and submit a pull request. 











