from flask import *
from database import*
import os
import uuid



retailer=Blueprint("retailer",__name__)

@retailer.route('/retailer_home')
def retailer_home():
    return render_template('retailer_home.html')

# @retailer.route("/retailer_view_wholesaler",methods=['post','get'])
# def retailer_view_wholesaler():
#     data={}
#     qo="SELECT * FROM `product`"
#     res8=select(qo)
#     data['retailer_view_wholesaler  ']=res8
#     if res8:
#         data['view']=res8
#         return render_template("retailer_view_wholesaler.html",data=data)
    


@retailer.route('/retailer_view_wholesaler')
def retailer_view_wholesaler():
    data={}
    x="select * from wholesaler"
    y=select(x)
    if y:
        data['view']=y 
    return render_template("retailer_view_wholesaler.html",data=data)


@retailer.route('/retailer_view_products')
def retailer_view_products():
    data={}
    id= request.args['id']
    x="select * from product where wholesaler_id='%s'"%(id)
    y=select(x)
    if y:
        data['view']=y 
    return render_template("retailer_view_products.html",data=data)     



# @retailer.route('/make_order',methods=['post','get'])
# def make_order():
#     id=request.args['id']
#     am=request.args['am']

#     if 'submit' in request.form:
#         stock=request.form['stock']

#         tot=int(am)*int(stock)

#         x="insert into order_master values(null,'%s','%s',curdate(),'pending')"%(session['retailer'],tot)
#         om=insert(x)

#         y="insert into order_details values(null,'%s','%s','%s','%s')"%(om,id,stock,tot)
#         insert(y)
#         return """<script>alert('Added to cart');window.location='retailer'</script>"""
#     return render_template('makeorder.html')


@retailer.route('/addtocart',methods=['POST','GET'])
def addtocart():
    minorder=''
    if 'action' in request.args:
        id= request.args['id']
        wh_id= request.args['wh_id']
        amount = request.args['amount']
        minorder=int(request.args['minorder'])

        if 'submit' in request.form:
            quantity = int(request.form['quantity'])
            if quantity>minorder:
                qry3="select * from product where product_id='%s'"%(id)
                res3=select(qry3)
                if res3:
                    stock_quantity=int(res3[0]['stock_quantity'])
                    if stock_quantity>quantity:

                        qry="select * from order_master where retailer_id = '%s' and status='pending'"%(session['retailer'])
                        res=select(qry)

                        total = int(quantity)*int(amount)

                        if res :

                            oid=res[0]['om_id']
                            t=res[0]['total']
                            btotal = int(total)+int(t)


                            a="update order_master set total='%s',date=curdate() where om_id='%s'"%(btotal, oid)
                            update(a)

                            b ="insert into order_details values(null,'%s','%s','%s','%s')"%(oid,id,quantity,total)
                            insert(b)

                            # qry3="select * from order_master inner join order_details using(om_id) inner join product using(product_id) where product_id='%s'"%(id)
                            # res3=select(qry3)

                            # if res3:
                            #     stock_quantity=int(res3[0]['stock_quantity'])
                            rem_quantity=int(stock_quantity)-int(quantity)
                            
                            qry4="update product set stock_quantity='%s' where product_id='%s'"%(rem_quantity,id)
                            update(qry4)

                        else:
                            qry1 ="insert into order_master values(null,'%s','%s',curdate(),'pending','%s')"%(session['retailer'],total,wh_id)
                            res1=insert(qry1)

                            qry2 ="insert into order_details values(null,'%s','%s','%s','%s')"%(res1,id,quantity,amount)
                            insert(qry2)

                            rem_quantity=int(stock_quantity)-int(quantity)
                            
                            qry4="update product set stock_quantity='%s' where product_id='%s'"%(rem_quantity,id)
                            update(qry4)

                        return ("<script>alert('Order Placed Successfully');window.location='retailer_view_wholesaler'</script>")
                    
                    return ("<script>alert('Product is out of stock!!..');window.location='retailer_view_wholesaler'</script>")
                    
            else:
                return ("<script>alert('Item quantity is less than minimum order');window.history.back();</script>")

    return render_template("addtocart.html",minorder=minorder)




# @retailer.route("/retailer_view_cart",methods=['post','get'])
# def retailer_view_cart():
#     data={}
#     qo="SELECT * FROM order_master INNER JOIN order_details USING(om_id) WHERE retailer_id='%s'"%(session['retailer'])
#     res8=select(qo)
#     data['retailer_view_cart']=res8
#     if res8:
#         data['view']=res8
#     return render_template("retailer_view_cart.html",data=data)
    

@retailer.route('/retailer_view_order')
def retailer_view_order():
    data={}
    # x="SELECT * from order_master INNER JOIN order_details USING (om_id) INNER JOIN product USING (product_id) inner join assign_order using(om_id) WHERE order_master.status = 'pending' and retailer_id = '%s'" % (session['retailer'])
    x = """
            SELECT order_master.*, order_details.*, product.*
            FROM order_master
            INNER JOIN order_details USING (om_id)
            INNER JOIN product USING (product_id)
            WHERE order_master.status = 'pending' AND retailer_id = '%s'
            """ % (session['retailer'])

    y=select(x)
    print(y,'////////////////////////////////////////////')
    if y:
        data['view']=y 
    else:
        return '<script>alert("No items ordered");window.location="retailer_home"</script>'

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None    

    if action=='viewdg':
        qry="select * from assign_order inner join delivery_agent using(dg_id) where om_id='%s'"%(id)  
        res=select(qry)
        if res:
            data['viewdg']=res
        else:
            return '<script>alert("Your Order is not assigned");window.location="retailer_view_order"</script>'

        
    return render_template("retailer_view_order.html",data=data)


# @retailer.route("/retailer_view_order",methods=['post','get'])
# def retailer_view_order():
#     data={}
#     qo="SELECT * FROM order_master inner join order_details USING(om_id) WHERE retailer_id='%s'"%(session['retailer'])
#     res9=select(qo)
#     data['retailer_view_order']=res9
#     return render_template("retailer_view_order.html",data=data)


@retailer.route("/retailer_purchase",methods=['post','get'])
def retailer_purchase():
    data={}
    id=request.args['id']
    qo="SELECT * FROM order_details inner join product using(product_id) WHERE om_id='%s'"%(id)
    res9=select(qo)
    data['retailer_purchase']=res9
    return render_template("retailer_purchase.html",data=data)
    





@retailer.route("/retailer_give_feedback",methods=['post','get'])
def retailer_give_feedback():
   data1={}
   qry="select * from wholesaler"
   res=select(qry)
   if res:
       data1['whole']=res


   data2={}
   qry2="select * from feedback where retailer_id='%s'"%(session['retailer'])  
   res2=select(qry2)
   if res2:
      data2['view']=res2


   if 'Submit' in request.form:
      feedback=request.form['feedback']
      id=request.form['w_id']
      qfs="insert into `feedback` values(null,'%s','%s','%s',curdate())"%(id,session['retailer'],feedback)
      insert(qfs)
      

   
   return render_template("retailer_give_feedback.html",data2=data2,data1=data1)


@retailer.route("/retailer_complaint",methods=['post','get'])
def retailer_complaint():
    data1={}
    qry="select * from wholesaler"
    res=select(qry)
    if res:
       data1['whole']=res

    data={}
    qry="select * from complaint where sender_id='%s'"%(session['log']) 
    res=select(qry)
    data['view']=res
    
    if 'Submit' in request.form:
        description=request.form['description']
        qryy="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['log'],description)
        a=insert(qryy) 

        
    return render_template("retailer_complaint.html",data=data,data1=data1)




from new_predict import *
@retailer.route('/retailer_detect_defect', methods=['POST','GET'])
def retailer_detect_defect():
    data={}
    # x="select * from defect_report inner join product using(product_id) where retailer_id='%s'"%(session['retailer'])
    x = """
        SELECT defect_report.*, product.*, defect_report.description AS defect_description, product.description AS product_description, defect_report.image AS defect_image
        FROM defect_report
        INNER JOIN product USING (product_id)
        WHERE retailer_id = '%s'
        """ % (session['retailer'])
    y=select(x)
    if y:
        data['view']=y

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None    

    if 'submit' in request.form:
        file=request.files['file']
        path='static/'+str(uuid.uuid4())+file.filename
        file.save(path)
        print(path,"ppppppppppppppppppppppp")
        class_name, confidence = predict_image_class(model, path)

        # Return the result
        # return f"Predicted class: {class_name} with confidence: {confidence:.2f}"
    
        # print(res,"ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
        
        qry = "insert into defect_report values(null,'%s','%s','%s','%s',curdate())"%(id,session['retailer'],class_name,path)
        insert(qry)

        return '<script>alert("Report Send Successfully");window.location="retailer_detect_defect"</script>'

    return render_template("retailer_detect_defect.html",data=data)



import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import os
import uuid
from flask import Flask, request

# Constants
IMG_HEIGHT, IMG_WIDTH = 224, 224
CLASS_NAMES = ['hole', 'pilling', 'snags', 'stain', 'unknown']  # Update this based on your classes

# Load the trained model from the specified path
def load_trained_model(model_path):
    model = load_model(model_path)
    print("Model loaded successfully.")
    return model

# Preprocess the image to match model input requirements
def prepare_image(image_path):
    image = load_img(image_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    image = img_to_array(image)  # Convert to numpy array
    image = image / 255.0  # Normalize to [0,1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Predict the class of a given image using the loaded model
def predict_image_class(model, image_path):
    image = prepare_image(image_path)
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions, axis=1)
    confidence = np.max(predictions)
    class_name = CLASS_NAMES[predicted_class[0]]
    print(f"Predicted class: {class_name} with confidence: {confidence:.2f}")
    return class_name, confidence

# Load the model
model_path = "new_fabric_damage_detection_vgg16_10_epochs.h5"
model = load_trained_model(model_path)
