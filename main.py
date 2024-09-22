from flask import Flask
from Models import db,UserTabel
from Views import index,register,Help,Login,Tree_Wallet
from Urls import url
from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
db.init_app(app)

with app.app_context():
    db.create_all()
    # DB = db.session.execute(db.select(UserTabel)).scalars().all()
    # print(DB)
    # search = lambda data,n:(i for i in data if i.userName == n)
    # select = search(DB,'zaahra@in.com')
    # selected = select.send(None)
    # print("selected: ",selected)
    # print("selected: ",selected.ID)
    # print("selected: ",selected.userName)
    # try:
    #     select = db.get_or_404(UserTabel,1)
    #     select.login = 1
    #     db.session.commit()
    #     print(select.login)
    # except NotFound:
    #     select = 404
    #     print(select)
    # pass

method = ["GET","POST"]

# اینجا امور ثبت نام کاربران در وبسایت است
app.add_url_rule(url['index'],"Index-Home",index,methods=method)

# اینجا کاربران می توانند قوانین و اطلاعات کمکی به وبسایت ببینند
app.add_url_rule(url['Help'],"Help-Home",Help)

# اینجا قالب صفحه لاگین را لود می کند
app.add_url_rule(url['register'],"Index-Acc",register)

# در این صفحه لاگین انجام می گیرد
app.add_url_rule(url['Login'],'Login',Login,methods=method)

# این تابع فقط توکن ها رو اضافه می کند
app.add_url_rule(url['wallet'],'Tree_Wallet',Tree_Wallet,methods=method)

app.secret_key = '10<flask-app>irdrope107Mine5HostTree</flask-app>01'
