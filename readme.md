### Setup

Read [the Wiki](https://github.com/thejohnhoffer/bewo/wiki) if **copying this project** for use with your own [AWS](https://en.wikipedia.org/wiki/Amazon_Web_Services) endpoints. Otherwise, just [follow our guide to set up a python environment](https://github.com/thejohnhoffer/bearword/wiki/Python-Setup) and run `aws configure` with AWS Access Keys that have access to our endpoints.

### Development

In a bash shell, clone the code base for the `REPO`:

```
REPO="https://github.com/thejohnhoffer/bearword"
git clone $REPO
cd bearword
```

### Local Testing

#### Install DynamoDB

If `java version` does not show a Runtime Environment `>=6.0`, [install java](https://www.java.com/en/download/), then download DynamoDB:

```
wget -qO- https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz | tar xvz -C lib/dynamodb
```

#### Run locally

In one shell session, start the database like this:

```
java -Djava.library.path=./lib/dynamodb/DynamoDBLocal_lib -jar lib/dynamodb/DynamoDBLocal.jar -sharedDb
```

In another shell session, start the app like this:
```
export BEWO_DYNAMO="http://localhost:8000"
export FLASK_APP="blog.py"
flask run
```

### AWS Deployment

When ready, go ahead and deploy to the dev stage!

```
zappa update dev
```
