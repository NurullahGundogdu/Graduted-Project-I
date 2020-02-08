from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

from graph_tool.all import *
import os 

file_path = None

def draw_graph(file_path) : 

    g = Graph(directed = False)

    file = open(file_path)
    # format check yap 
    
    a = file.readlines()
    list_of_edges = [None] * len(a)
    for i in range(len(a)) : 
        list_of_edges[i] = [a[i][0],a[i][2]]

    vertices = {}

    for e in list_of_edges:
        if e[0] not in vertices:
            vertices[e[0]] = True
        if e[1] not in vertices:
            vertices[e[1]] = True


    for d in vertices:
        vertices[d] = g.add_vertex()


    for edge in list_of_edges:
        g.add_edge(vertices[edge[0]], vertices[edge[1]])

    ### yukarıda ki txt den edge ve vertex okumak ve olusturmak icin ###

    vertex_color = g.new_vertex_property("string")

    for r in g.vertices():
        vertex_color[r] = "#9FFF33"


    g.vertex_properties["color"] = vertex_color


    edge_color = g.new_edge_property("string")

    for r in g.edges():
        edge_color[r] = "#33E9FF"


    g.edge_properties["color"] = edge_color


    print(graph_tool.draw.graph_draw(g, edge_color = edge_color,vertex_fill_color = vertex_color,vertex_text = g.vertex_index  ))


class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
        elif answer & QMessageBox.Cancel:
            e.ignore()


def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path
    if file_path != None : 
        draw_graph(file_path)





def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)

def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        file_path = path
        save()

def show_about_dialog():
    text = "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    QMessageBox.about(window, "About Text Editor", text)




if __name__ == "__main__" :

    app = QApplication([])
    app.setApplicationName("MAXIMUM INDUCED MATCH")
    #text = QPlainTextEdit()
    window = QMainWindow()
    window.resize(500,500)
    #window.setCentralWidget(text)

    #QMainWindow.__init__(self)



    menu = window.menuBar().addMenu("&File")
    open_action = QAction("&Open")
    open_action.triggered.connect(open_file)
    open_action.setShortcut(QKeySequence.Open)
    menu.addAction(open_action)

    save_action = QAction("&Save")
    save_action.triggered.connect(save)
    save_action.setShortcut(QKeySequence.Save)
    menu.addAction(save_action)

    save_as_action = QAction("Save &As...")
    save_as_action.triggered.connect(save_as)
    menu.addAction(save_as_action)

    close = QAction("&Close")
    close.triggered.connect(window.close)
    menu.addAction(close)

    help_menu = window.menuBar().addMenu("&Help")
    about_action = QAction("&About")
    help_menu.addAction(about_action)
    about_action.triggered.connect(show_about_dialog)



    help_menu = window.menuBar().addMenu("&Create Random Graph")
    about_action = QAction("&About")
    about_action2 = QAction("&mal olmada")
    help_menu.addAction(about_action)
    help_menu.addAction(about_action2)
    about_action.triggered.connect(show_about_dialog)
    about_action2.triggered.connect(show_about_dialog)
    
    window.show()
    app.exec_()

