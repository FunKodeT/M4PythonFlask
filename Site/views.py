#region <PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>--|
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v---/
#region <FINAL_PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
#region <IMPORTS> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <IMPORTS> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#region <BLUEPRINT> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
views = Blueprint('views', __name__)
#region <ROUTES> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v---/
@views.route('/', methods=['GET', 'POST'])
@login_required
#region <HOME> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='warning')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    return render_template('home.html', user=current_user)
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <HOME> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
@views.route('/delete-note', methods=['POST'])
#region <DELETE> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
def delete_note():
    print('read me')
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <DELETE> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^--\
# <ROUTES> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <BLUEPRINT> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <FINAL_PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
#^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>--|