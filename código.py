# coding=utf-8
import json
import requests
import http.client
import urllib.parse


# Essa primeira função armazenara todas as urls que serão utilizadas para fazer as
# requisições deste iniciar o switche a deleta as regras. Ela ira retornar un dicionário com todas a urls.
def urls ():
    url = {}
    url ["url_rules"] = 'http://localhost:8080/firewall/rules/0000000000000001'
    url ["url_initial_status"] = "/firewall/module/enable/0000000000000001"
    url ["url_status_switche"] = "/firewall/module/status"
    url ["url_delete"] = "falta fazer"
    url ["url_all_rules"] = "/firewall/rules/0000000000000001"
    url ["url_acquiring_log"] =  "/firewall/log/status"
    url ["url_changing_log"] = "/firewall/log/enable/0000000000000001"

    return url

# Essa função ira passar os parâmetros que serão utilizados para criar as regras no firewall.

def parametros_firewall ():
    newConditions = {}
    newConditions ["nw_src"] = "10.0.0.1/32"
    newConditions ["nw_dst"] = "10.0.0.2/32"
    newConditions ["nw_proto"] = "ICMP"
    newConditions ["actions"] = "ALLOW"
    newConditions ["priority"] = "10"
    return newConditions

def parametros_servidor ():
    socket = {}
    socket ["ip"]= "localhost"
    socket ["port"] = 8080
    return socket

def initial_status ():
    url_initial_status = urls ()
    url = url_initial_status ["url_initial_status"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request("PUT", url)
    response = comment.getresponse()

    status = response.status
    reacao = response.reason
    dados = response.read ()
    comment.close()

def rules ():
    url_rules = urls ()
    newConditions = parametros_firewall ()
    conditionsSetURL = url_rules ["url_rules"]
    params = json.dumps(newConditions).encode('utf8')
    req = urllib.request.Request(conditionsSetURL, data=params,
                                headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)

    saida = response.read().decode('utf8')

def status_switche ():
    url_status_switche = urls ()
    url = url_status_switche ["url_status_switche"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request ("GET", url)
    response = comment.getresponse()

    status = response.status
    reacao = response.reason
    dados = response.read ()

def delete ():
    body = {"rule_id": "5"}
    conn = httplib.HTTPConnection('localhost', 8080)
    conn.request("DELETE", '/firewall/rules/0000000000000001', data = body)
    resp = conn.getresponse()
    content = resp.read()

def acquiring_all_rules ():
    all_rules = urls ()
    url = all_rules ["url_all_rules"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request ("GET", url)
    response = comment.getresponse()

    dados = response.read ()
    status = response.status
    reacao = response.reason

def acquiring_log_output ():
    acquiring_log = urls()
    url = acquiring_log ["url_acquiring_log"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request ("GET", url)
    response = comment.getresponse()

    status = response.status
    reacao = response.reason
    dados = response.read ()

def changing_log_output ():
    changing_log = urls ()
    url = changing_log ["url_changing_log"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request("PUT", url)
    response = comment.getresponse()

    status = response.status
    reacao = response.reason
    dados = response.read ()
    comment.close()