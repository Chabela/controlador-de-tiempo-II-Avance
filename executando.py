import panta
import sys
import os
import time
try:
    import pygtk
    require('2.0')
except:
    pass
try:
    import gtk
    from gtk import glade
    
except:
    print "no tienes el modulo instalado"
    time.sleep(2)
    sys.exit(1)

class time:
	
    def __init__(self):
        
        self.gladefile="tiempo.glade"
        self.conjuntos=gtk.glade.XML(self.gladefile)
        self.ventanaIngreso=self.conjuntos.get_widget("VentanaPrincipal")
        self.ventanaAviso=self.conjuntos.get_widget("ventanaaviso")
        self.diccionario={"on_BotonEnvio_clicked":self.on_BotonEnvio_clicked,
                          "on_botonojo_clicked":self.on_botonojo_clicked}
        self.conjuntos.signal_autoconnect(self.diccionario)
        self.ingresoTiempo=self.conjuntos.get_widget("EntradaDeTiempo")
##    def ventanaaviso(self,tiempo):
##        self.ventana=gtk.Window(gtk.POPUT)
##        self.etiqueta=gtk.Label(tiempo)
##        self.etiqueta.show()
##        self.boton=gtk.Button(self.etiqueta)
##        self.boton.show()
##        self.ventana.add(self.boton)
##        self.ventana.show()

    def on_BotonEnvio_clicked(self,widget):
        self.ventanaIngreso.destroy()
        import time
        while gtk.events_pending():
            gtk.main_iteration()
        tiempo=self.ingresoTiempo.get_text()
        tiempo=int(tiempo)
        time.sleep(tiempo)
        print tiempo
        panta.p()
    def on_botonojo_clicked(self,widget):
        print "adios"

    def on_BotonAdmin_clicked(self,widget):
        self.ventanaSuspension.destroy()
        
        
if __name__=="__main__":
    timetime=time()
    gtk.main()
