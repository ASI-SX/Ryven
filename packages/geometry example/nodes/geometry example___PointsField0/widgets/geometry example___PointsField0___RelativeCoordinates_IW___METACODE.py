# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...


class %INPUT_WIDGET_TITLE%_PortInstanceWidget(...):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(%INPUT_WIDGET_TITLE%_PortInstanceWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.setStyleSheet('''

        ''')


    def get_val(self):
        ...


    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...


    # remove logs and stop threads and timers here
    def removing(self):
        pass # ...
