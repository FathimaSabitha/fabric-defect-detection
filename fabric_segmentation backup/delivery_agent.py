from flask import *
from database import*



delivery_agent=Blueprint("delivery_agent",__name__)

@delivery_agent.route('/delivery_agent')
def delivery_agent_home():
    return render_template('delivery_agent_home.html')
 
@delivery_agent.route('/delivery_agent_profile')
def delivery_agent_profile():
    data2={}
    qc="SELECT * FROM `delivery_agent` where dg_id='%s'"%(session['delivery_agent'])
    res5=select(qc)
    data2['view_profile']=res5
 
    return render_template('delivery_agent_profile.html',data=data2)


@delivery_agent.route('/delivery_agent_assigned_order')
def delivery_agent_assigned_order():
    data2={}
    # qc="SELECT * FROM assign_order INNER JOIN order_master USING(om_id) INNER JOIN retailer USING(retailer_id) where dg_id='%s'"%(session['delivery_agent'])
    qc="SELECT * FROM assign_order INNER JOIN order_master USING(om_id) INNER JOIN wholesaler USING(wholesaler_id) WHERE dg_id='%s'"%(session['delivery_agent'])
    res5=select(qc)
    data2['view_assigned_order']=res5


    if 'action' in request.args:
      action=request.args['action']
      id=request.args['id']
      omid=request.args['omid']

    else:
      action=None   


    if action=='update':
      qry="update assign_order set status='deliverd'  where assign_id='%s'"%(id)
      update(qry)

      qry1="update order_master set status='deliverd'  where om_id='%s'"%(omid)
      res=update(qry1)
    
      return """<script>alert('Updated');window.location='delivery_agent_assigned_order'</script>"""

 
 
    return render_template('delivery_agent_assigned_order.html',data=data2)


@delivery_agent.route('/delivery_agent_view_details')
def delivery_agent_view_details():
    id=request.args['id']
    data2={}
    qc="SELECT * FROM order_details INNER JOIN product USING(product_id) where om_id='%s'"%(id)
    res5=select(qc)
    data2['view_details']=res5



    return render_template('delivery_agent_view_details.html',data=data2)
