import socket

HOST = '10.100.102.194'  # כתובת ה-IP של השרת (localhost במקרה הזה)
PORT = 1234  # אותו מספר פורט שבו השרת מאזין

# יצירת חיבור לשרת
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # שליחת הודעה לשרת
        message = input("Enter message to send: ")
        if message.lower() == 'exit':  # יציאה מהלולאה אם הקלט הוא 'exit'
            break

        # המרת ההודעה למערך בתים
        message_data = bytearray(message, 'utf-8')

        # שליחת ההודעה לשרת
        s.sendall(message_data)

        # קבלת התגובה מהשרת
        reply_data = s.recv(1024)  # קבלת עד 1024 בתים
        reply_text = reply_data.decode("utf-8").rstrip('\x00')  # המרת הבתים להודעה
        print("Received reply from server: " + reply_text)

print("Connection closed.")
