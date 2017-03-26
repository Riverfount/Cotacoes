#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
import json
import time


def cotar():

    moeda = dict()
    try:
        req = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
        moeda = json.loads(req.text)
        for key in moeda["valores"]:
            moeda["valores"][key]["ultima_consulta"] = time.strftime("%Hh.%Mmin. de %d/%b/%Y",
                                                       time.localtime(moeda["valores"][key]["ultima_consulta"]))

            moeda["valores"][key]["valor"] = "%.2f" % moeda["valores"][key]["valor"]

            partes = str.split(moeda["valores"][key]["fonte"], "-")
            moeda["valores"][key]["fonte"] = partes[0] + " - " + '<a href="' + partes[1] + '">' + partes[1] + "</a>"

        return moeda
    except:
        return moeda

