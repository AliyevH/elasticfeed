From csv into Elasticsearch

[![MIT licensed](https://img.shields.io/github/license/aliyevH/elasticfeed)](https://raw.githubusercontent.com/aliyevH/elasticfeed/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/aliyevH/elasticfeed.svg)](https://github.com/aliyevH/elasticfeed/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aliyevH/elasticfeed.svg)](https://github.com/aliyevH/elasticfeed/network)
[![GitHub issues](https://img.shields.io/github/issues-raw/aliyevH/elasticfeed)](https://github.com/aliyevH/elasticfeed/issues)
[![Downloads](https://pepy.tech/badge/elasticfeed)](https://pepy.tech/project/elasticfeed)


###  🔨  Installation ###

```sh
 $ sudo pip3 install elasticfeed
```


### 🕹 Guide

```bash

elasticfeed  --help 

```

```bash

elasticfeed  --host 127.0.0.1 --port 9200 <full filepath>

```

```python
from elastic_feeder.controller import FeedElastic
```
```python
fd = FeedElastic(
        host="hostname or ip address", 
        port="port",
        filename="<full path>",
        index="index name",
        properties={
            "some-name": {
                "type": "some-type",
            },
             "some-name": {
                "type": "some-type",

            },
             "some-name": {
                "type": "some-type",

            }
```
```python
fd.run()
```


## Supported OS
Linux, MacOS


## 🌱 Contributing
Feel free to open issue and send pull request.

### elasticfeed  supports Python >= 3.6