# weblog-filter
Small utility to filter web logs based on an IP or a CIDR

## How To Setup

You need Python3 to use this utility. You can use your package manager to install it for you or download and install from [https://www.python.org/downloads/](https://www.python.org/downloads/). Use `brew install python3` for Mac. Linux folks have it by default most of the time, and if not, you are smart enough to install it by yourself.

- Clone the repo and add execute permissions to the `weblog_helper` file.
```
> git clone git@github.com:nkmadusanka/weblog-filter.git
> cd weblog-filter
> chmod +x weblog_helper
```
- If you have regular usage of this utility, it will be much easier if you add this script as a regular command available on your shell. Either you can copy to `/usr/local/bin/` use your own directory and add it to the PATH variable on your `bash`/`zsh` profiles.

For zsh fans
```
> mkdir ~/.mybin
> cp weblog_helper ~/.mybin
> echo "export PATH=$PATH:$HOME/.mybin" > ~/.zshrc
> source ~/.zshrc
```

## Usage

```
weblog_helper --ip <IP address or CIDR> --log <Webserver log file>
weblog_helper -i <IP address or CIDR> -l <Webserver log file>

--ip / -i : IP address or CIDR to filter the logs
--log / -l : Webserver log file
```
