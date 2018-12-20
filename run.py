import os
import re
import flask
import flask_bootstrap
app = flask.Flask(__name__)
bs = flask_bootstrap.Bootstrap()
bs.__init__(app)

COURSE = 'async-techniques-python-course'

def list_transcripts(course, chapter=None):
    chapters = nsorted(os.listdir(f'{course}/transcripts'))
    sections = ""
    if chapter:
        sections = nsorted(os.listdir(f'{course}/transcripts/{chapter}'))
    return chapters, sections

def nsorted(seq):
    def initial_numbers(item):
        num = int(re.match(r'^(\d+)', item).group(1))
        return num
    return sorted(seq, key=initial_numbers)

@app.route('/')
@app.route('/<course>')
def index(course=COURSE):
    chapters, _ =  list_transcripts(course)
    return flask.render_template('index.html', course=course, chapters=chapters)

@app.route('/<course>/<chapter>')
def section(course, chapter):
    chapters, sections =  list_transcripts(course, chapter)
    return flask.render_template('chapter.html', course=course, chapter=chapter, chapters=chapters, sections=sections)

@app.route('/<course>/<chapter>/<section>')
def text(course, chapter, section):
    chapters, sections =  list_transcripts(course, chapter)
    lines = [line.split(maxsplit=1)[1] for line in open(f'{course}/transcripts/{chapter}/{section}')]
    text = " ".join(lines)
    return flask.render_template('section.html', course=course, chapter=chapter, section=section, text=text, chapters=chapters, sections=sections)

#
if __name__ == "__main__":
    app.run(debug=True)
