from flask import *
from database import *


public=Blueprint('public',__name__)


@public.route("/")
def home():
    return render_template("home.html")


@public.route("/login",methods=['POST','GET'])
def login():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        
        qry1="select * from login where username='%s' and password='%s'"%(username,password)
        res1=select(qry1)
        # print(res1,"___________________________")
        if res1:
           session['log']=res1[0]['login_id']
        
        if res1[0]['usertype']=='admin':
          return redirect(url_for('admin.adminhome'))
        
        if res1[0]['usertype']=='wholesaler':
          qry="select * from wholesaler where login_id='%s'"%(session['log'])
          res=select(qry)
          if res:
              session['wholesaler']=res[0]['wholesaler_id']
              return redirect(url_for('wholesaler.wholesaler_home'))
        
        if res1[0]['usertype']=='retailer':
          qry="select * from retailer where login_id='%s'"%(session['log'])
          res=select(qry)
          if res:
              session['retailer']=res[0]['retailer_id']
              return redirect(url_for('retailer.retailer_home'))
        
        if res1[0]['usertype']=='delivery':
          qry="select * from delivery_agent where login_id='%s'"%(session['log'])
          res=select(qry)
          if res:
              session['delivery_agent']=res[0]['dg_id']
              return redirect(url_for('delivery_agent.delivery_agent_home'))
        
    return render_template("login.html")



@public.route('/wholesaler',methods=['GET','POST'])
def wholesaler():
    if 'Submit' in request.form:
      username=request.form['username']
      password=request.form['password']
      company_name=request.form['company_name']
      owner_name=request.form['owner_name']
      email=request.form['email']
      phone=request.form['phone']
      address=request.form['address']
      pin=request.form['pin']
      upload_business_license=request.form['upload_business_license']
      upload_tax_license=request.form['upload_tax_license']

      qry1="select * from login where username='%s'"%(username)
      res=select(qry1)
  
      if res:
          return """<script>alert('Username already exist');window.location='/wholesaler'</script>"""
      else:

        qry5="insert into login values(null,'%s','%s','pending')"%(username,password)
        a=insert(qry5)  
        qry2="insert into wholesaler values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a,company_name,owner_name,email,phone,address,pin,upload_business_license,upload_tax_license)
        insert(qry2)
        return """<script>alert('Success');window.location='/login'</script>"""
      
    return render_template("wholesaler.html")


@public.route('/retailer',methods=['GET','POST'])
def retailer():
    if 'Submit' in request.form:
      username=request.form['username']
      password=request.form['password']
      company_name=request.form['company_name']
      owner_name=request.form['owner_name']
      email=request.form['email']
      phone=request.form['phone']
      address=request.form['address']
      pin=request.form['pin']
      upload_business_license=request.form['upload_business_license']
      upload_tax_license=request.form['upload_tax_license']

      qry1="select * from login where username='%s'"%(username)
      res=select(qry1)

      qry5="insert into login values(null,'%s','%s','retailer')"%(username,password)
      a=insert(qry5)  
        
      qry3="insert into retailer values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a,company_name,owner_name,email,phone,address,pin,upload_business_license,upload_tax_license)
      insert(qry3)  
      

    return render_template("retailer.html")

# ********************************************************************************************
# @public.route("/product",methods=['post','get'])
# def product():
#     if 'submit' in request.form:
#       product_id=request.form['product_id']
#       product_name=request.form['product_name']
#       description=request.form['description']
#       category=request.form['category']
#       fabric_type=request.form['fabric_type']
#       color=request.form['color']
#       price_per_unit=request.form['price_per_unit']
#       stock_quantity=request.form['stock_quantity']
#       minimum_order=request.form['minimum_order']
#       image=request.form['image']
        
#       qry6="insert into product values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(product_id,product_name,description,category,fabric_type,color,price_per_unit,stock_quantity,minimum_order,image)
#       insert(qry6)


#     return render_template("product.html")

# @public.route("/order_master",methods=['post','get'])
# def order_master():
#     if 'submit' in request.form:
#       om_id=request.form['om_id']
#       retailer_id=request.form['retailer_id']
#       total=request.form['total']
#       status=request.form['status']
#       date=request.form['date']
      
#       qry6="insert into order_master values(null,'%s','%s','%s','%s')"%(om_id,retailer_id,total,status,date)
#       insert(qry6)


#     return render_template("order_master.html")

# @public.route("/order_details",methods=['post','get'])
# def order_details():
#     if 'submit' in request.form:
#       od_id=request.form['od_id']
#       om_id=request.form['om_id']
#       product_id=request.form['product_id']
#       stock=request.form['stock']
#       amount=request.form['amount']
      
#       qry7="insert into order_details values(null,'%s','%s','%s','%s')"%(od_id,om_id,product_id,stock,amount)
#       insert(qry7)


#     return render_template("order_details.html")

# @public.route("/defect_report",methods=['post','get'])
# def defect_report():
#     if 'submit' in request.form:
#       report_id=request.form['report_id']
#       product_id=request.form['product_id']
#       description=request.form['description']
#       image=request.form['image']
#       date=request.form['date']
      
#       qry8="insert into defect_report values(null,'%s','%s','%s','%s')"%(report_id,product_id,description,image,date)
#       insert(qry8)


#     return render_template("defect_report.html")