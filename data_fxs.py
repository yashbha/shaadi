import sqlite3
import json
import datetime as dt

conn = sqlite3.connect('shaadi.db',check_same_thread=False)
c = conn.cursor()

def create_table():

	c.execute('CREATE TABLE IF NOT EXISTS Guests(Name PRIMARY KEY NOT NULL ,category,Family_No,Expected_Arrival,Expected_Departure,Gifts,Confirmed,contact_no)')
	conn.commit()
	c.execute('CREATE TABLE IF NOT EXISTS Functions(Name PRIMARY KEY NOT NULL,Date,Main_ppl,Requirements,return_gifts,comments,events)')
	conn.commit()

def update_guest_gift_all(a,b):
	c.execute("UPDATE Guests SET Gifts=?  WHERE Name=?  ", (str(a), b))
	conn.commit()
def add_data(n,k):
	if n==0:
		c.execute('INSERT INTO Guests(Name,category,Family_No,Expected_Arrival,Expected_Departure,Gifts,Confirmed,contact_no) VALUES (?,?,?,?,?,?,?,?)',(k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7]))
		conn.commit()
	else:
		c.execute('INSERT INTO Functions(Name ,Date,Main_ppl,Requirements,return_gifts,comments,events) VALUES (?,?,?,?,?,?,?)',(k[0],k[1],k[2],k[3],k[4],k[5],k[6]))
		conn.commit()

def update_events(a,b,flag):
	if flag==0:
		ll = "('" + b + "')"
		c.execute("SELECT events FROM Functions WHERE Name=?", (ll,))
		gif = c.fetchall()

		aa = eval(gif[0][0])
		print(aa.keys())
		try:
			aa['Event'].append(a[0])
			aa['Date'].append(a[1].isoformat())
			aa['Time'].append(a[2].isoformat())
		except:
			aa={"Event":[a[0]],"Date":[a[1].isoformat()],"Time":[a[2].isoformat()]}
		aa = json.dumps(aa)

	else:
		aa=a['data'].to_json()
	c.execute("UPDATE Functions SET events=?  WHERE Name=?  ", (aa, b))
	conn.commit()

def view_all_data(a):
	gh="SELECT * FROM "+a
	c.execute(gh)
	data = c.fetchall()
	return data

def view_all_task_names():
	c.execute('SELECT DISTINCT task FROM taskstable')
	data = c.fetchall()
	return data

def get_task(task):
	c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
	data = c.fetchall()
	return data

def get_task_by_status(task_status):
	c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
	data = c.fetchall()


def edit_task_data(task,val,table):
	query="UPDATE {} SET {}={}".format(table,task,val)
	c.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(task):
	c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
	conn.commit()

def update_guest_gift(a,b):

	c.execute("SELECT Gifts FROM Guests WHERE Name=?",(b,))
	gif=c.fetchall()
	print(gif)
	aa = eval(gif[0][0])
	aa.append(a)
	c.execute("UPDATE Guests SET Gifts=?  WHERE Name=?  ", (str(aa), b))
	conn.commit()

def update_main_ppl(a,b,flag):

	if flag==0:
		ll="('"+b+"')"
		c.execute('SELECT Main_ppl FROM Functions WHERE Name={}'.format(ll))
		data = c.fetchall()
		aa=eval(data[0][0])
		aa['name'].append(a[0])
		aa['Contact'].append(a[1])
		aa = json.dumps(aa)
	else:
		aa=a['data'].to_json()
	c.execute("UPDATE Functions SET Main_ppl=?  WHERE Name=?  ",(aa,b))
	conn.commit()

def update_ret_gift(a,b,flag):
	if flag==0:
		ll = "('" + b + "')"
		c.execute('SELECT return_gifts FROM Functions WHERE Name={}'.format(ll))
		data = c.fetchall()

		try:
			aa = eval(data[0][3])
		except:
			aa = eval(data[0][0])

		counter = 0
		try:
			aa['name'].append(a[0])
			aa['contact'].append(a[1])
			aa['return gift'].append(a[2])

		except:
			aa = {'name': [a[0]], 'contact': [a[1]], 'return gift': [a[2]]}
		aa = json.dumps(aa)
	else:
		aa=a['data'].to_json()

	c.execute("UPDATE Functions SET return_gifts=?  WHERE Name=?  ", (aa, b))
	conn.commit()

def update_comments(a,b):
	c.execute("UPDATE Functions SET comments=?  WHERE Name=?  ", (a, b))
	conn.commit()

def update_req(a,b,flag):
	if flag==0:
		ll="('"+b+"')"
		c.execute('SELECT Requirements FROM Functions WHERE Name={}'.format(ll))
		data = c.fetchall()
		print(data[0][0])
		try:
			aa=eval(data[0][3])
		except:
			aa=eval(data[0][0])


		counter=0
		try:
			aa['Item'].append(a[0])
			aa['Quantity'].append(a[1])
			aa['Units'].append(a[2])
			aa['Agg'].append(a[3])
		except:
			aa={'Item':[a[0]],'Quantity':[a[1]],'Units':[a[2]],'Agg':[0]}
		aa = json.dumps(aa)
	else:
		aa=a['data'].to_json()

	c.execute("UPDATE Functions SET Requirements=?  WHERE Name=?  ",(aa,b))
	conn.commit()
