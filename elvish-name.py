from flask import Flask, render_template, request

app = Flask(__name__)

def convert_to_elvish(name):
    elvish_mapping = {
        'a': 'al', 'b': 'bel', 'c': 'cel', 'd': 'dal', 'e': 'el',
        'f': 'fal', 'g': 'gal', 'h': 'hal', 'i': 'il', 'j': 'jal',
        'k': 'kel', 'l': 'lir', 'm': 'mal', 'n': 'nil', 'o': 'ol',
        'p': 'pal', 'q': 'qel', 'r': 'rel', 's': 'sil', 't': 'tal',
        'u': 'ul', 'v': 'val', 'w': 'wil', 'x': 'xal', 'y': 'yel',
        'z': 'zal'
    }

    elvish_name = []
    prev_char = None

    for char in name:
        char_lower = char.lower()
        if char_lower == prev_char:
            continue  # Skip consecutive duplicate letters
        elvish_name.append(elvish_mapping.get(char_lower, char_lower))
        prev_char = char_lower

    return ''.join(elvish_name)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        first_name = request.form['first_name'].lower()
        last_name = request.form['last_name'].lower()

        if first_name in ['nate', 'nathaniel'] and last_name == 'brown':
            message = "I cannot give you that information. You need to call the guy, man."
        else:
            elvish_first_name = convert_to_elvish(first_name)
            elvish_last_name = convert_to_elvish(last_name)
            message = f"Your Elvish name is: {elvish_first_name} {elvish_last_name}"

        return render_template('index.html', message=message)

    return render_template('index.html', message=None)

if __name__ == "__main__":
    app.run(debug=True)
