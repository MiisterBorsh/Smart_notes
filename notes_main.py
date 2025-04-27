# notes_main.py
import json
from PyQt5.QtWidgets import QApplication, QInputDialog

notes = {
    "Welcome" : {
        "text" : "У цьому додатку можна створювати замітки з тегами...",
        "tags" : ["smart notes", "instruction"]
    }
}

json_filename = "smart_notes/notes_data.json"

def save_notes(notes):
    # Save notes to a JSON file
    global json_filename
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(notes, json_file, sort_keys=True, ensure_ascii=False)

# main app logic
app = QApplication([])

from notes_win import *

def read_notes():
    global notes
    with open(json_filename, "r", encoding="utf-8") as json_file:
        notes = json.load(json_file)
    notes_list.clear()
    notes_list.addItems(notes.keys())

read_notes()

def update_notes():
    global notes
    save_notes(notes)
    read_notes()

def show_note():
    # Display the selected note's text and tags
    if notes_list.selectedItems():
        item = notes_list.selectedItems()[0].text()
        text = notes[item]["text"]
        tags = notes[item]["tags"]
        note_edit.setText(text)
        tags_list.clear()
        tags_list.addItems(tags)

notes_list.itemPressed.connect(show_note)

def add_note():
    global notes
    note_name, ok = QInputDialog.getText(note_win, "Add Note", "Note name:")
    if ok and note_name != "":
        notes[note_name] = {
            "text" : "",
            "tags" : []
        }
        notes_list.addItem(note_name)
        update_notes()

def delete_note():
    global notes
    if len(notes_list.selectedItems()) > 0:
        item = notes_list.selectedItems()[0].text()
        del notes[item]
        update_notes()

def save_note():
    global notes
    if len(notes_list.selectedItems()) > 0:
        item = notes_list.selectedItems()[0].text()
        new_text = note_edit.toPlainText()
        notes[item]["text"] = new_text
        update_notes()

create_note_btn.clicked.connect(add_note)
delete_note_btn.clicked.connect(delete_note)
save_note_btn.clicked.connect(save_note)

def add_tag():
    global notes
    if len(notes_list.selectedItems()) > 0 and search_tag.text() != "":
        new_tag = search_tag.text()
        item = notes_list.selectedItems()[0].text()
        if new_tag not in notes[item]["tags"]:
            notes[item]["tags"].append(new_tag)
            tags_list.clear()
            tags_list.addItems(notes[item]["tags"])
            update_notes()

add2note_btn.clicked.connect(add_tag)

def show_tag():
    # Display selected tag in the search field
    if tags_list.selectedItems():
        tag = tags_list.selectedItems()[0].text()
        search_tag.setText(tag)

tags_list.pressed.connect(show_tag)

def untag_selected_tag():
    global notes
    if len(notes_list.selectedItems()) > 0 and len(tags_list.selectedItems()) > 0:
        item = notes_list.selectedItems()[0].text()
        tag = tags_list.selectedItems()[0].text()
        notes[item]["tags"].remove(tag)
        tags_list.clear()
        tags_list.addItems(notes[item]["tags"])
        update_notes()

untag_note_btn.clicked.connect(untag_selected_tag)

# Search notes by tag
def search_notes_by_tag():
    tag = search_tag.text()
    if tag:
        filtered_notes = {}
        for note, data in notes.items():
            if tag in data["tags"]:
                filtered_notes[note] = data
        notes_list.clear()
        notes_list.addItems(filtered_notes.keys())
    else:
        notes_list.clear()
        notes_list.addItems(notes.keys())

search_tag_notes_btn.clicked.connect(search_notes_by_tag)

app.exec_()
