

# @markdown

import base64
import subprocess
import time
import threading
import os
from IPython.display import display, HTML
import ipywidgets as widgets
from IPython.display import display, HTML

from IPython.display import HTML

# CSS import for Bree Serif font
css_import = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bree+Serif&display=swap');
</style>
"""

# CSS styles for widgets
widget_css = """
<style>
.bree-serif-regular {
  font-family: "Bree Serif", serif;
  font-weight: 400;
  font-style: normal;
}

.begin-popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #F0E68C;
    border: 2px solid #32CD32;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    z-index: 1000;
}
.begin-popup h2 {
    color: #32CD32;
}
.begin-popup p {
    color: #333333;
}
.begin-popup button {
    background-color: #32CD32;
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
}

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
    background-image: linear-gradient(to right, #00FF7F, #00FF7F);
}
.custom-accordion {
    width: 350px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, pink, pink) !important;
    padding: 10px !important;
    z-index: 9999 !important;
}
.custom-accordion .accordion-button {
    position: relative;
    overflow: hidden;
}
.custom-accordion .accordion-button::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1;
    opacity: 0;
    transition: opacity 0.3s ease;
}
.custom-accordion .accordion-button:hover::before {
    opacity: 1;
}
.custom-accordion .accordion-text {
    position: relative;
    z-index: 2;
    color: #000000;
}
</style>
"""

# HTML content for begin popup
begin_popup_html = """
<div class="begin-popup" id="begin-popup">
    <h2 class="bree-serif-regular">रूपांतरक ~ Rupantarak Installation Begin</h2>
    <p class="bree-serif-regular">Installation process has started & This will take a while...</p>
    <button onclick="close_begin_popup()" class="bree-serif-regular">Close</button>
</div>
<script>
    function close_begin_popup() {
        document.getElementById('begin-popup').style.display = 'none';
    }
    setTimeout(close_begin_popup, 10000); // Hide the popup after 10 seconds
</script>
"""

# Display CSS import
display(HTML(css_import))

# Display CSS styles for widgets
display(HTML(widget_css))

# Display begin popup HTML
display(HTML(begin_popup_html))

# Function to generate the main repo URL
def generate_main_repo_url():
    main_repo_url = "https://github.com/nick-arch/Rupantarak.git"
    encoded_repo_url = base64.b64encode(main_repo_url.encode()).decode()
    return encoded_repo_url

from IPython.display import HTML

def display_logo():
    logo_html = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Yatra+One&display=swap');

    .yatra-one-regular {
        font-family: 'Yatra One', sans-serif;
        font-weight: 400;
        font-style: normal;
    }
    </style>
    <div style='text-align: center;'><h1 style='font-family: Andika, sans-serif;'><span class="yatra-one-regular" style='color: pink; font-size: 44px;'>रूपांतरक <span style='color: black;'>~ </span></span><span style='color: white; font-size: 25px;'>Ꮢᥙραɳ𝜏αɾαƙ</span></br><br><span style='color: #00FF7F; font-size: 34px;'>вч νιѕнαℓ ѕнαямα</span></h1></div>
    """
    display(HTML(logo_html))

# Displaying the customized text logo
display_logo()
# Progress bar
progress = widgets.IntProgress(value=0, min=0, max=3, step=1, description='Loading:')
display(progress)

# Downloading and installing रूपांतरक ~ Rupantarak
encoded_url = generate_main_repo_url()
progress.value += 1

# Executing git clone command using subprocess
subprocess.run(["git", "clone", base64.b64decode(encoded_url).decode()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

progress.value += 1
os.chdir('/content/Rupantarak')
progress.value += 1


from IPython.display import HTML

html_content_1 = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Bree+Serif&family=Yatra+One&display=swap');

.bree-serif-regular {
  font-family: "Bree Serif", serif;
  font-weight: 400;
  font-style: normal;
}

.yatra-one-regular {
  font-family: "Yatra One", sans-serif;
  font-weight: 400;
  font-style: normal;
}
</style>

<div style="display: flex; justify-content: center; margin-top: 10px; margin-bottom: 10px;">
  <div style="width: 350px; margin: 10px 0;">
    <details id="details1">
      <summary id="summary1" style="border: none; border-radius: 8px; background: linear-gradient(to right, pink, pink); color: black; padding: 3px; text-align: center; cursor: pointer; list-style: none; font-weight: bold; margin-bottom: 10px;" class="bree-serif-regular">
        <span id="arrow1" class="bree-serif-regular">➼</span> <b class="bree-serif-regular">Must-Knows</b>
      </summary>
      <div style="border-radius: 8px; background-color: #222222; padding: 7px; color: white;" class="yatra-one-regular">
        The <span class="yatra-one-regular">रूपांतरक</span> ~ Ꮢᥙραɳ𝜏αɾαƙ installation process typically takes up to 8 minutes without GPU dependencies. However, if the NVIDIA CUDA Toolkit is available in your environment, it may extend the installation time to up to 12 minutes.
      </div>
    </details>
  </div>
</div>

<script>
  var details1 = document.getElementById('details1');
  var arrow1 = document.getElementById('arrow1');
  details1.addEventListener('toggle', function(event) {
    if (details1.open) {
      arrow1.textContent = '➷';
    } else {
      arrow1.textContent = '➼';
    }
  });
</script>
'''

display(HTML(html_content_1))

import time
import threading
import os
from IPython.display import display, HTML
import ipywidgets as widgets

# स्थनुप्रभॊ विश्वभावः स्वयम्भू शम्भूवामनः |
total_duration = 600
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


# सहस्रशीर्षा पुरुषः सहस्राक्षः सहस्रपात् ॥५॥
log_output = widgets.Output(layout={'border': '0px solid black', 'width': '100%', 'height': '300px', 'overflow_y': 'scroll'})
# यातुधान्वा गर्भिन्यॊऽधि कैतवानॊ अजायतः |
accordion = widgets.Accordion(children=[log_output])
accordion.set_title(0, 'Installation Logs')
accordion.selected_index = None
accordion.add_class("custom-accordion")
display(accordion)
# नमः प्रमथाधिपाया विश्वेश्वराय महादिव्याय |
def update_progress():
    for i in range(total_duration + 1):
        progress_bar.value = (i / total_duration) * 100
        time.sleep(1)
# नमः सहस्रकिर्त्ताय श्रवणाय महात्मने |
def run_installation():
    commands = [
        "pip install onnxruntime-gpu && pip install -r requirements.txt",
        "pip install onnxruntime-gpu --upgrade",
        "apt-get update --yes",
        "pip install gdown moviepy ipywidgets",
        "pip install pytube"
    ]
    with log_output:
        for command  in commands:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
            for line in iter(process.stdout.readline, ''):
                print(line, end='')
            process.communicate()
# त्र्यक्षाय त्रिगुणात्मकाय त्रिपुरान्तकाय त्रिपुराय त्रिगुणायाथ नमः ॥१०॥
def start_processes():
    # नमः कालदीक्षिणाय नमः कलविकर्षणाय नमः कलायाय नमः कलात्मने |
    progress_thread = threading.Thread(target=update_progress)
    progress_thread.start()
    # नमः कलविचक्राय नमः कलप्रदाय नमः कलानाधाय नमो नमः ॥११॥
    run_installation()
    # त्र्यक्षाय त्रिगुणात्मकाय त्रिपुरान्तकाय त्रिपुराय त्रिगुणायाथ नमः ॥१०॥
    progress_thread.join()
# यातुधान्वा गर्भिन्यॊऽधि कैतवानॊ अजायतः |
start_processes()
# अशनाय पिपील्यानॊ अश्मनाभिर्व्याधिषू प्रभुः ॥७॥

import subprocess
import threading
import time
from IPython.display import display, HTML
import ipywidgets as widgets

def check_cuda_availability():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False

def update_progress(progress_bar):
    total_duration = 150
    for i in range(total_duration + 1):
        progress_bar.value = (i / total_duration) * 100
        time.sleep(1)

def run_installation():
    if check_cuda_availability():
        display_heading()
        display_cuda_available_message()
        progress_bar = widgets.FloatProgress(
            value=0,
            min=0,
            max=100,
            layout=widgets.Layout(width='90%', margin='0 auto 0 auto')
        )
        display(progress_bar)
        progress_thread = threading.Thread(target=update_progress, args=(progress_bar,))
        progress_thread.start()

        commands = [
            "apt install nvidia-cuda-toolkit --yes",
            "pip install gdown",
        ]
        log_output = widgets.Output(layout={'border': '0px solid black', 'width': '100%', 'height': '300px', 'overflow_y': 'scroll'})
        accordion = widgets.Accordion(children=[log_output])
        accordion.set_title(0, 'Nvidia Cuda Toolkit Installation Logs')
        accordion.selected_index = None
        accordion.add_class("custom-accordion")
        display(accordion)
        
        with log_output:
            for command in commands:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
                for line in iter(process.stdout.readline, ''):
                    print(line, end='')
                process.communicate()
    else:
        display_cuda_not_available_message()

def display_heading():
    heading_html = """
    <style>
        .heading {
            text-align: center;
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 20px;
        }
    </style>
    <div class="heading">
        GPU Acceleration Nvidia Cuda Toolkit Installation
    </div>
    """
    display(HTML(heading_html))

def display_cuda_available_message():
    available_html = """
    <style>
        .available-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #D4EDDA;
            border: 2px solid #28A745;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .available-popup h2 {
            color: #28A745;
        }
        .available-popup p {
            color: #333333;
        }
    </style>
    <div id="available-popup" class="available-popup">
        <h2>CUDA toolkit is available for acceleration!</h2>
        <p>Proceeding with installation...</p>
    </div>
    <script>
        // Function to hide the popup after 2 seconds
        setTimeout(function() {
            var popup = document.getElementById('available-popup');
            popup.style.display = 'none';
        }, 12000);
    </script>
    """
    display(HTML(available_html))

def display_cuda_not_available_message():
    unavailable_html = """
    <style>
        .unavailable-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #F8D7DA;
            border: 2px solid #FFC107;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .unavailable-popup h2 {
            color: #DC3545;
        }
        .unavailable-popup p {
            color: #333333;
        }
    </style>
    <div id="unavailable-popup" class="unavailable-popup">
        <h2>CUDA toolkit is not available for acceleration</h2>
        <p>The CUDA toolkit is not detected in this environment.</p>
        <p>You can still enjoy the full functionality of our tool रूपांतरक through a CPU, even without GPU acceleration. No worries!</p>
    </div>
    <script>
        // Function to hide the popup after 2 seconds
        setTimeout(function() {
            var popup = document.getElementById('unavailable-popup');
            popup.style.display = 'none';
        }, 12000);
    </script>
    """
    display(HTML(unavailable_html))

run_installation()


from IPython.display import display, HTML

def display_rupantarak_confirmation():
    confirmation_html = """
    <style>
        .confirmation-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #F5F5DC;
            border: 2px solid #FA8072;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            z-index: 1000;
        }
        .confirmation-popup h2 {
            color: #ff0066;
        }
        .confirmation-popup p {
            color: #333333;
        }
        .confirmation-popup button {
            background-color: #FA8072;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    <div class="confirmation-popup" id="popup">
        <h2>Rupantarak Installation Complete Successfully</h2>
        <p>Click the button below to close this message, or it will disappear in 10 seconds.</p>
        <button onclick="close_popup()">Close</button>
    </div>
    <script>
        function close_popup() {
            document.getElementById('popup').style.display = 'none';
        }
        setTimeout(close_popup, 10000); // Hide the popup after 10 seconds
    </script>
    """
    display(HTML(confirmation_html))

# At the end of your notebook, after all installations and configurations
display_rupantarak_confirmation()
