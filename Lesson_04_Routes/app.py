from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
            <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLS</h2>
<ul>
    <li><a href="/user/john">User profile: john</a></li>
    <li><a href="/user/alice">User profile: alice</a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
</ul>
'''
@app.route('/user/<username>', methods=['GET'])
def user_profile(username):
    return f'''
    <h1>User Profile</h1>
 <p>Username: <strong>{username}</strong></p>
 <p>Profile Type: {type(username)}</p>
 <p>Welcome to {username}'s profile page!</p>
 <nav>
    <a href="/">Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/Bob">Bob</a>
 </nav>
'''
# @app.route("/calc/<int:num1>/<operation>/<int:num2>")
# def calculator(num1,operation,num2):
#     operations = {
#         '+' : num1 + num2,
#         '-' : num1 - num2,
#         '*' : num1 * num2,
#         '/' : num1 / num2 if num2 !=0 else 'Error:Division by zero!',


#     }
#     if operation in operations:
#         result = operations[operation]
#         return f"{num1} {operation} {num2} = {result}"
#     else:
#         return f"Unknown operation!{operation}"
# @app.route("/temp_calc/<unit>/<float:temp>")
# def temperature_converter(unit, temp):
#     units = {
#         'C':(temp * 9/5) + 32,
#         'F':(temp - 32) * 5/9,
#     }
#     if unit in units:
#         converted_temp = units[unit]
#         if unit == 'C': target_unit = 'F'
#         else: target_unit = 'C'

#         return f"{temp} {unit} is equal to {converted_temp:.2f} to {target_unit}."
#     else:
#         return f"Unknown unit!{unit}"

@app.route("/temp_calc/<unit>/<float:temp>")
def temperature_converter(unit, temp):
    units = {
        'C': (temp * 9/5) + 32,
        'F': (temp - 32) * 5/9,
    }
    if unit in units:
        converted_temp = units[unit]
        target_unit = 'F' if unit == 'C' else 'C'
        return f"{temp}°{unit} is equal to {converted_temp:.2f}°{target_unit}."
    else:
        return f"Unknown unit: {unit}"
    

if __name__ == '__main__':
    app.run(debug=True)