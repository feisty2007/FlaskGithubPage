#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'黄道'

__author__ = 'Ming gong'

import os
import shutil

from flask import Flask, render_template, jsonify, request

from FileUtil import FileUtil
from TimeUtil import TimeUtil
from UUIDUtil import UUIDUtil

app = Flask(__name__)
github_io_dir = "C:/git/xxxx.github.io/"
images_dir = github_io_dir + "assets/images/"
time_util = TimeUtil()
file_util = FileUtil()
uuid_uitl = UUIDUtil()
today_str = time_util.today()


@app.route("/")
def index():
    return edit()


@app.route('/index')
def r_index():
    return edit()


@app.route("/edit")
def edit():
    types = ['心情', 'blog', '工具', '软件']
    return render_template('edit.html',
                           category=types)


def save_md_file(title, md_file_name, category, md_text):
    file_title = "-".join(md_file_name.split(" "))
    all_md_file_name = today_str + "-" + file_title + ".md"
    post_file_name = github_io_dir + "/_posts/" + all_md_file_name

    lines = []
    lines.append("---")
    lines.append("layout:   post")
    lines.append("title:    \"%s\"" % (title))
    lines.append("crawlertitle: \"%s\"" % (title))
    lines.append("description:  \"%s\"" % (title))
    lines.append("summary:  \"%s\"" % (title))
    lines.append("date: %s" % (time_util.now().toStr()))
    lines.append("categories:   %s" % (category))
    lines.append("tags: [%s]" % (category))
    lines.append("author:   \"feisty2007\"")
    lines.append("---")
    lines.append("")
    lines.append(md_text)

    with open(post_file_name, 'w', encoding='utf-8') as f:
        f.writelines([line + "\n" for line in lines])


@app.route("/admin/saveContent", methods=["POST"])
def save():
    title = request.form["title"]
    md_file_name = request.form["des"]
    category = request.form["category"]
    md_text = request.form["md_text"]

    md_text = str(md_text).replace("/static/uploads", "/assets/images")
    title = str(title).replace(".", "-")

    print(md_text)

    save_md_file(title, md_file_name, category, md_text)

    recognize_info = {'code': 0,
                      'msg': "保存成功"}
    return jsonify(recognize_info), 201


def genuuid(filename):
    file_ext = file_util.getExt(filename)
    uuid = uuid_uitl.gen()

    return today_str + "-" + uuid + "." + file_ext


@app.route("/uploadfile", methods=["POST"])
def uploadFile():
    f = request.files["editormd-image-file"]
    # print(file_name)

    basepath = os.path.dirname(__file__)  # 当前文件所在路径

    uuid_file_name = genuuid(f.filename)
    upload_path = os.path.join(basepath, 'static/uploads/', uuid_file_name)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    assert_path = images_dir + uuid_file_name
    f.save(upload_path)
    shutil.copy(upload_path, assert_path)

    resp = {
        "success": 1,
        "message": "上传成功",
        "url": "/static/uploads/%s" % (uuid_file_name)
    }

    return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True)
