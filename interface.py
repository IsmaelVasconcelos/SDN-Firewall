# coding=utf-8
#Para usar esse código é necessária a instalação do pygtk 3

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from os import system as s
protocol = ""
action = ""
rule_posit = ""
switch_nome_db = []
switch_id_db = []
class Firewall(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Firewall Ryu")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        self.set_default_size(500,200)
        self.set_border_width(10)

        self.ligar = Gtk.Switch()
        #self.ligar.set_active(True)
        self.ligar.connect("notify::active",self.Power)

        self.image = Gtk.Image()
        self.image.set_from_file("fogo.png")
#--------------------------Entradas--------------------------------
        self.entry = Gtk.Entry()
        self.entry.connect("activate",self.nomeSwitch)
        self.entry.set_alignment(0.5)

        self.entry2 = Gtk.Entry()
        self.entry2.connect("activate", self.nomeHost)
        self.entry2.set_alignment(0.5)

        self.switch_entryid = Gtk.Entry()
        self.switch_entryid.set_alignment(0.5)

        self.entry_posit = Gtk.Entry()
        #self.entry_posit.connect("activate",self.position_rule)
        self.entry_posit.set_alignment(0.5)
#------------------------Botões---------------------------------

        button1 = Gtk.Button(label = 'Bloquear')
        button1_2 = Gtk.Button(label = 'Desbloquear')
        button2 = Gtk.Button(label = 'Bloquear')
        button2_2 = Gtk.Button(label = 'Desbloquear')
        button3 = Gtk.Button(label = 'Bloquear')
        button3_2 = Gtk.Button(label = 'Desbloquear')
        button4 = Gtk.Button(label = 'Bloquear')
        button4_2 = Gtk.Button(label = 'Desbloquear')
        button5 = Gtk.Button(label = 'Bloquear')
        button5_2 = Gtk.Button(label = 'Desbloquear')
        separador = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        button1.connect("clicked",self.bloquear)
        button1_2.connect("clicked",self.desbloquear)
        button2.connect("clicked", self.bloquear_ICMP)
        button2_2.connect("clicked", self.desbloquear_ICMP)
        ajuda = Gtk.ToolButton.new_from_stock(Gtk.STOCK_DIALOG_QUESTION)
        info = Gtk.ToolButton.new_from_stock(Gtk.STOCK_INFO)
        info.connect("clicked", self.infoBox)
        ajuda.connect("clicked", self.janela_de_ajuda)
        ajuda.set_size_request(20,20)
        plusButton = Gtk.ToolButton.new_from_stock(Gtk.STOCK_ADD)
        plusButton.connect("clicked", self.MoreFunctions)

#----------------------Labels---------------------------------------
        label0 = Gtk.Label("Origem")
        label1 = Gtk.Label("TCP")
        label2 = Gtk.Label("ICMP")
        label3 = Gtk.Label("SSH")
        label4 = Gtk.Label("SMTP")
        label5 = Gtk.Label("Destino")
        self.id_Label = Gtk.Label("Id")
        self.nomeSwitch = Gtk.Label("")
        self.Label_posit = Gtk.Label("Posição")
        self.aviso = Gtk.Label('Aperte no botão de "?"')
#----------------------Organização de espaços-------------------------------
        grid = Gtk.Grid()
        grid.set_column_spacing(1)
        grid.set_column_homogeneous(False)
        grid.set_row_homogeneous(False)
        grid.set_row_spacing(5)
#-----------------posicionar e ligar widgets--------------------------------

        grid.attach(self.image, 0, 0, 7, 1)#Banner
        grid.attach(label0, 1, 1, 1, 1)
        grid.attach(self.entry2, 2, 2, 2, 1)
        #grid.attach(self.entry_posit, 3, )
        grid.attach(label5, 1, 2, 1, 1)
        grid.attach(self.entry, 2, 1, 2, 1)
        grid.attach(self.switch_entryid, 2, 3, 2, 1)
        grid.attach(self.entry_posit, 2, 4, 2, 1)
        grid.attach(self.Label_posit, 1, 4, 1, 1)
        grid.attach(self.id_Label, 1, 3, 1, 1)
        grid.attach(separador, 0, 5, 7, 1 )
        grid.attach(label1, 1, 6, 1, 1)
        grid.attach(label2, 1, 7, 1, 1)
        grid.attach(label3, 1, 8, 1, 1)
        grid.attach(label4, 1, 9, 1, 1)
        grid.attach(button1, 2, 6, 1, 1)
        grid.attach(button1_2, 3, 6, 1, 1)
        grid.attach(button2, 2, 7, 1, 1)
        grid.attach(button2_2, 3, 7, 1, 1)
        grid.attach(button3, 2, 8, 1, 1)
        grid.attach(button3_2, 3, 8, 1, 1)
        grid.attach(button4, 2, 9,1, 1)
        grid.attach(button4_2,3, 9, 1, 1)
        grid.attach(plusButton, 0, 10, 1, 1)
        grid.attach(ajuda, 0, 11, 1, 1)
        grid.attach(info, 0, 12, 1, 1)
        #grid.attach(self.ligar, 6, 11, 1, 1)
        grid.attach(self.aviso, 2, 13, 2, 1)


        self.add(grid)


#-------------------------Janelas------------------------------------
    def janela_de_ajuda(self, widget):
        window = Gtk.Window(title = "Ajuda")
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_default_size(500,500)
        window.set_resizable(False)
        imageHelp = Gtk.Image()
        imageHelp.set_from_file("green.jpg")

        grid2 = Gtk.Grid()
        window.escreve = Gtk.Label("Ajuda:\n\n\n"
                                    "● Primeiro digite o ip de origem e destino.\n"
                                    "● Logo após, escolha o id do switch e a posição\n"
                                    "  que a regra vai tomar.\n"
                                    "● Então escolha o que deseja fazer e pronto.\n\n\n"
                                    "O botão de '+' tem lugar para ligar e\n"
                                    "desligar o switch; além de adicionar nomes\n"
                                    "a eles para que você a se organizar.\n"
                                    "Você ainda pode listar os switchs e ver\n"
                                    'quais estão ligados apertando em "listar"')

        grid2.attach(window.escreve, 2,2,1,1)
        grid2.attach(imageHelp, 0,1,4,1)

        window.add(grid2)
        window.show_all()

    def MoreFunctions(self, widget):
        imageMore = Gtk.Image()
        imageMore.set_from_file("blue2.jpg")
        firewall2 = Gtk.Window(title = "Adicionais")
        firewall2.set_position(Gtk.WindowPosition.CENTER)
        firewall2.set_default_size(100,200)
        firewall2.set_resizable(False)

        grid3 = Gtk.Grid()
        self.switch_entry_id = Gtk.Entry()
        self.id_label = Gtk.Label("id")
        self.switch_entry_nome = Gtk.Entry()
        self.nome_label = Gtk.Label("Nome")
        self.valid_button = Gtk.Button("Validar")
        self.valid_button.connect("clicked",self.dataBase)
        self.listar_button = Gtk.Button("Listar")

        grid3.attach(imageMore,0,0,5,1)
        grid3.attach(self.switch_entry_id, 2, 1, 1, 1)
        grid3.attach(self.id_label, 1, 1, 1, 1)
        grid3.attach(self.switch_entry_nome, 2, 2, 1, 1)
        grid3.attach(self.nome_label, 1, 2, 1, 1)
        grid3.attach(self.valid_button, 3, 2, 1, 1)
        grid3.attach(self.ligar,3, 1, 1, 1)
        grid3.attach(self.listar_button,3, 3, 1, 1)
        firewall2.add(grid3)
        firewall2.show_all()
#-------------------------Fim janelas/Inicio...----------------------------------------
    def infoBox(self, widget):
        infoBox = Gtk.Window(title = "Sobre")
        infoBox.set_position(Gtk.WindowPosition.CENTER)

        grid5 = Gtk.Grid()
        info = ("Programa criado por:\n"\
                "Ismael Lima: Implementação do firewall Ryu.\n"\
                "Wallace Rocha: Interface gráfica.")
        informacao = Gtk.Label(info)
        grid5.attach(informacao,0,0,1,1)
        infoBox.add(grid5)
        infoBox.show_all()

#------------------Funções-------------------------
    def nomeSwitch(self, entry):
        if len(self.entry.get_text()) == 0:
            self.aviso.set_text("Falta parametros")
        else:
            nome = self.entry.get_text()+" configurado"
            self.aviso.set_text(nome)

    def nomeHost(self, entry):
        if len(self.entry2.get_text()) == 0:
            self.aviso.set_text("Falta parametros")
        else:
            self.Host = (self.entry2.get_text() + " configurado")
            self.aviso.set_text(self.Host)

    def dataBase(self, widget):

        switch_nome_db = self.switch_entry_nome.get_text()
        switch_id_db = self.switch_entry_id.get_text()

        print_db = switch_id_db +" "+ switch_nome_db
        self.aviso.set_text(print_db)



    def bloquear(self, widget):
        print("botão funcionando.")
    def desbloquear(self, widget):
        print("botão funcionando.")

    def bloquear_ICMP(self, widget):
        protocol = "ICMP"
        action = "REJECT"
        self.aviso.set_text("ICMP bloqueado")

    def desbloquear_ICMP(self, widget):
        protocol = "ICMP"
        action = "ALLOW"
        self.aviso.set_text("ICMP desbloqueado")


    def Power(self, button, active):
        if button.get_active():
            self.aviso.set_text('Switch ligado')
        else:
            self.aviso.set_text('Switch desligado')






window = Firewall()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()