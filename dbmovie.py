from pymongo import MongoClient
import certifi

ca = certifi.where();

client = MongoClient('mongodb+srv://sammymin:sammy0404@cluster0.gvkfzz2.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

db.user1.update_one({'title':'가버나움'},{'$set':{'star': '0'}})
