# PervyCliffNotes (NSFW)
Teaching robots to love since 2017. We won't stop until the ghost of Alan Turing says so.

Note (NSFW): This robot has a filthy mouth. Probably shouldn't whip it out during work hours.

# Getting Started

## 1. Obtain credentials for twitter

If you want to contribute, shoot us and email at pervycliffnotes at gmail dot com. We'll then provide the following variables which you can add to your ```~/.bashrc``` file
```
export TWITTER_CONSUMER_TOKEN="abcd"
export TWITTER_CONSUMER_SECRET="efgh"
export TWITTER_ACCESS_TOKEN="ijkl"
export TWITTER_ACCESS_SECRET="mnop"
```
## 2. Setting up python environment

We use [conda](https://conda.io/docs/index.html) to manage our environment. Assuming you have conda installed, use ...
```
conda env create -f environment.yml  # first time you develop
source activate ship_env             # every time you develop
```
