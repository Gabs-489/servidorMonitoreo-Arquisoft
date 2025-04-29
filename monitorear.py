from flask import Flask, jsonify, request
from twilio.rest import Client

app = Flask(__name__)

@app.route('/errorUsuarios', methods=['GET'])
def mandar_mensaje_advertencia():
    print("Se entro a la funcion!")
    account_sid = 'AC55994d626e2eb71e524c938bf8c27b07'  
    auth_token = '78154485797bd9dc9a5ee57f5ab97914' 

    
    from_number = '+14634030212' 
    to_number = '+573214044360' 
    print("Credenciales listas")
    client = Client(account_sid, auth_token)
    print("Cliente creado")
    message = client.messages.create(
        body='¡Alerta! Falló el manejador de usuarios. Por favor, verifique el sistema.',
        from_=from_number,
        to=to_number
    )
    print("mensaje enviado")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
