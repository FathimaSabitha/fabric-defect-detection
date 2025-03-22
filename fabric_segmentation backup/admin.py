from flask import *
from database import*

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route("/admin_view_wholesaler")
def admin_view_wholesaler():
   data={}
   qq="SELECT * FROM `wholesaler` INNER JOIN `login` USING(`login_id`)"
   res=select(qq)
   data['view_who']=res

   if "action" in request.args:
      action=request.args['action']
      idd=request.args['ids']
   else:
      action =None
   if action == "accept":
      qq="UPDATE `login` SET `usertype`='wholesaler' WHERE `login_id`='%s'"%(idd)
      update(qq)
      return redirect(url_for("admin.admin_view_wholesaler"))
   elif action == "reject":
      qr="UPDATE `login`SET `usertype`='reject' WHERE `login_id`='%s'"%(idd)
      update(qr)
      return redirect(url_for("admin.admin_view_wholesaler"))
   else:
      action =None
      
   return render_template("admin_view_wholesaler.html",data=data)


@admin.route("/admin_view_retailers")
def admin_view_retailers():
   data1={}
   qr="SELECT * FROM `retailer`"
   res4=select(qr)
   data1['view_retail']=res4
   return render_template("admin_view_retailers.html",data1=data1)


@admin.route("/admin_view_complaints")
def admin_view_complaints():
   data2={}
   qc="SELECT * FROM `complaint` where reply='pending'"
   res5=select(qc)
   data2['view_complaint']=res5
   return render_template("admin_view_complaints.html",data=data2)


@admin.route("/admin_com_reply",methods=['get','post'])
def admin_com_reply():
   id=request.args['id']

   if 'submit' in request.form:
      reply=request.form['reply']
      qry6="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
      res2=update(qry6)
      return redirect(url_for("admin.admin_view_complaints"))
   return render_template("reply.html")

@admin.route("/admin_view_feedbacks")
def admin_view_feedbacks():
   data3={}
   qf="SELECT * FROM `feedback`"
   res6=select(qf)
   data3['view_feed']=res6
   return render_template("admin_view_feedbacks.html",data=data3)



# @admin.route('/complaint',methods=['GET','POST'])
# def complaint():
#    if 'submit' in request.form:
#        complaint_id=request.form['complaint_id']
#        sender_id=request.form['sender_id']
#        description=request.form['description']
#        reply=request.form['reply']
#        date=request.form['date']
      
#        qry4="insert into complaint values(null,'%s','%s','%s','%s')"%(complaint_id,sender_id,description,reply,date)
#        insert(qry4)
   
#    return render_template("complaint.html")
    
   

@admin.route("/feedback",methods=['post','get'])
def feedback():
    if 'submit' in request.form:
      feedback_id=request.form['feedback_id']
      wholesaler_id=request.form['wholesaler_id']
      retailer_id=request.form['retailer_id']
      feedback=request.form['feedback']
      date=request.form['date']
      
      qry5="insert into feedback values(null,'%s','%s','%s','%s')"%(feedback_id,wholesaler_id,retailer_id,feedback,date)
      insert(qry5)
    return render_template("feedback.html")


    
