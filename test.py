from pymongo import MongoClient

client = MongoClient("mongodb+srv://usermonty0007:1234@cluster1.xt0egrp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
print(client.list_database_names())  # It should list existing databases like 'admin', 'local', etc.
