![xspamguardbanner](https://github.com/rohsec/X-SpamGuard/assets/63975446/85bf7fcd-06aa-41a3-b2bf-99e9627418de)


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
![xspamguardHelp](https://github.com/rohsec/X-SpamGuard/assets/63975446/99de6d00-b127-4ead-8a3d-10c3bd76ab4a)
![xspamguardWorking](https://github.com/rohsec/X-SpamGuard/assets/63975446/7fcf6f91-fbfe-453b-9b7c-d6cc089c506e)


## License

X-SpamGuard is licensed under the [MIT License](https://github.com/<username>/<repo>/blob/main/LICENSE).

## Contributing

If you would like to contribute to X-SpamGuard, please feel free to fork the repository, make your changes, and submit a pull request. 











