from flask import Blueprint, render_template, url_for, flash
from werkzeug.utils import redirect
from GenDB import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField, \
    validators, TimeField, TextAreaField, FloatField, FieldList, Form, FormField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo

ricettario = Blueprint('ricettario', __name__)

class newSemi(FlaskForm):
    Nome = StringField(validators=[InputRequired()], render_kw={"placeholder": "Nome"})
    PrezzoUnitario = FloatField(validators=[InputRequired()], default=0.0)
    IVA = IntegerField(validators=[InputRequired()], default=0)
    Categoria = StringField(validators=[InputRequired()], render_kw={"placeholder": "Categoria"})
    Descrizione = TextAreaField('Inserire una piccola decrizione del nuovo prodotto', validators=[InputRequired()])

    submit = SubmitField('Prosegui')

class materiePrime:
    merce = list((session.query(Merce.Nome, Merce.Id).filter(Merce.MateriaPrima == True)))
    matPrime = []
    for i in range(0, len(merce)):
        matPrime.append((merce[i][0], merce[i][1]))

class IngredientiForm(Form):
    Quantità = FloatField('Quantità', default=0)

class newRecipe(FlaskForm):
    Ingrediente = FieldList(FormField(IngredientiForm), min_entries=len(materiePrime.matPrime))
    Persone = IntegerRangeField('Persone', [validators.NumberRange(min=1, max=20)], default=0)
    Tempo = IntegerField('Durata', validators=[InputRequired()])
    Preparazione = TextAreaField('Inserire preparazione', validators=[InputRequired()])

    submit = SubmitField('Aggiungi')

@ricettario.route('/ricettarioGestionale')
def ricettarioGestionale():
    recipes = session.query(Ingredienti.Id_Semilavorato).group_by(Ingredienti.Id_Semilavorato).count()

    if recipes == 0:
        flash("Non hai ricette.")
        return render_template("gestionale/ricettario.html", len_ricette=0)
    else:
        prod = session.query(Semilavorati.Nome, Semilavorati.Incipit, Immagini.img).\
            join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id).\
            join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img).\
            all()

        ing = list(session.query(Ingredienti, Merce).join(Merce).filter(Merce.Id == Ingredienti.Id_MateriaPrima))

        list_ric = []
        lista_aux = []


        for i in range(0, len(list(ing))):
            if i == 0:
                lista_aux.append((ing[i][1].Nome, ing[i][0].Quantita))
            else:
                if ing[i][0].Id_Semilavorato == ing[i-1][0].Id_Semilavorato:
                    lista_aux.append((ing[i][1].Nome, ing[i][0].Quantita))
                else:
                    list_ric.append(lista_aux)
                    lista_aux = []
                    lista_aux.append((ing[i][1].Nome, ing[i][0].Quantita))

        list_ric.append(lista_aux)

        return render_template("gestionale/ricettario.html", len_ricette = recipes, Prod=prod, Ing=list_ric, len_Ing=len(list_ric))

@ricettario.route('/addSemilavorato', methods=['GET', 'POST'])
def addSemi():
    form = newSemi()
    if form.validate_on_submit():
        new_Semi = Semilavorati(Nome=form.Nome.data, Preparazione='', IVA=form.IVA.data, Categoria=form.Categoria.data, Descrizione=form.Descrizione.data, PrezzoUnitario=form.PrezzoUnitario.data, Quantità=0, Incipit='', TempoPreparazione=0, Porzioni=1)
        db.session.add(new_Semi)
        db.session.commit()

        semi = session.query(Semilavorati.Id).filter(Semilavorati.Nome == form.Nome.data).first()
        form2 = newRecipe()

        return redirect(url_for("ricettario.aggiungiRicetta", id=semi[0], nome = form.Nome.data, form=form2, ing = materiePrime.matPrime, len_ing = len(materiePrime.matPrime)))

    return render_template("gestionale/addSemilavorato.html", form = form)


@ricettario.route('/addRicetta/<id>', methods=['GET', 'POST'])
def aggiungiRicetta(id):
    form = newRecipe()

    data = form.Ingrediente.data
    ingrediente = []
    for i in range(0, len(data)):
        ingrediente.append((data[i]['Quantità']))

    if(form.validate_on_submit()):
        for i in range(0, len(ingrediente)):
            if ingrediente[i] > 0 :
                new_Rec = Ingredienti(Id_Semilavorato = id, Id_MateriaPrima = materiePrime.matPrime[i][1], Quantita = ingrediente[i])
                db.session.add(new_Rec)

        Semilavorati.query.filter(Semilavorati.Id == id).update({"Preparazione":form.Preparazione.data, "Porzioni" : form.Persone.data, "TempoPreparazione" : form.Tempo.data})
        db.session.commit()

        return redirect(url_for('ricettario.ricettarioGestionale'))

    return render_template("gestionale/formRicette.html", form=form, ing = materiePrime.matPrime, len_ing = len(materiePrime.matPrime))

@ricettario.route('/ricetta/<id>', methods=['GET', 'POST'])
def ricetta(id):
    ricetta = session.query(Semilavorati.Nome, Semilavorati.Descrizione, Semilavorati.Incipit, Semilavorati.TempoPreparazione, Semilavorati.Preparazione, Semilavorati.Porzioni). \
        join(Ingredienti, Semilavorati.Id == Ingredienti.Id_Semilavorato). \
        filter(Semilavorati.Id == id).first()

    ingredienti = session.query(Merce.Nome, Ingredienti.Quantita, Allergeni.Nome).\
        join(Ingredienti, Ingredienti.Id_MateriaPrima == Merce.Id).\
        join(Allergeni, Allergeni.Id == Merce.Id_Allergene).\
        filter(Ingredienti.Id_Semilavorato == id).all()

    return render_template("gestionale/ricetteSingle.html", Ricetta=ricetta, Ingredienti=ingredienti)

