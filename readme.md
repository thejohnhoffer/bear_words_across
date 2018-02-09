### Setup

Read [the Wiki](https://github.com/thejohnhoffer/bewo/wiki) if **copying this project** to use your own [AWS](https://en.wikipedia.org/wiki/Amazon_Web_Services) endpoints. Otherwise, just [follow our guide](https://github.com/thejohnhoffer/bewo/wiki/Python-Setup) to set up a python environment and run `aws configure` with your own AWS Access Keys.

### Development

In your favorite shell, clone the main code base:
```
git clone https://github.com/thejohnhoffer/bewo
cd bewo
```

When you've made changes, go ahead and deploy to the dev stage!

```
zappa update dev
```
