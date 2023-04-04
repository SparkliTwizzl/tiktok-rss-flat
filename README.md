![TikTok RSS Logo](https://tiktokrss.conoroneill.com/favicon-32x32.png)
# TikTok RSS Using GitHub OCTO Flat Data

## index

- [iamtabithabrown](https://tiktokrss.uselesslesbians.gay/rss/iamtabithabrown.xml)
- [mirandagoesoutside](https://tiktokrss.uselesslesbians.gay/rss/mirandagoesoutside.xml)
- [scottseiss](https://tiktokrss.uselesslesbians.gay/rss/scottseiss.xml)
- [texasbeeworks](https://tiktokrss.uselesslesbians.gay/rss/texasbeeworks.xml)
- [visitballyhoura](https://tiktokrss.uselesslesbians.gay/rss/visitballyhoura.xml)

## about

**NOTE January 2023: This is now working again due to an alternative TikTok library.**

* Generate usable RSS feeds from TikTok using [GitHub OCTO Flat Data](https://octo.github.com/projects/flat-data), GitHub Actions and GitHub Pages.

* This uses a newer unoffical [TikTokPy library](https://github.com/Russell-Newton/TikTokPy) to extract information about user videos from TikTok as JSON and generate RSS feeds for each user you are interested in.

* To get your own instance running
    * Fork this repo 
    * Enable GitHub Pages for your new repo
    * Change the `ghPagesURL` in postprocessing.py from "https://conoro.github.io/tiktok-rss-flat/" to your URL
    * Add the TikTok usernames that you like to subscriptions.csv
    * Make sure to enable Actions in the Actions tab 

* It's set to run once per hour and generates one RSS XML file per user in the rss output directory.

* You then subscribe to each feed in [Feedly](https://www.feedly.com) or another feed reader using a GitHub Pages URL. Those URLs are constructed like so. E.g.:

    * TikTok User = iamtabithabrown
    * XML File = rss/iamtabithabrown.xml
    * Feedly Subscription URL = https://conoro.github.io/tiktok-rss-flat/rss/iamtabithabrown.xml
    * (Or in my case where I've set a custom domain for the GitHub Pages project called tiktokrss.conoroneill.com, the URL is https://tiktokrss.conoroneill.com/rss/iamtabithabrown.xml)

Logo was created using the TikTok and RSS [Font Awesome](https://fontawesome.com/license/free) icons via CC BY 4.0 License

Copyright Conor O'Neill, 2021 (conor@conoroneill.com)

License Apache 2.0

