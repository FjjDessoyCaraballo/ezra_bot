# Ezra_bot

![](/ezra_preview.png)

Webscrapper application exclusively to retrieve `.zip` files from and old and inactive [website](https://web.archive.org/web/20240222194932/http://brlcenter.org/) to preserve knowledge. This bot is divided into a crawler/scrapper mode that fetches the HTML body of the old website and retrieves the `href` links.

## Usage

Ezra does not use external dependencies. As long as you have `Python 3.12.3` you are good to go. Check you python version like this:

```bash
python3 --version
```

If you have the necessary version, then just run the following command:

```bash
python3 ezra.py
```