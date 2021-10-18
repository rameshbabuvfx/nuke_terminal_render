import os
import sys
import subprocess

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from UI import nukeTerminal_UI


class TerminalRender(nukeTerminal_UI.Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.package_path = os.path.dirname(__file__)
        self.selected_nuke_file = None

        with open(r"D:\PythonProjects\NukePython\nuke_terminal_render\cache\nukeExec.log", "r+") as exec:
            self.nuke_exec_path = exec.readline()
        self.nuke_exec_lineEdit.setText(self.nuke_exec_path)

        self.connect_ui()

    def connect_ui(self):
        self.browse_pushButton.clicked.connect(self.browse_nuke_exec)
        self.nuke_file_listWidget.itemClicked.connect(self.get_write_node_data)
        self.render_pushButton.clicked.connect(self.render_write_nodes)

    def browse_nuke_exec(self):
        self.nuke_exec_path = QFileDialog.getExistingDirectory(self)
        self.nuke_exec_lineEdit.setText(self.nuke_exec_path)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()
            for path in url:
                nuke_file_path = path.toLocalFile()
                if nuke_file_path.endswith(".nk"):
                    self.nuke_file_listWidget.addItem(nuke_file_path)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            selected_items = self.nuke_file_listWidget.selectedItems()
            for item in selected_items:
                row = self.nuke_file_listWidget.row(item)
                self.nuke_file_listWidget.takeItem(row)

    def get_write_node_data(self):
        self.selected_nuke_file = self.nuke_file_listWidget.currentItem().text()
        self.write_node_listWidget.clear()
        write_cmd = r"{} -t {}\writeNodeData.py {}".format(
            self.nuke_exec_path,
            self.package_path,
            self.selected_nuke_file
        )
        process = subprocess.Popen(write_cmd, stdout=subprocess.PIPE)
        write_node_data = process.communicate()[0].decode(encoding="utf-8")
        write_node_list = write_node_data.splitlines()
        for count, write_node in enumerate(write_node_list):
            if count > 1:
                self.write_node_listWidget.addItem(write_node)

    def render_write_nodes(self):
        self.terminal_plainTextEdit.clear()
        selected_write_nodes = self.write_node_listWidget.selectedItems()
        for node in selected_write_nodes:
            write_node_details = node.text()
            write_split = write_node_details.split(":")
            write_node_name = write_split[0]
            cmd = "{} -X {} {} {}".format(
                self.nuke_exec_path,
                write_node_name,
                self.selected_nuke_file,
                write_split[1]
            )
            self.render_thread = RenderThread(cmd=cmd)
            self.render_thread.render_log.connect(self.display_render_progress)
            self.render_thread.start()

    def display_render_progress(self, val):
        self.terminal_plainTextEdit.append(val)


class RenderThread(QThread):
    render_log = Signal(str)

    def __init__(self, cmd):
        super(RenderThread, self).__init__()
        self.cmd = cmd

    def run(self):
        render_process = subprocess.Popen(self.cmd, stdout=subprocess.PIPE)
        while True:
            render_log = render_process.stdout.readline().decode(encoding="utf-8")
            if render_log:
                render_progress = str(render_log)
            else:
                render_progress = "Render Completed"
                break
            self.render_log.emit(render_progress)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = TerminalRender()
    tool.show()
    sys.exit(app.exec_())
