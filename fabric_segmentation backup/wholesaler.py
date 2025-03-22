import uuid
from flask import *
from database import*



wholesalers=Blueprint("wholesaler",__name__)

@wholesalers.route('/wholesaler')
def wholesaler_home():
    return render_template('wholesaler_home.html')
 

 

@wholesalers.route("/wholesaler_manage_products",methods=['post','get'])
def wholesaler_manage_products():
   data={}
   qd="SELECT * FROM product where wholesaler_id='%s'"%(session['wholesaler'])
   res9=select(qd)
   data['view']=res9
   print(data,"///////")

   if 'Submit' in request.form:
      product_name=request.form['product_name']
      description=request.form['description']
      category=request.form['category']
      fabric_type=request.form['fabric_type']
      color=request.form['color']
      price_per_unit=request.form['price_per_unit']
      stock_quantity=request.form['stock_quantity']
      minimum_order=request.form['minimum_order']
      image=request.files['image']

      path = 'static/prods/'+str(uuid.uuid4())+image.filename
      image.save(path)

      qryy="insert into product values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(product_name,description,category,fabric_type,color,price_per_unit,stock_quantity,minimum_order,path,session['wholesaler'])
      a=insert(qryy)  
      return """<script>alert('Added');window.location='/wholesaler/wholesaler_manage_products'</script>"""   
      
   
   if 'action' in request.args:
      action=request.args['action']
      id=request.args['id']
   else:
      action=None   


   if action=='delete':
      qry="delete from product where product_id='%s'"%(id)
      delete(qry) 
      return """<script>alert('deleted');window.location='/wholesaler/wholesaler_manage_products'</script>"""   
        


   if action=='update':
      qry="select * from product where product_id='%s'"%(id)
      res=select(qry)
      if res:
         data['up']=res

   if 'update' in request.form:
      product_name=request.form['product_name']
      description=request.form['description']
      category=request.form['category']
      fabric_type=request.form['fabric_type']
      color=request.form['color']
      price_per_unit=request.form['price_per_unit']
      stock_quantity=request.form['stock_quantity']
      minimum_order=request.form['minimum_order']
      image=request.files['image']

      path = 'static/prods/'+str(uuid.uuid4())+image.filename
      image.save(path)

      qryy="update product set product_name='%s',description='%s',category='%s',fabric_type='%s',color='%s',price_per_unit='%s',stock_quantity='%s',minimum_order='%s',image='%s' WHERE product_id='%s'"%(product_name,description,category,fabric_type,color,price_per_unit,stock_quantity,minimum_order,path,id)
      update(qryy)
      return """<script>alert('updated');window.location='/wholesaler/wholesaler_manage_products'</script>"""   
      
   return render_template("wholesaler_manage_products.html",data=data) 





@wholesalers.route("/wholesaler_manage_deliveryagent",methods=['post','get'])
def wholesaler_manage_deliveryagent():
   data={}
   qd="SELECT * FROM delivery_agent"
   res9=select(qd)
   data['view']=res9

   if 'Submit' in request.form:
      fname=request.form['fname']
      lname=request.form['lname']
      place=request.form['place']
      phone=request.form['phone']
      address=request.form['address']
      username=request.form['username']
      password=request.form['password']

      qry1="select * from login where username='%s'"%(username)
      res=select(qry1)
  
      if res:
          return """<script>alert('Username already exist');</script>"""
      else:
         qry5="insert into login values(null,'%s','%s','delivery')"%(username,password)
         a=insert(qry5)  
         qryy="insert into delivery_agent values(null,'%s','%s','%s','%s','%s','%s')"%(a,fname,lname,place,phone,address)
         b=insert(qryy) 
         
   
   if 'action' in request.args:
      action=request.args['action']
      id=request.args['id']
   else:
      action=None   


   if action=='delete':
      qry="delete from delivery_agent where dg_id='%s'"%(id)
      delete(qry)

      return """<script>alert('deleted');window.location='/wholesaler/wholesaler_manage_deliveryagent'</script>"""   

   if action=='update':
      qry="select * from delivery_agent where dg_id='%s'"%(id)
      res=select(qry)
      if res:
         data['up']=res

   if 'update' in request.form:
      fname=request.form['fname']
      lname=request.form['lname']
      place=request.form['place']
      phone=request.form['phone']
      address=request.form['address']
      qryy="update delivery_agent set fname='%s',lname='%s',place='%s',phone='%s',address='%s' WHERE dg_id='%s'"%(fname,lname,place,phone,address,id)
      update(qryy)
      """<script>alert('updated');window.location='/wholesaler/wholesaler_manage_deliveryagent'</script>"""   
   return render_template("wholesaler_manage_deliveryagent.html",data=data)



@wholesalers.route("/wholesaler_view_order")
def wholesaler_view_order():
   data5={}
   qo="SELECT * FROM `order_details` INNER JOIN order_master USING(om_id) WHERE wholesaler_id='%s'"%(session['wholesaler'])
   res8=select(qo)
   data5['view_orders']=res8
   return render_template("wholesaler_view_order.html",data=data5)


@wholesalers.route("/wholesaler_assign_order",methods=['post','get'])
def wholesaler_assign_order():

   if 'action' in request.args:
      omid=request.args['id']
      session['omid']=omid
   data={}
   qry="select * from delivery_agent"
   res=select(qry)
   if res:
      data['view']=res

   if 'submit' in request.form:
      print("hello")
      deliveryagent=request.form['deliveryagent']
      qry1="insert into assign_order values(null,'%s','%s','pending')"%(deliveryagent,session['omid'])
      insert(qry1)
   return render_template("wholesaler_assign_order.html",data=data)


@wholesalers.route("/wholesaler_view_defect")
def wholesaler_view_defect():
   data6={}
   qd="SELECT *,defect_report.description as def_des, defect_report.image as def_image FROM `defect_report` INNER JOIN product USING(product_id)WHERE wholesaler_id='%s'"%(session['wholesaler'])
   res9=select(qd)
   data6['view_orders']=res9
   return render_template("wholesaler_view_defect.html",data=data6)




@wholesalers.route("/wholesaler_view_feedback")
def wholesaler_view_feedback():
   data4={}
   qfs="SELECT * FROM `feedback` where wholesaler_id='%s'"%(session['wholesaler'])
   res7=select(qfs)
   data4['view_feeds']=res7
   return render_template("wholesaler_view_feedback.html",data=data4)






#wholesalers delivery


@wholesalers.route("/wholesaler_complaint",methods=['post','get'])
def wholesaler_complaint():
   
   if 'Submit' in request.form:
      description=request.form['description']
      qryy="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['wholesaler'],description)
      a=insert(qryy) 
   data={}
   qry="select * from complaint where sender_id='%s'"%(session['wholesaler']) 
   res=select(qry)
   if res:
      data['view']=res
   return render_template("wholesaler_complaint.html",data=data)



