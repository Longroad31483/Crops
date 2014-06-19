from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """This class create a group of radio buttons from a given list of labels"""

    #Constructor
    def __init__(self,label,instruction,button_list):
        super().__init__() #Call the super class constructor
        #Create widgets
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()
        
        #Create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))
            
        #set the default checked item
        self.radio_button_list[0].setChecked(True)

        #Create layout
        self.radio_button_layout = QVBoxLayout()

        #Add buttons to the layout and button group
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each,counter)
            couter += 1

        #Add radio buttons to the group box
        self.radio_group.box.setLayout(self.radio_button_layout)
        
        #create a layout for whole widget
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)

        #set the layout for this widget
        self.setLayout(self.main_layout)

    #Method to find out the selected button
    def selected_button(self):

        ################################# http://www.pythonschool.net/radiobuttonwidget/
        ############### 11:14
        
