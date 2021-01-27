import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9001

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket oluşturuldu")

    s.bind((HOST, PORT)) 
    print("socket {} nolu porta bağlandı".format(PORT))

    s.listen(5)      
    print("socket dinleniyor")
except socket.error as msg:
    print("Hata:",msg)

while True: 

   # Client ile bağlantı kurulursa
   c, addr = s.accept()      
   print('Gelen bağlantı:', addr)

   # Bağlanan client tarafına hoşgeldin mesajı gönderelim.  
   mesaj = 'Bağlantı için teşekkürler'
   c.send(mesaj.encode('utf-8')) 

   # Bağlantıyı sonlandıralım 
   c.close()