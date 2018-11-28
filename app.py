# ######################################
# Update this list with your own episodes
# ######################################
# List of dictionaries of episodes with number, title and mp3 url, in the following format:
# {'num': '1', 'title': 'Speech to Text - Eric Bolo, Batvoice', 'mp3': 'https://www.buzzsprout.com/159584/691682-speech-to-text-eric-bolo-batvoice-voice-tech-podcast-ep-001.mp3'},
# escape any ' with \
# MUST remove any ampersands (&) or feed will break
episodes = [

{'num': '1', 'title':' One More Thing. Broadcast on Thursday, September 13, 2018. This week, Brett hosts John Nosta, Faisal Khan and David Gerbino, covering the Apples big September event, talking the new iPhone XS and Apple Watch Series 4s new heart-tracking features. Then, Greg Palmer of Finovate introduces us to two startups, Bucket and Crypterium, demoing at Finovate Fall 2018 in NYC Sept 24-26.. ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking091318.mp3'},
{'num': '2', 'title':' My Voice is my Password. Broadcast on Thursday, September 20, 2018. . ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking092018.mp3'},
{'num': '3', 'title':' The Guardians of our Money. Broadcast on Thursday, September 27, 2018. Brett King hosts NetGuardians, a Swiss based AI fraud prevention start-up discusses how machine learning has radically changed the way we manage fraud within organizations like banks. We speak to COO and co-founder RAFFAEL MAIO and CTO JÉRÔME KEHRLI about how NetGuardians was established and when they pivoted to becoming an AI company.. ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking092718.mp3'},
{'num': '4', 'title':' Finovate Fall 2018. Broadcast on Thursday, October 04, 2018. Brett King, JP Nicols, Jim Marous and moderator Greg Palmer talk the future of fintech and financial services at our recent Breaking Banks Power Hour Chat event, recording a live podcast onstage at Finovate Fall 2018 in New York City.. ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking100418.mp3'},
{'num': '5', 'title':' Funding Fintechs Future: Workhorses vs. Unicorns. Broadcast on Thursday, October 11, 2018. How is the future of fintech being funded? Hosts JP Nicols and Jason Henrichs talk about corporate venture capital and strategic investing, then Jason continues the conversation with VCs Kat Utecht and Matt Harris as we explore the differences between investing in “workhorses” vs. “unicorns.". ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking101118.mp3'},
{'num': '6', 'title':' The Glue That Binds Us. Broadcast on Thursday, October 18, 2018. . ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking101818.mp3'},
{'num': '7', 'title':' FinTech: Worlds Apart. Broadcast on Thursday, October 25, 2018. This week, we tour Sydney, Australia and Las Vegas, USA with the Fintech Mafia and the extended FinTech family. Out at SIBOS, Brett King hosts Joe Lubin, co-Founder of Ethereum and Consensys, Gottfried Leibbrandt, CEO of SWIFT, and Uday Goyal from APIS. Then, from Money 20/20 in Las Vegas, JP Nicols hosts Tom Poole, Capital Ones VP of Payments, Identity and Capital One Labs.. ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking102518.mp3'},
{'num': '8', 'title':' Deep Learning Goes Public. Broadcast on Thursday, November 01, 2018. Brett King hosts Jim Marous, talking his new Digital Banking Report, and Spiros Margaris joins as we reveal the identity of the man behind @DeepLearn007, a mysterious Twitter account known in the fintech community. Then, JP Nicols hosts Ken Dodelin as they discuss Capital Ones conversational AI program.. ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking110118.mp3'},
{'num': '9', 'title':' Closing the Gap Between Idea and Results. Broadcast on Thursday, November 08, 2018. Lauren Amarante, co-founder of World Entrepreneurship Day, said: “You could have a million ideas, but theyre all worthless if you dont get them done.” Todays show features banks that are getting it done and Jill Castilla, CEO of Citizens Bank if Edmond and John Epperson, Global Regulatory & Compliance Solution Leader at Crowe on why compliance shouldnt be your blocker. Co-hosts Jason Henrichs and JP Nicols will also share details on the public launch of the Alloy Labs Alliance, a consortium based approach to innovation. In the second half, Andrew Nash head of Digital Identity for Capital One joins us as a part of our #InvestedInTech series, #sponsored by Capital One.. ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking110818.mp3'},
{'num': '10', 'title':' Blurring the Line Between Incumbents and Insurgents. Broadcast on Thursday, November 15, 2018. This week we look at the increasingly blurry line between incumbents and insurgents in fintech and financial services. Eric Byunn and Tom Davis, partners at Centana Growth Partners join Jason Henrichs. Then Naveed Anwar, head Strategic Partnerships/Integrations & Developer Community for Capital One joins us as a part of our #InvestedInTech series, #sponsored by Capital One.. ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking111518.mp3'},
{'num': '11', 'title':' RegTech goes AI. Broadcast on Tuesday, November 27, 2018. In this weeks show, we talk to one on the leading players in RegTech AI development Pegasystems, a US listed Fintech. Reetu Khosla joins us to talk the scope of AI development and we check in with PWCs Henri Arslanian to get a feel for where the big AI changes are coming for global regulators. When laws become code, how do regulators operate? Join us on BreakingBanks to find out.. ', 'mp3': 'https://cdn.voiceamerica.com/business/011292/bking112718.mp3'}


]

# ######################################
# No need to touch the code below this point
# ######################################

from flask import Flask
from flask_restful import Api, Resource
import os

# deployed here:
# https://dashboard.heroku.com/apps/voicetechpodcast-episodes/deploy/github

# links:
# https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
# https://medium.freecodecamp.org/how-to-host-lightweight-apps-for-free-a29773e5f39e

# create objects
app = Flask(__name__)
api = Api(app)


# build the episode string
episode_string = ''.join([''.join(['Episode ', ep['num'], ' - ', ep['title'], '. ']) for ep in reversed(episodes)])
episode_string = episode_string[:-2]  # remove final comma
episode_feed = {'topics': episode_string, 'min_episode': 1, 'max_episode': len(episodes)}

# class to process request for a specific episode
class Episode(Resource):
    def get(self, num):
        try:
            ep = episodes[int(num) - 1]
            return ep, 200
        # no element at this index
        except IndexError:
            return 'Episode not found', 404

# url endpoint for information on a specific episode
# For a specified episode e.g. episode 1:
    # debug: http://127.0.0.1:5000/ep/1
    # live: https://voicetechpodcast-episodes.herokuapp.com/ep/1
# For the latest episode:
    # debug: http://127.0.0.1:5000/ep/0
    # live: https://voicetechpodcast-episodes.herokuapp.com/ep/0
# sample output: {"num": "12", "title": "Fast Scalable Voice IoT Apps - Syed Ahmed, PubNub", "mp3": "https://www.buzzsprout.com/159584/829047-fast-scalable-voice-iot-apps-syed-ahmed-pubnub-voice-tech-podcast-ep-012.mp3"}
api.add_resource(Episode, '/ep/<string:num>')

# class to process request for list of all episodes
class Feed(Resource):
    def get(self):
        return episode_feed, 200

# url endpoint for list of all episodes
    # debug: hit http://127.0.0.1:5000/feed
    # live: hit https://voicetechpodcast-episodes.herokuapp.com/feed
# sample output: {"topics": "Episode 12 - Fast Scalable Voice IoT Apps - Syed Ahmed, PubNub. Episode 11 - Audio Branding and Sound Design - Sebastian Hanfland, Hanfland and Friends. Episode 10 - Podcasts of the Future - Bryan Colligan, AlphaVoice. Episode 9 - Hum a Fingerprint, Extract a Melody - Dogac Basaran, CNRS. Episode 8 - Signal Processing Basics for Audio - Dogac Basaran, CNRS. Episode 7 - Perception of Smiles in the Voice - Pablo Arias, IRCAM. Episode 6 - Deaf Person Calling - Benjamin Etienne, Rogervoice. Episode 5 - The Art of Sound in Motion - Greg Beller, IRCAM. Episode 4 - Building Knight Rider's KITT - Charles Cadbury, Champers Advisory. Episode 3 - Vivatech 2018 Voice Startup Summary. Episode 2 - Voice AI for eCommerce - John Fitzpatrick, Voysis. Episode 1 - Speech to Text - Eric Bolo, Batvoice", "min_episode": 1, "max_episode": 12}
api.add_resource(Feed, '/feed')

# uncomment this line and comment the main method to run debug locally
# app.run(debug=False)

# main method that runs on program start, and listens for incoming requests for episodes
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
    app.run(host='0.0.0.0', port=port)  #Start listening
