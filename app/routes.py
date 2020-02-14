from flask import render_template, url_for, redirect
from app import app, nbrs, df
from app.forms import LegoPrefForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/user_input', methods=['GET', 'POST'])
def user_input():
    print ("loaded user_input")

    form = LegoPrefForm()
    num_selections_returned = 5

    if form.validate_on_submit():
        year = form.year.data
        selection = [form.piece_count.data, \
                form.difficulty.data, \
                form.star_rating.data, \
                year-1992, \
                form.price.data]

        dists, closest_ = nbrs.kneighbors([selection], n_neighbors=num_selections_returned, return_distance=True)
        print (df.iloc[closest_[0]])
        results_data = df.iloc[closest_[0]].to_dict('records')

        return render_template('results.html', title='Results', results_data=results_data)
    return render_template('set-decider.html', title='Set-Decider', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')