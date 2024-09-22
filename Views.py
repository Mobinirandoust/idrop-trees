from flask import request,redirect,render_template
from Models import UserTabel,db
from werkzeug.security import generate_password_hash as pHash,check_password_hash as cHash
from markupsafe import escape as es
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

def DB(n:str) -> object:
    DB = db.session.execute(db.select(UserTabel)).scalars().all()
    search = lambda data,n:(i for i in data if i.userName == n)
    select = search(DB,n)
    selected = select.send(None)
    return selected

def index():
        if request.method == "GET":
            return redirect('/register')
        elif request.method == "POST":
            value = {
                 1:es(request.form['username']),
                 2:pHash(es(request.form['password']),salt_length=1),
                 3:es(request.form['Friend']),
                 }
            if '@' not in value[1]:
                 return "<script>history.back();alert('ایمیل نامشخص است')</script>"

            try:
                n_user = UserTabel(
                    userName = value[1],
                    passWord = value[2],
                    )
                db.session.add(n_user)
                db.session.commit()
                select = db.get_or_404(UserTabel,int(value[3]))
                select.friends += 1
                db.session.commit()
                return "<script>history.back();alert('ثبت نام شما با موفقیت انجام شد')</script>"
            except ValueError:
                return "<script>history.back();alert('آیدی دوست تان را با اعداد انگلیسی وارد کنید')</script>"
            except IntegrityError:
                return "<script>history.back();alert('ایمیل وارد شده قبلا ثبت نام کرده است لطفا ایمیل جدید وارد کنید')</script>"
            except NotFound:
                 return "<script>history.back();alert('آیدی که وارد کردین شناسایی نشد')</script>"

def register():
    return render_template('account/index.html')

def Help():
     return render_template('Home/help.html')

def Login():
    try:
        if request.method == "POST":
            user = request.form['username']
            selected = DB(user)
            password = request.form['password']
            if cHash(selected.passWord, password):
                return render_template('Home/irdrop.html',User=selected)
            elif cHash(selected.passWord, password) is False:
                return "<script>history.back();alert('رمز نادرست است')</script>"
        else:
            return "<script>history.back();alert('ورود ناموفق')</script>"
    except StopIteration:
        return "<script>history.back();alert('ورود ناموفق')</script>"
    
def Tree_Wallet():
    if request.method == "POST":
        UserID = request.form['UserID']
        Coin = request.form['Coin']
        User = db.get_or_404(UserTabel,int(UserID))
        User.Token += int(Coin)
        db.session.commit()
        return "<script>history.back();alert('توکن های استخراج شده شما به کیف پول اضافه شد برای مشاهده روی بارگذاری مجدد کلیک کنید')</script>"
    return redirect("/")