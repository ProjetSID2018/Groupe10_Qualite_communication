
from functions.g5_import_json import import_daily_jsons
import datetime
import os


def test_import_json():
    path_source = os.getcwd()
    if (int(datetime.datetime.now().month) < 10):
        date = str(datetime.datetime.now().year) + '-0' + \
            str(datetime.datetime.now().month) + '-'\
            + str(datetime.datetime.now().day)
    else:
        date = str(datetime.datetime.now().year) + '-' + \
            str(datetime.datetime.now().month) + '-'\
            + str(datetime.datetime.now().day)

    json1 = {
        "title": "De la <<liberte d'offenser>> a celle d'importuner?",
        "newspaper": "Liberation",
        "author": ["Denis  Ramond  Docteur en Science politique"],
        "date_publi": "2018-01-12",
        "content": "<<Pas de nouvel impot>>,\
            promet Bruno Le Maire Emmaus Solidarite : supports ",
        "theme": " "}
    json2 = {
        "title": "Du silence a l'operation de com :\
            ce qu'il faut retenir de la sortie mediatique du boss de Lactalis",
        "newspaper": "Liberation",
        "author": ["Philippe Brochen "],
        "date_publi": "2018-01-14",
        "content": "Catherine Deneuve : <<Rien a donner ports ",
        "theme": " "}

    os.mkdir(path_source + "/" + date)
    os.mkdir(path_source + "/" + date + "/" + "liberation")

    f = open(path_source + "/" + date + "/" + "liberation" +
             "/" + "art_libe_1_2018-01-12_robot.json", "w")
    f.write(str(json1))
    f.close()

    f = open(path_source + "/" + date + "/" + "liberation" +
             "/" + "art_libe_1_2018-01-14_robot.json", "w")
    f.write(str(json2))
    f.close()

    res = import_daily_jsons(path_source)
    assert res["art_libe_1_2018-01-12_robot.json"]["title"]\
        == json1["title"]
    assert res["art_libe_1_2018-01-12_robot.json"]["newspaper"]\
        == json1["newspaper"]
    assert res["art_libe_1_2018-01-12_robot.json"]["author"]\
        == json1["author"]
    assert res["art_libe_1_2018-01-12_robot.json"]["date_publi"]\
        == json1["date_publi"]
    assert res["art_libe_1_2018-01-12_robot.json"]["content"]\
        == json1["content"]
    assert res["art_libe_1_2018-01-12_robot.json"]["theme"]\
        == json1["theme"]

    assert res["art_libe_1_2018-01-14_robot.json"]["title"]\
        == json1["title"]
    assert res["art_libe_1_2018-01-14_robot.json"]["newspaper"]\
        == json1["newspaper"]
    assert res["art_libe_1_2018-01-14_robot.json"]["author"]\
        == json1["author"]
    assert res["art_libe_1_2018-01-14_robot.json"]["date_publi"]\
        == json1["date_publi"]
    assert res["art_libe_1_2018-01-14_robot.json"]["content"]\
        == json1["content"]
    assert res["art_libe_1_2018-01-14_robot.json"]["theme"]\
        == json1["theme"]
