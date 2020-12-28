from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from base.modul import Modul

class PerhitunganWidget( QWidget ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self._modul : Modul
        self._modul = None

        self.layout = QVBoxLayout( self )
        self.layout.setAlignment( Qt.AlignTop )

    def set_modul( self, modul ):
        if self._modul != modul:
            self._modul = modul

    def add_modul( self ):
        if self._modul != None:
            pass
