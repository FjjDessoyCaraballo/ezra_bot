# Ezra

![](/ezra_preview.png)

Webscrapper application exclusively to retrieve `.zip` files from and old and inactive [website](https://web.archive.org/web/20240222194932/http://brlcenter.org/) to preserve knowledge. This bot is divided into a scrapper and download mode that fetches the HTML body of the old website and retrieves the `href` links, which are saved in a local database to avoid further requests to [Web Archive](https://web.archive.org/) and avoiding wasting resources from both sides and also rate limiting.

## Usage

Ezra contains its own Guided User Interface (GUI) that is quite user-friendly, and displays actions onto the GUI.

Ezra does not use external dependencies. However, for older Ubuntu version, you may need to install Tkinter for the GUI:

```bash
sudo apt install python3-tk
```


As long as you have `Python 3.12.3` you are good to go. Check you python version like this:

```bash
python3 --version
```

If you have the necessary version, then just run the following command:

```bash
python3 ezra.py
```

If you are not even comfortable using terminal, you can use the executable `run_ezra`. It's effectively the same thing as running the script in terminal.

## Constraints

Ezra is very dedicated and can't be closed while downloading files. Be patient.
