from flask import Markup
from itertools import product
import random

# maps strings to dictionaries
def domains():
    return {
        'font_size':['1em','1.3em','2em','0.8em','1.1em'],
        'font_family':['Arial Black', 'Comic Sans MS', 'Lucida Sans Unicode', 'Courier New', 'Trebuchet MS'],
        'label_text':['Home Address', 'Address', 'Shipping Address', 'Location', 'Direct Address'],
        'error_color':xrange(100),
        'error_text':['Invalid E-mail', 'Bad email', 'Invalid E-mail Address', 'Check E-mail', 'Re-try email'],
        'button_text':['Submit!','Submit', 'Buy now', 'Order', 'Complete payment', 'Ship!', 'Finish'],
        'button_style': [
            "-moz-box-shadow:inset 0px 1px 0px 0px #54a3f7;   -webkit-box-shadow:inset 0px 1px 0px 0px #54a3f7;   box-shadow:inset 0px 1px 0px 0px #54a3f7;   background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #007dc1), color-stop(1, #0061a7));   background:-moz-linear-gradient(top, #007dc1 5%, #0061a7 100%);   background:-webkit-linear-gradient(top, #007dc1 5%, #0061a7 100%);   background:-o-linear-gradient(top, #007dc1 5%, #0061a7 100%);   background:-ms-linear-gradient(top, #007dc1 5%, #0061a7 100%);   background:linear-gradient(to bottom, #007dc1 5%, #0061a7 100%);   filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#007dc1', endColorstr='#0061a7',GradientType=0);   background-color:#007dc1;   -moz-border-radius:3px;   -webkit-border-radius:3px;   border-radius:3px;   border:1px solid #124d77;   display:inline-block;   cursor:pointer;   color:#ffffff;   font-family:Arial;   font-size:13px;   padding:6px 24px;   text-decoration:none;   text-shadow:0px 1px 0px #154682;",
            "-moz-box-shadow:inset 0px 1px 0px 0px #cf866c; -webkit-box-shadow:inset 0px 1px 0px 0px #cf866c; box-shadow:inset 0px 1px 0px 0px #cf866c; background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #d0451b), color-stop(1, #bc3315)); background:-moz-linear-gradient(top, #d0451b 5%, #bc3315 100%); background:-webkit-linear-gradient(top, #d0451b 5%, #bc3315 100%); background:-o-linear-gradient(top, #d0451b 5%, #bc3315 100%); background:-ms-linear-gradient(top, #d0451b 5%, #bc3315 100%); background:linear-gradient(to bottom, #d0451b 5%, #bc3315 100%); filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#d0451b', endColorstr='#bc3315',GradientType=0); background-color:#d0451b; -moz-border-radius:3px; -webkit-border-radius:3px; border-radius:3px; border:1px solid #942911; display:inline-block; cursor:pointer; color:#ffffff; font-family:Arial; font-size:13px; padding:6px 24px; text-decoration:none; text-shadow:0px 1px 0px #854629; ",
            "-moz-box-shadow: 0px 10px 14px -7px #276873; -webkit-box-shadow: 0px 10px 14px -7px #276873; box-shadow: 0px 10px 14px -7px #276873; background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #599bb3), color-stop(1, #408c99)); background:-moz-linear-gradient(top, #599bb3 5%, #408c99 100%); background:-webkit-linear-gradient(top, #599bb3 5%, #408c99 100%); background:-o-linear-gradient(top, #599bb3 5%, #408c99 100%); background:-ms-linear-gradient(top, #599bb3 5%, #408c99 100%); background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%); filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#599bb3', endColorstr='#408c99',GradientType=0); background-color:#599bb3; -moz-border-radius:8px; -webkit-border-radius:8px; border-radius:8px; display:inline-block; cursor:pointer; color:#ffffff; font-family:Arial; font-size:20px; font-weight:bold; padding:13px 32px; text-decoration:none; text-shadow:0px 1px 0px #3d768a; ",
            "-moz-box-shadow:inset 0px 1px 0px 0px #bee2f9; -webkit-box-shadow:inset 0px 1px 0px 0px #bee2f9; box-shadow:inset 0px 1px 0px 0px #bee2f9; background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #63b8ee), color-stop(1, #468ccf)); background:-moz-linear-gradient(top, #63b8ee 5%, #468ccf 100%); background:-webkit-linear-gradient(top, #63b8ee 5%, #468ccf 100%); background:-o-linear-gradient(top, #63b8ee 5%, #468ccf 100%); background:-ms-linear-gradient(top, #63b8ee 5%, #468ccf 100%); background:linear-gradient(to bottom, #63b8ee 5%, #468ccf 100%); filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#63b8ee', endColorstr='#468ccf',GradientType=0); background-color:#63b8ee; -moz-border-radius:6px; -webkit-border-radius:6px; border-radius:6px; border:1px solid #3866a3; display:inline-block; cursor:pointer; color:#14396a; font-family:Arial; font-size:15px; font-weight:bold; padding:6px 24px; text-decoration:none; text-shadow:0px 1px 0px #7cacde; ",
            "-moz-box-shadow:inset 0px 1px 0px 0px #fbafe3; -webkit-box-shadow:inset 0px 1px 0px 0px #fbafe3; box-shadow:inset 0px 1px 0px 0px #fbafe3; background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #ff5bb0), color-stop(1, #ef027d)); background:-moz-linear-gradient(top, #ff5bb0 5%, #ef027d 100%); background:-webkit-linear-gradient(top, #ff5bb0 5%, #ef027d 100%); background:-o-linear-gradient(top, #ff5bb0 5%, #ef027d 100%); background:-ms-linear-gradient(top, #ff5bb0 5%, #ef027d 100%); background:linear-gradient(to bottom, #ff5bb0 5%, #ef027d 100%); filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bb0', endColorstr='#ef027d',GradientType=0); background-color:#ff5bb0; -moz-border-radius:6px; -webkit-border-radius:6px; border-radius:6px; border:1px solid #ee1eb5; display:inline-block; cursor:pointer; color:#ffffff; font-family:Arial; font-size:15px; font-weight:bold; padding:6px 24px; text-decoration:none; text-shadow:0px 1px 0px #c70067; ",
        ],
    }

def mutate(parameters):
    new = dict(**parameters)
    for attribute in new:
        if random.random() < 0.01:
            new[attribute] = random.choice(domains()[attribute])
    return new

def combine(parent_a, parent_b):
    new = genetic.combine_random(parent_a, parent_b)
    return new

# returns Markup object
def generate(parameters):
    print parameters
    def color2rgb(c):
        return '#%02x%02x%02x' % (c+155,c,c)
    font_size = parameters["font_size"]
    font_family = parameters["font_family"]
    label_text = parameters["label_text"]
    error_color = color2rgb(parameters["error_color"])
    error_text = parameters["error_text"]
    button_text = parameters["button_text"]
    button_style = parameters["button_style"]
    form = '''
<div style="width: 500px; height: 600px; font-size: %s; font-family: '%s';">
<form>
<label>%s:<br />
<input type="text" value="130 Beach Rd, Glencoe, IL 60022" style="border: 1px solid black; border-radius: 3px; padding: 5px; font-size: 1.1em;"/>
</label><br /><br />
<label style="color: %s">E-mail: <br />
<input type="text" value="@jserrino@@gmail.com" style="border: 1px solid %s; border-radius: 3px; padding:5px; font-size: 1.1em;"/><br />
<span>%s</span>
</label><br /><br />
<label>Payment Info:<br />
<input type="text" value="************0342" style="border 1px solid black; border-radius: 3px; padding: 5px; font-size: 1.1em;" />
</label><br /><br />
<button type="submit" style="%s">%s</button>
</form>
</div>

    ''' % (font_size, font_family, label_text, error_color, error_color, error_text, button_style, button_text)
    return Markup(form)
