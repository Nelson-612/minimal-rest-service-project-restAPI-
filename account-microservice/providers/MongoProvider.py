import json
import os
import pymongo
from bson import ObjectId
from bson.json_util import dumps
from steam_scraper.SteamScraper import SteamScraper  

class JSONEncoder(json.JSONEncoder):
	"""
	Extend JSON Encoder to support mongoDB id encoding
	"""
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)


class MongoProvider(object):

	def __init__(self):
		"""
		Create the connection with mongoDB
		"""
		self.myclient = pymongo.MongoClient(f"mongodb://{os.environ.get('MONGO_URL', 'localhost')}:{os.environ.get('MONGO_PORT', 27017)}/")
		self.mydb = self.myclient["steam"]
		self.mycol = self.mydb["discountgame"]
		self.scrapper = SteamScraper()

	def get_and_push_discounted_games(self):
		games = self.scrapper.get_discounted_games()
		if games and isinstance(games, list):
			for game in games:
				print(game)
				self.mycol.insert_one(game)
		else:
			print("No discounted games found or invalid data format.")



	def read_game_by_title(self, gameTitle):
		
		print(f"Database: {self.mydb.name}")
		print(f"Collection:  {self.mycol.name}")
		collections = self.mydb.list_collection_names()
		print(f"Available collections: {collections}")
		count = self.mycol.count_documents({})
		print(f"Number of documents in collection: {count}")

		if self.mycol.count_documents({'title': gameTitle}, limit=1) != 0:
			user_query = {"title": gameTitle}

			user = self.mycol.find_one(user_query)
			
			user = JSONEncoder().encode(user)
			return json.loads(user), 200
		else:
			return {"error": "user not found"}, 400

	def read_all_games(self):
		logs = self.mycol.find()
		logs_list = list(logs)
		print(logs_list)

		collections = self.mydb.list_collection_names()
		print(f"Available collections: {collections}")
		count = self.mycol.count_documents({})
		print(f"Number of documents in collection: {count}")
		
		
		json_string = dumps(logs_list)
		logs_dict = json.loads(json_string)
		return {"logs": logs_dict}, 200
	



