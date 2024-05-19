from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def hello():
    page_color = os.getenv('PAGE_COLOR', 'white')  # Default color is white
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body {{
                background-color: {page_color};
                color: black;
                text-align: center;
                padding-top: 20%;
                font-family: Arial, sans-serif;
            }}
        </style>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
