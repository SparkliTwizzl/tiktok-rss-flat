import asyncio
import csv
from datetime import datetime, timezone
from feedgen.feed import FeedGenerator
from tiktokapipy.async_api import AsyncTikTokAPI

# Now using a new TikTok library https://github.com/Russell-Newton/TikTokPy

# Normal GitHub Pages URL
# ghPagesURL = "https://sparklitwizzl.github.io/tiktok-rss-flat/"

# Custom Domain
ghPagesURL = "https://tiktokrss.uselesslesbians.gay/"

maxItems = 10
subscriptionFileCount = 4


async def runAll():
	try:
		print( '-------------------- runAll start --------------------' )
		
		currentFileNumber = 0
		print( f'-------------------- attempt to load subscription file number to run --------------------' )
		with open( 'nextSubscriptionFileToRun.py' ) as f:
			currentFileNumber = f.read()
			print( f'-------------------- currentFileNumber = {currentFileNumber} --------------------' )
		
		fileToRun = 'subscriptions' + currentFileNumber + '.csv'
		print( f'-------------------- fileToRun = {fileToRun} --------------------' )
		
		with open( fileToRun ) as f:
			# TODO: Switch to 3.11 TaskGroup or trio nursery
			await asyncio.gather( *[
				run( row['username'] ) for row in csv.DictReader( f, fieldnames=['username'] ) ] )
		
		nextFileNumber = int( currentFileNumber ) + 1
		if ( nextFileNumber > subscriptionFileCount ):
			nextFileNumber = 1
		print( f'-------------------- nextFileNumber = {nextFileNumber} --------------------' )
		
		print( f'-------------------- attempt to store next subscription file number to run \( subscriptions{nextFileNumber}.csv\ ) --------------------' )
		with open( 'nextSubscriptionFileToRun.py' ) as f:
			f.write( str( nextFileNumber ) )
	except Exception as e:
		print( f'-------------------- an error occurred: {e} --------------------' )
	
	print( '-------------------- runAll end --------------------' )


async def run( csvuser ):
	print( f'-------------------- run start {csvuser} --------------------' )
	try:		
		fg = FeedGenerator()
		fg.id( 'https://tiktok.com/@' + csvuser )
		fg.title( '@' + csvuser + ' | TikTok' )
		fg.author( {'name':'Conor ONeill','email':'conor@conoroneill.com'} )
		fg.link( href='http://tiktok.com', rel='alternate' )
		fg.logo( ghPagesURL + 'tiktok-rss.png' )
		fg.subtitle( 'Latest TikToks from @' + csvuser )
		fg.link( href=ghPagesURL + 'rss/' + csvuser + '.xml', rel='self' )
		fg.language( 'en' )
		
		# Set the last modification time for the feed to be the most recent post, else now.
		updated=None
		
		async with AsyncTikTokAPI( navigation_retries=3, navigation_timeout=60 ) as api:
			tiktokuser = await api.user( csvuser, video_limit=maxItems )
			async for video in tiktokuser.videos:
				# print( video.create_time, video.desc )
				print( "URL = " + "https://tiktok.com/@" + csvuser + "/video/" + str( video.id ) )
				fe = fg.add_entry()
				link = "https://tiktok.com/@" + csvuser + "/video/" + str( video.id )
				fe.id( link )
				ts = video.create_time
				print( ts )
				fe.published( ts )
				fe.updated( ts )
				updated = max( ts, updated ) if updated else ts
				if video.desc:
					fe.title( video.desc[0:255] )
				else:
				  fe.title( "No Title" )
				fe.link( href=link )
				#fe.description( "<img src='" + tiktok.as_dict['video']['cover'] + "' />" )
				if video.desc:
					fe.description( video.desc )
				else:
					fe.description( "No Description" )
				#print( fg.rss_str( pretty=True ) )
		
		fg.updated( updated )
		fg.atom_file( 'rss/' + csvuser + '.xml', pretty=True ) # Write the RSS feed to a file
	except Exception as e:
		print( f"-------------------- an error occurred: {e} --------------------" )
		pass
	
	print( f'-------------------- run end {csvuser} --------------------' )



asyncio.run( runAll() )
