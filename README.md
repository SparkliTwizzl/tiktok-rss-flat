![TikTok RSS Logo](https://tiktokrss.uselesslesbians.gay/favicon-32x32.png)
# TikTok RSS Using GitHub OCTO Flat Data

**NOTE January 2023: This is now working again due to an alternative TikTok library.**

* Generate usable RSS feeds from TikTok using [GitHub OCTO Flat Data](https://octo.github.com/projects/flat-data), GitHub Actions and GitHub Pages.

* This uses a newer unoffical [TikTokPy library](https://github.com/Russell-Newton/TikTokPy) to extract information about user videos from TikTok as JSON and generate RSS feeds for each user you are interested in.

* To get your own instance running
	* Fork this repo 
	* Enable GitHub Pages for your new repo
	* Change the `ghPagesURL` in postprocessing.py from "https://conoro.github.io/tiktok-rss-flat/" to your URL
	* Add the TikTok usernames that you like to subscriptions.csv
	* Set Actions to be allowed under Settings -> Actions -> General -> Actions Permissions
	* Set Workflow permissions to read-write under Settings -> Actions -> General -> Workflow Permissions

* It's set to run twice per hour and generates one RSS XML file per user in the rss output directory.

* You then subscribe to each feed in [Feedly](https://www.feedly.com) or another feed reader using a GitHub Pages URL. Those URLs are constructed like so. E.g.:

	* TikTok User = iamtabithabrown
	* XML File = rss/iamtabithabrown.xml
	* Feedly Subscription URL = https://conoro.github.io/tiktok-rss-flat/rss/iamtabithabrown.xml
	* (Or in my case where I've set a custom domain for the GitHub Pages project called tiktokrss.conoroneill.com, the URL is https://tiktokrss.conoroneill.com/rss/iamtabithabrown.xml)

Logo was created using the TikTok and RSS [Font Awesome](https://fontawesome.com/license/free) icons via CC BY 4.0 License

Copyright Conor O'Neill, 2021 (conor@conoroneill.com)

License Apache 2.0

