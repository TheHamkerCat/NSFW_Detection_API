# ✨ NSFW Classifier API ✨
Rest API Written In Python To Classify NSFW Images.

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/TheHamkerCat/)

<img src="https://thereader.mitpress.mit.edu/wp-content/uploads/2019/10/nsfw-hed.jpg" width=400 height=200>

## Install Locally Or On A VPS

```sh
$ git clone https://github.com/thehamkercat/NSFW_Detection_API

$ cd NSFW_Detection_API

$ pip3 install -U -r requirements.txt

$ python3 -m api
```

## Docker

```sh
$ git clone https://github.com/thehamkercat/NSFW_Detection_API

$ cd NSFW_Detection_API

$ docker-compose up -d
```


## Usage 

```sh
$ curl --request GET \
  --url 'http://localhost:8001/?url=https%3A%2F%2Fcdn.stocksnap.io%2Fimg-thumbs%2F960w%2Fwoman-model_LCPHH1BDI2.jpg'
```

## Classifies

* **Hentai** - Hentai and pornographic drawings
* **Porn** - Pornographic images, sexual acts
* **Drawings** - Safe for work drawings (including anime)
* **Neutral** - Safe for work neutral images
* **Sexy** - Sexually explicit images, not pornography

# Credits

Thanks to https://github.com/GantMan/nsfw_model/ for their model.
