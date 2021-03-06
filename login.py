import pandas as pd
import json
import numpy as np

def login(username, password):

	user_file = "user.csv"
	user_db = pd.read_csv(user_file)

	if username not in list(user_db["email"]):
		return False, None

	else:
		row = user_db.loc[user_db["email"] == username]
		if not row["password"].tolist()[0] == password :
			return False, None
		else :
			#print(user_db.loc[user_db["email"] == username])
			user = {"email" : list(row['email'])[0], "password" : list(row['password'])[0], "isLeader" : list(row["isLeader"])[0], "pool" : list(row['pool'])[0], "uid" : list(row['uid'])[0], "name" : list(row['name'])[0]}
			return True, user

def signup(name, username, password):

	user_file = "user.csv"
	user_db = pd.read_csv(user_file)
	row = None
	try :
		row = {"email" : str(username), "password" : str(password), "isLeader" : 0, "pool" : 0, "uid" : int(max(list(user_db["uid"])) + 1), "name" : name}
		user_db = user_db.append(row,ignore_index=True)

		if("Unnamed: 0" in user_db.columns):
			user_db = user_db.drop(["Unnamed: 0"], axis=1)
		user_db.to_csv("user.csv")
		print(user_db, "\nDone")
	except Exception as e:
		print(e)
		return False, row

	return True, row

print(login("test", "test"))
