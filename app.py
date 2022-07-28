from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def get_dropdown_on_home():
    """Go to homepage that has a form with autogenerated prompt input sections
    based on the story loading"""

    return render_template("dropdown.html", stories = stories.values())

@app.get("/questions")
def get_form_on_home():
    """Go to homepage that has a form with autogenerated prompt input sections
    based on the story loading"""
    story_code = request.arg.get("value")
    story = stories[story_code]
    prompts = story.prompts

    return render_template("questions.html", prompts = prompts)

# route to result
@app.get("/results")
def go_to_story():
    """Show results of filled in story based on form input"""

    text = silly_story.generate(request.args)

    return render_template("results.html", text = text)

