#!/usr/bin/python

import requests

PRODUCTS = ("firefox", "firefox-os", "mobile")

LANGUAGES = (
    'ach',
    'ak',
    'ar',
    'as',
    'az',
    'be',
    'bg',
    'bn-BD',
    'bn-IN',
    'bs',
    'ca',
    'cs',
    'da',
    'de',
    'el',
    'en-US',
    'eo',
    'es',
    'et',
    'eu',
    'fa',
    'ff',
    'fi',
    'fr',
    'fy-NL',
    'ga-IE',
    'gd',
    'gu-IN',
    'he',
    'hi-IN',
    'hr',
    'hu',
    'hy-AM',
    'id',
    'ilo',
    'is',
    'it',
    'ja',
    'kk',
    'km',
    'kn',
    'ko',
    'lg',
    'lt',
    'mai',
    'mk',
    'ml',
    'mn',
    'mr',
    'ms',
    'my',
    'nb-NO',
    'ne-NP',
    'nl',
    'no',
    'nso',
    'pa-IN',
    'pl',
    'pt-BR',
    'pt-PT',
    'rm',
    'ro',
    'ru',
    'rw',
    'sah',
    'si',
    'sk',
    'sl',
    'son',
    'sq',
    'sr-Cyrl',
    'sr-Latn',
    'sv',
    'sw',
    'ta-LK',
    'ta',
    'te',
    'th',
    'tr',
    'uk',
    'vi',
    'zh-CN',
    'zh-TW',
    'zu',
)
def main(baseurl):
  bundle_url = baseurl + "/offline/get-bundle"
  meta_url = baseurl + "/offline/bundle-meta"
  languages_url = baseurl + "/offline/get-languages"

  print "Getting languages"
  l = requests.get(languages_url)
  with open("files/languages.json", "w") as f:
    f.write(l.text)

  for product in PRODUCTS:
    for locale in LANGUAGES:
      print "Getting {} {}".format(locale, product)
      b = requests.get(bundle_url, params={"locale": locale, "product": product})
      if b.status_code != 200:
        raise Exception("getting failed")
      with open("files/bundles/{}-{}.json".format(locale, product), "w") as f:
        f.write(b.text)

      m = requests.get(meta_url, params={"locale": locale, "product": product})
      if m.status_code != 200:
        raise Exception("getting failed")
      with open("files/meta/{}-{}.json".format(locale, product), "w") as f:
        f.write(m.text)

if __name__ == "__main__":
  import sys
  main(sys.argv[1])
