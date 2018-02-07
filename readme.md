Mimicking [this](https://serverlessblog.com/)

### Pip Setup

```
pyenv global 3.6.0
pyenv virtualenv bear_words_across
pip install zappa flask awscli
pip install flask_blogging
pip install flask_login
```

### AWS Setup

[Set up AWSCLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

```
aws configure
```

### Zappa deploy

```
zappa init
zappa deploy dev
```

## Development

```
zappa update dev
```
