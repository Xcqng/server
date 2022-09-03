import socket


def mainRun():
	#ระบุเป้าหมาย
	ip = "127.0.0.1"
	#port หมายเลข
	port = 5000
	#สร้างobject
	server = socket.socket()
	#ผูกobject
	server.bind((ip,port))
	#เชื่อมต่อกี่คน
	server.listen(1)
	
	print("รอการเชื่อมต่อจาก client")
	#ยืนยันเครื่องclientเชื่อมต่อ
	client,ddr = server.accept()
	
	print("ip from "+str(ddr))
	
	while True:
		#ถอดรหัสจาก client
		data=client.recv(1024).decode('utf-8')
		
		
		if not data:
			break
		
		print("client from data : "+data)
		data=str(data.upper())
		#เข้ารหัสที่จะส่ง
		print("รอการตอบกลับ")
		ta = input("message : ")
		client.send(ta.encode('utf-8'))
		
	
		
		
mainRun()
	