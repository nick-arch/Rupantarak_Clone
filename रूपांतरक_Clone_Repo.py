
# @markdown

import base64
import subprocess
import time
import threading
import os
from IPython.display import display, HTML
import ipywidgets as widgets
# नमस्ते रुद्रमन्यव उतोत इषवेनमः |
gradient_button_css = """
<style>

.progress {
    width: 100%;
    height: 30px;
    background-color: #222222;
    border-radius: 15px;
    margin-bottom: 20px;
    overflow: hidden;
}
.progress-bar {
    border-radius: 20px;
    background-image: linear-gradient(to right, #FA8072, #D8D8B4);
}
.custom-accordion {
    width: 380px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, #FA8072, #F5F5DC) !important;
    padding: 10px !important;
    z-index: 9999 !important;
}
.widget-container {
    border: none !important;
    background-color: #383838 !important; /* Background color changed */
    box-shadow: none !important;
    padding: 10px; /* Added padding */
    border-radius: 5px; /* Added border-radius */
}
.custom-accordion .custom-content {
    background-color: #F5F5DC !important;
    padding: 5px;
}
</style>
"""
# नमः प्रत्नय तॊषया गिरिश विप्रेषया ॥१॥
display(HTML(gradient_button_css))

# नमः पिपिव्याया च अम्भया च अर्णवाया च |
def display_logo():
    logo_html = """
    <div style='text-align: center;'>    <h1 style='font-family: Andika, sans-serif; font-size: 50px; background: -webkit-linear-gradient(left, #FA8072, #F5F5DC); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Rupantarak</span><br><span style='font-size: 18px;'>By Vishal Sharma</span><br><span style='color: #ff0066; font-size: 22px;'>ॐ नमः पार्वती पतये, हर-हर महादेव:</span></h1>
    </div>    """
    display(HTML(logo_html))
# नमः शिवाय च शर्वाय च महादेवाय च |
display_logo()


import os
import subprocess
import re
import time
from ipywidgets import IntProgress, VBox, HTML
from IPython.display import display

def generate_main_repo_url():
    main_repo_url = "https://github.com/nick-arch/Rupantarak.git"
    encoded_repo_url = base64.b64encode(main_repo_url.encode()).decode()
    return encoded_repo_url

# Define a function to display the gradient text logo
def display_logo():
    logo_html = """
    <div style='text-align: center;'>    <h1 style='font-family: Andika, sans-serif; font-size: 50px; background: -webkit-linear-gradient(left, #2196f3, #800080); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Rupantarak</span><br><span style='font-size: 18px;'>By Vishal Sharma</span><br><span style='color: #ff0066; font-size: 22px;'>ॐ नमः पार्वती पतये, हर-हर महादेव:</span></h1>
    </div>    """
    display(HTML(logo_html))

# Display the gradient text logo
display_logo()


# Progress bar
progress = widgets.IntProgress(value=0, min=0, max=3, step=1, description='Loading:')
display(progress)

# Downloading and installing रूपांतरक ~ Rupantarak

encoded_url = generate_main_repo_url()
progress.value += 1
!git clone $(echo {encoded_url} | base64 --decode) > /dev/null 2>&1 || true
progress.value += 1
os.chdir('/content/Rupantarak')
progress.value += 1

display(HTML(html_content_1))

# स्थनुप्रभॊ विश्वभावः स्वयम्भू शम्भूवामनः |
total_duration = 700
# स भूमिं विश्वतो वर्त्त्या आत्मानं च जगत् स्थितं |
layout = widgets.Layout(width='90%', margin='0 auto 0 auto')
progress_bar = widgets.FloatProgress(
    value=0,
    min=0,
    max=100,
    layout=layout
)
# संभूतं च चराचरं तस्मै संभवाय नमः ॥६॥
display(progress_bar)
