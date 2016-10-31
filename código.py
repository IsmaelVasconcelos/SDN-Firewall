# coding=utf-8
import json
import requests
import http.client
import urllib.parse


# Essa primeira função armazenara todas as urls que serão utilizadas para fazer as
# requisições deste iniciar o switche a deleta as regras. Ela ira retornar un dicionário com todas as urls.
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
# ela retornara um dicionário e será chamada pelas demais funções. ex: rules(), delete().

def parametros_firewall ():
    newConditions = {}
    newConditions ["nw_src"] = "10.0.0.1/32"
    newConditions ["nw_dst"] = "10.0.0.2/32"
    newConditions ["nw_proto"] = "ICMP"
    newConditions ["actions"] = "ALLOW"
    newConditions ["priority"] = "10"
    return newConditions

# Essa função ira passar os parâmetros para comunicação com a aplicação rest_firewalldo ryu
# será passado o ip do servidor e a porta a qual a aplicação está trabalhando.

def parametros_servidor ():
    socket = {}
    socket ["ip"]= "localhost"
    socket ["port"] = 8080
    return socket

# Essa função ira ativar o firewall nos switches, será a primeira função a ser chamada.

def initial_status ():
    url_initial_status = urls ()    # Chamando a função urls
    url = url_initial_status ["url_initial_status"] # A url será armazenada na variável url
    socket = parametros_servidor () # Chamando a funcão parametros_servidor
    ip = socket ["ip"]  # O ip do servidor que está a aplicação será armazenado aqui
    port = socket ["port"] # A porta será armazenada aqui
    comment = http.client.HTTPConnection (ip, port)  # Essas proxímas linhas fara a requisição
    comment.request("PUT", url)                      # utilizando o método put
    response = comment.getresponse()

    status = response.status  # Retornara 200 se for aceita ou 404
    reacao = response.reason  # Retornara ok se a requisição for aceita
    dados = response.read ()  # Retornara em json o resultado o id_switche
    comment.close()

# Função responsável pelas regras utilizando o método post
def rules ():
    url_rules = urls ()
    newConditions = parametros_firewall ()
    conditionsSetURL = url_rules ["url_rules"]
    params = json.dumps(newConditions).encode('utf8')
    req = urllib.request.Request(conditionsSetURL, data=params,
                                headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)

    saida = response.read().decode('utf8') # Retornara em json o resultado o id_switche


# Função responsável por retornar o status do switche se está ativo ou não e sua id
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

# Função responsável por deleta as regras enviadas, OBS: Não está funcionando
def delete ():
    body = {"rule_id": "5"}
    conn = httplib.HTTPConnection('localhost', 8080)
    conn.request("DELETE", '/firewall/rules/0000000000000001', data = body)
    resp = conn.getresponse()
    content = resp.read()


# Função que ira mostrar todas as regras estabelecidas o switche
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


# Função para adquirir os logs de saída
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