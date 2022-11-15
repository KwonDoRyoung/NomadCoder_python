# -*-coding: utf-8 -*-
# from extractors.wwr import extract_wwr_jobs
# from extractors.indeed import extract_indeed_jobs
# from file import save_to_file
#
# keyword = input("What do you want to search for?")
#
# wwr = extract_wwr_jobs(keyword)
# indeed = extract_indeed_jobs(keyword)
# jobs = wwr + indeed
#
# save_to_file(keyword, jobs)

from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html", name="nico")


@app.route("/search")
def search():
    global db
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword in db:
        jobs = db[f"{keyword}"]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[f"{keyword}"] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    global db
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("127.0.0.1")
