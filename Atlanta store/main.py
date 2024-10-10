from flask import Flask, render_template, request, redirect, url_for
from user_agents import parse

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index_page():
    user_agent = request.headers.get('User-Agent')
    parsed_user_agent = parse(user_agent)
    
    if parsed_user_agent.is_mobile or parsed_user_agent.is_tablet:
        return render_template("Forbidden-Device.html")
    
    return render_template("index.html")




if __name__ == "__main__":
    app.run()