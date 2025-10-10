from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import pickle

model=pickle.load(open("model.pkl","rb"))

personality_traits = {
    'EXT1': "I am the life of the party",
    'EXT2': "I don't talk a lot",
    'EXT3': "I feel comfortable around people",
    'EXT4': "I keep in the background",
    'EXT5': "I start conversations",
    'EXT6': "I have little to say",
    'EXT7': "I talk to a lot of different people at parties",
    'EXT8': "I don't like to draw attention to myself",
    'EXT9': "I don't mind being the center of attention",
    'EXT10': "I am quiet around strangers",
    'EST1': "I get stressed out easily",
    'EST2': "I am relaxed most of the time",
    'EST3': "I worry about things",
    'EST4': "I seldom feel blue",
    'EST5': "I am easily disturbed",
    'EST6': "I get upset easily",
    'EST7': "I change my mood a lot",
    'EST8': "I have frequent mood swings",
    'EST9': "I get irritated easily",
    'EST10':"I often feel blue",
    'AGR1': "I feel little concern for others",
    'AGR2': "I am interested in people",
    'AGR3': "I insult people",
    'AGR4': "I sympathize with others' feelings",
    'AGR5': "I am not interested in other people's problems",
    'AGR6': "I have a soft heart",
    'AGR7': "I am not really interested in others",
    'AGR8': "I take time out for others",
    'AGR9': "I feel others' emotions",
    'AGR10': "I make people feel at ease",
    'CSN1': "I am always prepared",
    'CSN2': "I leave my belongings around",
    'CSN3': "I pay attention to details",
    'CSN4': "I make a mess of things",
    'CSN5': "I get chores done right away",
    'CSN6': "I often forget to put things back in their proper place",
    'CSN7': "I like order",
    'CSN8': "I shirk my duties",
    'CSN9': "I follow a schedule",
    'CSN10': "I am exacting in my work",
    'OPN1': "I have a rich vocabulary",
    'OPN2': "I have difficulty understanding abstract ideas",
    'OPN3': "I have a vivid imagination",
    'OPN4': "I am not interested in abstract ideas",
    'OPN5': "I have excellent ideas",
    'OPN6': "I do not have a good imagination",
    'OPN7': "I am quick to understand things",
    'OPN8': "I use difficult words",
    'OPN9': "I spend time reflecting on things",
    'OPN10': "I am full of ideas"
}

db=SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_inputs.db"

db.init_app(app)

class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    EXT1 = db.Column(db.Integer, nullable=False)
    EXT2 = db.Column(db.Integer, nullable=False)
    EXT3 = db.Column(db.Integer, nullable=False)
    EXT4 = db.Column(db.Integer, nullable=False)
    EXT5 = db.Column(db.Integer, nullable=False)
    EXT6 = db.Column(db.Integer, nullable=False)
    EXT7 = db.Column(db.Integer, nullable=False)
    EXT8 = db.Column(db.Integer, nullable=False)
    EXT9 = db.Column(db.Integer, nullable=False)
    EXT10 = db.Column(db.Integer, nullable=False)

    EST1 = db.Column(db.Integer, nullable=False)
    EST2 = db.Column(db.Integer, nullable=False)
    EST3 = db.Column(db.Integer, nullable=False)
    EST4 = db.Column(db.Integer, nullable=False)
    EST5 = db.Column(db.Integer, nullable=False)
    EST6 = db.Column(db.Integer, nullable=False)
    EST7 = db.Column(db.Integer, nullable=False)
    EST8 = db.Column(db.Integer, nullable=False)
    EST9 = db.Column(db.Integer, nullable=False)
    EST10 = db.Column(db.Integer, nullable=False)
    
    AGR1 = db.Column(db.Integer, nullable=False)
    AGR2 = db.Column(db.Integer, nullable=False)
    AGR3 = db.Column(db.Integer, nullable=False)
    AGR4 = db.Column(db.Integer, nullable=False)
    AGR5 = db.Column(db.Integer, nullable=False)
    AGR6 = db.Column(db.Integer, nullable=False)
    AGR7 = db.Column(db.Integer, nullable=False)
    AGR8 = db.Column(db.Integer, nullable=False)
    AGR9 = db.Column(db.Integer, nullable=False)
    AGR10 = db.Column(db.Integer, nullable=False)

    CSN1 = db.Column(db.Integer, nullable=False)
    CSN2 = db.Column(db.Integer, nullable=False)
    CSN3 = db.Column(db.Integer, nullable=False)
    CSN4 = db.Column(db.Integer, nullable=False)
    CSN5 = db.Column(db.Integer, nullable=False)
    CSN6 = db.Column(db.Integer, nullable=False)
    CSN7 = db.Column(db.Integer, nullable=False)
    CSN8 = db.Column(db.Integer, nullable=False)
    CSN9 = db.Column(db.Integer, nullable=False)
    CSN10 = db.Column(db.Integer, nullable=False)

    OPN1 = db.Column(db.Integer, nullable=False)
    OPN2 = db.Column(db.Integer, nullable=False)
    OPN3 = db.Column(db.Integer, nullable=False)
    OPN4 = db.Column(db.Integer, nullable=False)
    OPN5 = db.Column(db.Integer, nullable=False)
    OPN6 = db.Column(db.Integer, nullable=False)
    OPN7 = db.Column(db.Integer, nullable=False)
    OPN8 = db.Column(db.Integer, nullable=False)
    OPN9 = db.Column(db.Integer, nullable=False)
    OPN10 = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'Scores(id={self.id})'
    
@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':

        form_values = {}
        
        for q_no in personality_traits.keys():
            form_values[q_no] = int(request.form.get(f'btnradio{q_no}', 3))

        ext1_value = form_values['EXT1']
        ext2_value = form_values['EXT2']
        ext3_value = form_values['EXT3']
        ext4_value = form_values['EXT4']
        ext5_value = form_values['EXT5']
        ext6_value = form_values['EXT6']
        ext7_value = form_values['EXT7']
        ext8_value = form_values['EXT8']
        ext9_value = form_values['EXT9']
        ext10_value = form_values['EXT10']

        est1_value = form_values['EST1']
        est2_value = form_values['EST2']
        est3_value = form_values['EST3']
        est4_value = form_values['EST4']
        est5_value = form_values['EST5']
        est6_value = form_values['EST6']
        est7_value = form_values['EST7']
        est8_value = form_values['EST8']
        est9_value = form_values['EST9']
        est10_value = form_values['EST10']

        agr1_value = form_values['AGR1']
        agr2_value = form_values['AGR2']
        agr3_value = form_values['AGR3']
        agr4_value = form_values['AGR4']
        agr5_value = form_values['AGR5']
        agr6_value = form_values['AGR6']
        agr7_value = form_values['AGR7']
        agr8_value = form_values['AGR8']
        agr9_value = form_values['AGR9']
        agr10_value = form_values['AGR10']

        csn1_value = form_values['CSN1']
        csn2_value = form_values['CSN2']
        csn3_value = form_values['CSN3']
        csn4_value = form_values['CSN4']
        csn5_value = form_values['CSN5']
        csn6_value = form_values['CSN6']
        csn7_value = form_values['CSN7']
        csn8_value = form_values['CSN8']
        csn9_value = form_values['CSN9']
        csn10_value = form_values['CSN10']

        opn1_value = form_values['OPN1']
        opn2_value = form_values['OPN2']
        opn3_value = form_values['OPN3']
        opn4_value = form_values['OPN4']
        opn5_value = form_values['OPN5']
        opn6_value = form_values['OPN6']
        opn7_value = form_values['OPN7']
        opn8_value = form_values['OPN8']
        opn9_value = form_values['OPN9']
        opn10_value = form_values['OPN10']


        new_scores_entry = Scores(
            EXT1=ext1_value,
            EXT2=ext2_value,
            EXT3=ext3_value,
            EXT4=ext4_value,
            EXT5=ext5_value,
            EXT6=ext6_value,
            EXT7=ext7_value,
            EXT8=ext8_value,
            EXT9=ext9_value,
            EXT10=ext10_value,

            EST1=est1_value,
            EST2=est2_value,
            EST3=est3_value,
            EST4=est4_value,
            EST5=est5_value,
            EST6=est6_value,
            EST7=est7_value,
            EST8=est8_value,
            EST9=est9_value,
            EST10=est10_value,
            
            AGR1=agr1_value,
            AGR2=agr2_value,
            AGR3=agr3_value,
            AGR4=agr4_value,
            AGR5=agr5_value,
            AGR6=agr6_value,
            AGR7=agr7_value,
            AGR8=agr8_value,
            AGR9=agr9_value,
            AGR10=agr10_value,
            
            CSN1=csn1_value,
            CSN2=csn2_value,
            CSN3=csn3_value,
            CSN4=csn4_value,
            CSN5=csn5_value,
            CSN6=csn6_value,
            CSN7=csn7_value,
            CSN8=csn8_value,
            CSN9=csn9_value,
            CSN10=csn10_value,

            OPN1=opn1_value,
            OPN2=opn2_value,
            OPN3=opn3_value,
            OPN4=opn4_value,
            OPN5=opn5_value,
            OPN6=opn6_value,
            OPN7=opn7_value,
            OPN8=opn8_value,
            OPN9=opn9_value,
            OPN10=opn10_value,
        )

        db.session.add(new_scores_entry)
        db.session.commit()
        return redirect('/latest_data')

    return render_template('quiz.html', personality_traits=personality_traits)

@app.route('/clear', methods=['GET'])
def clear_database():
    db.drop_all()
    db.create_all()
    return redirect('/')

@app.route("/latest_data", methods=['GET'])
def latest_data():
    latest_scores_entry = Scores.query.order_by(Scores.id.desc()).first()
    if latest_scores_entry is not None:
        column_order = ['EXT1', 'EXT2', 'EXT3', 'EXT4', 'EXT5', 'EXT6', 'EXT7', 'EXT8', 'EXT9', 'EXT10',
                        'EST1', 'EST2', 'EST3', 'EST4', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10',
                        'AGR1', 'AGR2', 'AGR3', 'AGR4', 'AGR5', 'AGR6', 'AGR7', 'AGR8', 'AGR9', 'AGR10',
                        'CSN1', 'CSN2', 'CSN3', 'CSN4', 'CSN5', 'CSN6', 'CSN7', 'CSN8', 'CSN9', 'CSN10',
                        'OPN1', 'OPN2', 'OPN3', 'OPN4', 'OPN5', 'OPN6', 'OPN7', 'OPN8', 'OPN9', 'OPN10']
        scores_data = pd.DataFrame([[
            latest_scores_entry.EXT1, latest_scores_entry.EXT2, latest_scores_entry.EXT3,
            latest_scores_entry.EXT4, latest_scores_entry.EXT5, latest_scores_entry.EXT6,
            latest_scores_entry.EXT7, latest_scores_entry.EXT8, latest_scores_entry.EXT9,
            latest_scores_entry.EXT10, latest_scores_entry.EST1, latest_scores_entry.EST2,
            latest_scores_entry.EST3, latest_scores_entry.EST4, latest_scores_entry.EST5,
            latest_scores_entry.EST6, latest_scores_entry.EST7, latest_scores_entry.EST8,
            latest_scores_entry.EST9, latest_scores_entry.EST10, latest_scores_entry.AGR1,
            latest_scores_entry.AGR2, latest_scores_entry.AGR3, latest_scores_entry.AGR4,
            latest_scores_entry.AGR5, latest_scores_entry.AGR6, latest_scores_entry.AGR7,
            latest_scores_entry.AGR8, latest_scores_entry.AGR9, latest_scores_entry.AGR10,
            latest_scores_entry.CSN1, latest_scores_entry.CSN2, latest_scores_entry.CSN3,
            latest_scores_entry.CSN4, latest_scores_entry.CSN5, latest_scores_entry.CSN6,
            latest_scores_entry.CSN7, latest_scores_entry.CSN8, latest_scores_entry.CSN9,
            latest_scores_entry.CSN10, latest_scores_entry.OPN1, latest_scores_entry.OPN2,
            latest_scores_entry.OPN3, latest_scores_entry.OPN4, latest_scores_entry.OPN5,
            latest_scores_entry.OPN6, latest_scores_entry.OPN7, latest_scores_entry.OPN8,
            latest_scores_entry.OPN9, latest_scores_entry.OPN10
        ]], columns=column_order)
        selected_columns = ['EXT2','EXT4','EXT6','EXT10','OPN1','OPN2','OPN4','OPN6','AGR1','AGR3','AGR5','AGR7','CSN2','CSN4','CSN6','CSN8','EST2','EST4','EST5','EST6']
        scores_data[selected_columns]=scores_data[selected_columns].replace([1,2,5,4],[5,4,1,2])
        predictions=model.predict(scores_data)

        return render_template("/result.html", predictions=predictions)
        
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=False)