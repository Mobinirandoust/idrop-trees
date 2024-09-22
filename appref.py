from flask import render_template_string,render_template

class views:
    def index():
        lists = ["Ali","Mobin","Amoo","Karlo","kian",]
        return render_template('home.html', li = lists)