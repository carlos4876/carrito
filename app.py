from flask import Flask, render_template,request,session,redirect,url_for

app = Flask(__name__)
#nesecario cunado se usa session
app.secret_key = 'unaclavesecreta'#definimos una clave secreta puede ser cualquir texto

@app.route("/")
def carrito():
    #verificando si un valor(lista) esta o no esta en la session
    if 'lista' not in session:
       #inisisalisamos la lista
       session['lista'] = []
    return render_template('index.html', lista = session['lista'])
 
@app.route("/procesa", methods=['GET','POST'])    
def procesa():
    producto = request.form.get("producto")
    if 'lista' in session and producto:
        #producto adicionado en la lista
        session['lista'].append(producto)
        #aseguramos que la session a sido modificado
        session.modified = True
    return redirect(url_for("carrito"))
@app.route("/vaciar",methods=["GET"])
def vaciar():
    #elimina de session el objeto de la lista
    session.pop("lista",None)
    return redirect(url_for("carrito"))
    
if __name__ == "__main__":
    app.run(debug=True)