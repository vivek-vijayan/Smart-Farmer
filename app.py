from twilio.rest import Client
from flask import Flask,render_template,request,redirect, url_for
app=Flask(__name__)
app.secret_key = 'glkno348y0958howajrgnpoqiwu34hp5i8hpq3o4iugp9qrngo'
import urllib2
import json
import smtplib

Farmer_id_p=[]
Product_id=[]
Product_name=[]
Quantity=[]
Price=[]

# wheat = 31 ----- Rice = 21

entry_id=[]

Farmer_id=[]
Farmer_name=[]
Address=[]
Pincode=[]
phno=[]

username=[]
password=[]
pincode_u=[]
email_u=[]

total_product_list=['Wheat','Rice']
purchased=[]

uname=""
uemail=""

control=0
session_username=""
session_pincode=""
power_switch=0

'''
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login("vijayanv31@gmail.com", "kjkszpjlavenjqhesoaymokllaaa")

msg = "Demo Mail from SMART FARMER DEVICE on product order confirmation"
server.sendmail("vijayanv31@gmail.com", "veenetha.1997@gmail.com", msg)
server.quit()
'''

@app.route("/")
@app.route("/index")
def main():
	CHANNEL_ID1="431236"
	READ_API_KEY1="1UGLU0A7XXIKI1PC"
	conn1=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID1,READ_API_KEY1))
	response1=conn1.read()
	status1=int(conn1.getcode())
	data1=json.loads(response1)
	total1=int(data1['channel']['last_entry_id'])

	for x in range(0,total1):
		Farmer_id.append(int(data1['feeds'][x]['field1']))
		Farmer_name.append(data1['feeds'][x]['field2'])
		Address.append(data1['feeds'][x]['field3'])
		Pincode.append(data1['feeds'][x]['field4'])
		phno.append(data1['feeds'][x]['field5'])
	CHANNEL_ID="431254"
	READ_API_KEY="CHYUAS6YQ96COFUO"
	conn=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID,READ_API_KEY))
	response=conn.read()
	status=int(conn.getcode())
	data=json.loads(response)
	total=int(data['channel']['last_entry_id'])

	for x in range(0,total):
		Farmer_id_p.append(data['feeds'][x]['field1'])
		Product_id.append(int(data['feeds'][x]['field2']))
		Product_name.append(data['feeds'][x]['field3'])
		Quantity.append(data['feeds'][x]['field4'])
		Price.append(data['feeds'][x]['field5'])
		entry_id.append(data['feeds'][x]['entry_id'])
	print "entry_id:-->"
	print entry_id

	control=0

	data={
	'username':session_username,
	'u_pin':session_pincode,
	'farmer_id_p': Farmer_id_p,
	'farmer_id': Farmer_id,
	'farmer_name': Farmer_name,
	'address': Address,
	'pincode': Pincode,
	'phno': phno,
	'product_id': Product_id,
	'product_name': Product_name,
	'quantity': Quantity,
	'price': Price,
	'total': total,
	'control':0
	}
	return render_template("buddy.html",**data)

@app.route("/filter",methods = ['POST', 'GET'])
def main_filter():
	global purchased
	if (request.method=="POST"):
		filters=str(request.form['filter']).lower()
	control=1
	CHANNEL_ID1="431236"
	READ_API_KEY1="1UGLU0A7XXIKI1PC"
	conn1=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID1,READ_API_KEY1))
	response1=conn1.read()
	status1=int(conn1.getcode())
	data1=json.loads(response1)
	total1=int(data1['channel']['last_entry_id'])
	unit_pid=[]
	for x in range(0,total1):
		Farmer_id.append(int(data1['feeds'][x]['field1']))
		Farmer_name.append(data1['feeds'][x]['field2'])
		Address.append(data1['feeds'][x]['field3'])
		Pincode.append(data1['feeds'][x]['field4'])
		phno.append(data1['feeds'][x]['field5'])
	CHANNEL_ID="431254"
	READ_API_KEY="CHYUAS6YQ96COFUO"
	conn=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID,READ_API_KEY))
	response=conn.read()
	status=int(conn.getcode())
	data=json.loads(response)
	total=int(data['channel']['last_entry_id'])

	for x in range(0,total):
		Farmer_id_p.append(data['feeds'][x]['field1'])
		Product_id.append(int(data['feeds'][x]['field2']))
		Product_name.append(data['feeds'][x]['field3'])
		Quantity.append(data['feeds'][x]['field4'])
		Price.append(data['feeds'][x]['field5'])
		entry_id.append(data['feeds'][x]['entry_id'])
	print purchased
	print Product_id
	data={
	'entry_id':entry_id,
	'purchased':purchased,
	'unit_pid':unit_pid,
	'username':session_username,
	'u_pin':session_pincode,
	'farmer_id_p': Farmer_id_p,
	'farmer_id': Farmer_id,
	'farmer_name': Farmer_name,
	'address': Address,
	'pincode': Pincode,
	'phno': phno,
	'product_id': Product_id,
	'product_name': Product_name,
	'quantity': Quantity,
	'price': Price,
	'total': total,
	'filters':filters,
	'control':1

	}
	return render_template("buddy.html",**data)

'''@app.route("/login")
def lgn():
	d={}
	return render_template("login.html",**d)'''


@app.route("/login",methods = ['POST','GET'])
def login():
	global power_switch
	if(power_switch==0):
		global uemail
		global uname
		s_name=""
		s_password=""
		if(request.method=="POST"):
			s_name=str(request.form['u_name'])
			s_password=str(request.form['u_password'])
			uname=s_name
			c=urllib2.urlopen("https://api.thingspeak.com/channels/445483/feeds.json?api_key=6KDB826WI7B1RN0N")
			response=c.read()
			status=int(c.getcode())
			data=json.loads(response)
			total=int(data['channel']['last_entry_id'])

			for x in range(0,total):
				username.append(str(data['feeds'][x]['field2']))
				password.append(str(data['feeds'][x]['field6']))
				pincode_u.append(str(data['feeds'][x]['field1']))
				email_u.append(str(data['feeds'][x]['field5']))
			try:
				'''print username
				print password
				print pincode_u
				print email_u'''
				u_id=int(username.index(s_name))
				u_pwd=int(password.index(s_password))
				e_email=str(email_u[u_id])
				print u_id
				uname=username[u_id]
				uemail=e_email
				print uemail
				if(u_id==u_pwd):
					PIN=pincode_u[u_id]
					session_username=u_id
					session_pincode=PIN
					power_switch=1
					return redirect(url_for('main'))
				else:
					a={'error':"something gone wrng"}
					return render_template("login.html",**a)
			except:
				a={'error':'Login Error.. Retry'}
				return render_template("login.html",**a)

		else:
			a={}
			power_switch=0
			return render_template("login.html",**a)
	else:
		return redirect(url_for('main'))

@app.route("/reg",methods = ['POST','GET'])
def regnow():
	if(request.method=="POST"):
		name=request.form['name']
		email=request.form['email']
		password=request.form['password']
		address=request.form['address']
		phno=request.form['phno']
		pincode=request.form['pincode']
		base_URL="http://api.thingspeak.com/update?api_key=%s"%("VQYWXWXK2AQDIAW9")
		conn=urllib2.urlopen(base_URL+"&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s"%(pincode,name,address,phno,email,password))
		conn.close()
	a={}
	return render_template("register.html",**a)
import random

@app.route("/getaccess/<fid>/<pid>",methods=['POST','GET'])
def getaccess(fid,pid):
	global uname
	global purchased
	print uname
	if(request.method=="POST"):
		order_id=random.randint(50000,9000000)
		farmer_id=request.form['fid']
		farmer_name=request.form['fname']
		farmer_address=request.form['faddr']
		farmer_phno=request.form['fphno']
		farmer_pin=request.form['fpin']

		product_id=request.form['pid']
		product_name=request.form['pname']
		product_quantity=request.form['pquan']
		product_price=request.form['pprice']

		user_name=request.form['uname']
		user_mail=request.form['uemail']
		eid=request.form['eid']

		total_price=int(product_quantity)*int(product_price)/1000
#)
		gmail_user = 'smartfarmersale@gmail.com'
		gmail_password = 'Smartfarmer157'
		client = Client("ACb0e39fcd74d7bd6eb7152d3315b93d15", "1634c65896b8671956dc81b67d8a8148")
		msg_bdy="Order ID: %d , Customer name: %s purchased %sg of %s for Rs:%s"%(order_id,uname,product_quantity,product_name,total_price)
		client.messages.create(to="+"+str(farmer_phno),from_="(256) 401-9985",body=msg_bdy)
		try:
		    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		    server.ehlo()
		    server.login(gmail_user, gmail_password)
		    message = """From: SMART Farmer sale <noreply@smartfs.com>
To: Customer <customer@smartfs.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Product Confirmation mail

			This is an e-mail message regarding product purcharse
			<br>
			<b>Confirmation mail for purchasing product in smart farmer sale.</b>
			<h1 style='color:red;'>Hi %s,Thank you for purchasing.</h1>
			<br>
			<h3>Order ID: %d</h3>
			<br>
			<hr>
			<table border="1">
			<tr>
				<th> Product ID</th>
				<th> Product name </th>
				<th> Quantity </th>
				<th> Price </th>
			</tr>
			<tr>
				<th> %s	</th>
				<th> %s	</th>
				<th> %s	</th>
				<th>Rs. %s	</th>
			</tr>
			</table>
			<br>
			<h4> Farmer details</h4>
			<table  border="1">
				<tr>
					<th> Farmer ID</th>
					<th> Farmer name </th>
					<th> Farmer Address </th>
					<th> Farmer Phno </th>
				</tr>
				<tr>
					<td> %s	</td>
					<td> %s	</td>
					<td> %s	</td>
					<td><h4> %s	 </h4></td>
				</tr>
			</table>
			<br>
			<font color="green" > Please take a print out to purchase the product: </font>
			<br>
			<font color="red"> <h3> Bill Validate only for a week from the today. </h3></font>

			"""%(uname,order_id,product_id,product_name,product_quantity,total_price,farmer_id,farmer_name,farmer_address,farmer_phno)
		    print "mail id :"+uemail
		    purchased.append(int(eid))
		    server.sendmail("vijayanv31@gmail.com",uemail,message)
			#print "Success"

		except:
		    print 'Something went wrong...'

		id=Farmer_id.index(int(fid))
		fid=Farmer_id[id]
		fname=Farmer_name[id]
		faddr=Address[id]
		fpin=Pincode[id]
		fphno=phno[id]
		p_id=Product_id.index(int(pid))
		pid=Product_id[p_id]
		pname=Product_name[p_id]
		pquan=Quantity[p_id]
		pprice=Price[p_id]
		eid=entry_id[p_id]

		a={
		'eid':eid,
		'fid':fid,
		'fname':fname,
		'faddr':faddr,
		'fpin':fpin,
		'fphno':fphno,
		'pid':pid,
		'pname':pname,
		'pquan':pquan,
		'pprice':pprice,
		'uname':uname,
		'uemail':uemail
		}
		print username
		print password
		print email_u
		return render_template("farmer_confirmation.html",**a)

	else:
		id=Farmer_id.index(int(fid))
		fid=Farmer_id[id]
		fname=Farmer_name[id]
		faddr=Address[id]
		fpin=Pincode[id]
		fphno=phno[id]
		p_id=Product_id.index(int(pid))
		pid=Product_id[p_id]
		pname=Product_name[p_id]
		pquan=Quantity[p_id]
		pprice=Price[p_id]
		eid=entry_id[p_id]
		print "eid -->"
		print eid
		a={
		'eid':eid,
		'fid':fid,
		'fname':fname,
		'faddr':faddr,
		'fpin':fpin,
		'fphno':fphno,
		'pid':pid,
		'pname':pname,
		'pquan':pquan,
		'pprice':pprice
		}
		return render_template("farmer_confirmation.html",**a)

@app.route("/logout")
def forms():
	global power_switch
	power_switch=0
	return redirect(url_for('login'))

@app.route("/buddy",methods=['POST'])
def reg():
	if request.method=='POST':
		product=request.form['hmm']
		price=request.form['k']
		c_data={
		'p1':product,
		'p2':price
		}
		return render_template("index.html",**c_data)

@app.route("/upload/<a1>/<a2>/<a3>")
def upload(a1,a2,a3):
	import urllib2
	import json
	CHANNEL_ID="402974"
	WRITE_API_KEY="1YHFQW0FQ2J8TR66"
	base_URL="http://api.thingspeak.com/update?api_key=%s"%(WRITE_API_KEY)
	p_name=a1
	p_quan=a2
	p_price=a3
	conn=urllib2.urlopen(base_URL+"&field1=%s&field2=%s&field3=%s"%(p_name,p_quan,p_price))
	conn.close()
	return "uploaded successfully"

@app.route("/get/<newname>")
def getnew(newname):
	myname=newname
	data_update={
	"change_name": myname
	}
	return render_template("update.html",**data_update)


if __name__=="__main__":
	app.run(host='127.0.0.1',port=8070,debug=True)
