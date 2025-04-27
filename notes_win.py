from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QTextEdit, QListWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
)

note_win = QWidget()
note_win.setWindowTitle("Розумні замітки")
note_win.setGeometry(100,150,800,600)

main_layout = QHBoxLayout()
note_edit = QTextEdit('''
                      Деякий текст що буде відображатися
                      в замітках''')
main_layout.addWidget(note_edit, stretch=2)

right_layout = QVBoxLayout()
notes_list_lbl = QLabel("Перелік заміток:")
right_layout.addWidget(notes_list_lbl, alignment=Qt.AlignTop, stretch=1)

notes_list = QListWidget()
notes_list.addItems(["Нотатка 1","Нотатка 2","Нотатка 3"])
right_layout.addWidget(notes_list, stretch=6)

hbox1 = QHBoxLayout()

create_note_btn = QPushButton("Створити замітку")
hbox1.addWidget(create_note_btn)

delete_note_btn = QPushButton("Видалити замітку")
hbox1.addWidget(delete_note_btn)

right_layout.addLayout(hbox1, stretch=1)

save_note_btn = QPushButton("Зберегти замітку")
right_layout.addWidget(save_note_btn, stretch=1)

tags_list_lbl = QLabel("Перелік тегів:")
right_layout.addWidget(tags_list_lbl, stretch=1)

tags_list = QListWidget()
tags_list.addItems(["tag 1", "tag 2"])
right_layout.addWidget(tags_list, stretch=6)

search_tag = QLineEdit()
search_tag.setPlaceholderText("Введіть тег...")
right_layout.addWidget(search_tag, stretch=1)

hbox2 = QHBoxLayout()

add2note_btn = QPushButton("Додати до замітки")
hbox2.addWidget(add2note_btn)

untag_note_btn = QPushButton("Відкрипити замітки")
hbox2.addWidget(untag_note_btn)

right_layout.addLayout(hbox2, stretch=1)

search_tag_notes_btn = QPushButton("Шукати замітки за тегом")
hbox2.addWidget(search_tag_notes_btn, stretch=1)

main_layout.addLayout(right_layout, stretch=1)
note_win.setLayout(main_layout)
note_win.show()

