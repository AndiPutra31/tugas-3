import threading
import socket
import time
import sys

def get_file(nama):
	myfile = open(nama)
	return myfile.read()


class MemprosesClient(threading.Thread):
	def __init__(self,client_socket,client_address,nama):
		self.client_socket = client_socket
		self.client_address = client_address
		self.nama = nama
		threading.Thread.__init__(self)
	
	def run(self):
		message = ''
		while True:
        		data = self.client_socket.recv(21)
            		if data:
				message = message + data #collect seluruh data yang diterima
				print "data : ",data
				#print "\n\n\n"
				#print "message : ",message 
				if (message == "GET /gambar1 HTTP/1.1" ) :
					print "haha\n\n"
					self.client_socket.send(get_file('gambar1.jpg'))
					break
				elif (message == "GET /gambar2 HTTP/1.1" ) :
					print "haha\n\n"
					self.client_socket.send(get_file('gambar2.jpg'))
					break
				elif (message == "GET /gambar3 HTTP/1.1" ) :
					print "haha\n\n"
					self.client_socket.send(get_file('gambar3.jpg'))
					break
				elif (message == "GET /gambar4 HTTP/1.1" ) :
					print "haha\n\n"
					self.client_socket.send(get_file('gambar4.jpg'))
					break
				elif (message == "GET /gambar5 HTTP/1.1" ) :
					print "haha\n\n"
					self.client_socket.send(get_file('gambar5.jpg'))
					break
				elif (message.endswith("\r\n\r\n")):
					self.client_socket.send(get_file('gambar.jpg'))
					break
            		else:
               			break
		self.client_socket.close()
		


class Server(threading.Thread):
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = ('localhost',9999)
		self.my_socket.bind(self.server_address)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.listen(1)
		nomor=0
		while (True):
			self.client_socket, self.client_address = self.my_socket.accept()
    			nomor=nomor+1
			#---- menghandle message cari client (Memproses client)
			my_client = MemprosesClient(self.client_socket, self.client_address, 'PROSES NOMOR '+str(nomor))
			my_client.start()
			#----


serverku = Server()
serverku.start()


