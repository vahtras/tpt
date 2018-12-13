import os
import flask
import flask_bootstrap
app = flask.Flask(__name__)
bs = flask_bootstrap.Bootstrap()
bs.__init__(app)

COURSE = 'async-techniques-python-course'

def list_transcripts(course, chapter=None):
    chapters = sorted(os.listdir(f'{course}/transcripts'))
    sections = ""
    if chapter:
        sections = sorted(os.listdir(f'{course}/transcripts/{chapter}'))
    return chapters, sections


@app.route('/')
def index():
    chapters, _ =  list_transcripts(COURSE)
    return flask.render_template('index.html', course=COURSE, chapters=chapters)

@app.route('/<chapter>')
def section(chapter):
    chapters, sections =  list_transcripts(COURSE, chapter)
    return flask.render_template('chapter.html', course=COURSE, chapter=chapter, chapters=chapters, sections=sections)

@app.route('/<chapter>/<section>')
def text(chapter, section):
    chapters, sections =  list_transcripts(COURSE, chapter)
    lines = [line.split(maxsplit=1)[1] for line in open(f'async-techniques-python-course/transcripts/{chapter}/{section}')]
    text = " ".join(lines)
    return flask.render_template('section.html', course=COURSE, chapter=chapter, section=section, text=text, chapters=chapters, sections=sections)

if __name__ == "__main__":
    app.run(debug=True)
