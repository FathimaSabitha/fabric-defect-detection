from flask import *
from public import public
from admin import admin
from wholesaler import wholesalers
from retailer import retailer
from delivery_agent import delivery_agent
app=Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(wholesalers,url_prefix="/wholesaler")
app.register_blueprint(retailer,url_prefix="/retailer")
app.register_blueprint(delivery_agent,url_prefix="/delivery_agent")
app.secret_key='abcdfgg'


    
app.run(debug=True,port=5001)