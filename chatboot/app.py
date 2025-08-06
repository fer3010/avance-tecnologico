from flask import Flask, request, jsonify, render_template

app= Flask (__name__)

def chatbot_response(user_message):
    user_message = user_message.lower().strip()
    if "hola" in user_message or "saludos" in user_message:
        return "¡hola! ¿en que puedo ayudarte?"
    elif "horarios" in user_message:
        return "Los horarios de atención son de lunes a viernes de 9:00 a 18:00."
    elif "ubicacion" in user_message:
        return "Estamos ubicados en la calle Falsa 123, Ciudad."
    elif "contacto" in user_message:
        return "Puedes contactarnos al correo"
    elif "precios" in user_message:
        return "Los precios varían según el producto. Por favor, especifica el producto que te interesa."    
    elif "gracias" in user_message or "gracias" in user_message:
        return "¡De nada! Si tienes más preguntas, no dudes en preguntar."
    else :
        return "Lo siento, no entendí tu pregunta. ¿Podrías reformularla?"
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/chat', methods=['POST'])
    def get_response():
        user_message = request.json.get('message')
        response=chatbot_response(user_message)
        return jsonify({'response': response})
    
    if __name__ == '__main__':
        app.run(debug=True)

        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = chatbot_response(user_message)
        return jsonify({'response': response})