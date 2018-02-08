Mimicking [this](https://serverlessblog.com/)

### Pip Setup

```
pyenv global 3.6.0
pyenv virtualenv bear_words_across
pyenv local bear_words_across
pip install zappa flask awscli
pip install flask-blogging
```

### AWS Setup

[Set up AWSCLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

- Add [new user](https://console.aws.amazon.com/iam/home#/users)
  - (Optional?) Add user to `AWSLambdaFullAccess`
  - (Optional?) Add user to `AdministratorAccess`
  - (Optional?) Add user to `AmazonDynamoDBFullAccess`

Configure local aws with new user Acess Keys:

```
aws configure
```

### Zappa deploy

```
zappa init
zappa deploy dev
```

- [DyanmoDB Full Access Policy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess$serviceLevelSummary?section=attached_entities)
  - attach policy to bewo-dev-ZappaLambdaExecutionRole

On the [API Gateway dashboard](https://us-east-2.console.aws.amazon.com/apigateway/home) choose Resources, click Actions and choose Deploy API

## Development

```
zappa update dev
```
