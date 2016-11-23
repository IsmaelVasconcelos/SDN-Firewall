import json
import requests
import http.client
import urllib.parse

def identi_sw (id_s):
    complemento = "000000000000000"
    id_sw = id_s
    id_sw = 16 - len(id)
    lendo = complemento[0:id_sw]
    id_sw = (lendo + id)
    return id_sw

def urls ():
    id_sw = identi_sw (id_s)
    url = {}
    url ["url_rules"] = ('http://localhost:8080/firewall/rules/%s' %id_sw)
    url ["url_initial_status"] = "/firewall/module/enable/0000000000000001"
    url ["url_status_switche"] = "/firewall/module/status"
    url ["url_delete"] =
    url ["url_all_rules"] = "/firewall/rules/0000000000000001"
    url ["url_acquiring_log"] =  "/firewall/log/status"
    url ["url_changing_log"] = "/firewall/log/enable/0000000000000001"
    return url


def parametros_firewall (nw_src, nw_dst, actions, priority):
    identi_sw (id_s)
    newConditions = {}
    newConditions ["id"] = id_sw
    newConditions ["nw_src"] = nw_src
    newConditions ["nw_dst"] = nw_dst
    newConditions ["nw_proto"] = nw_proto
    newConditions ["actions"] = actions
    newConditions ["priority"] = priority
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