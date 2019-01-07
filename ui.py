from cefpython3 import cefpython as cef
import base64
import platform
import sys
import threading
import subprocess
import glob
import time
import queue

from Abstract import Parser

parser = Parser()
# parser.fromTexttoXML('./dossier/Lin_2004_Rouge.txt')
# parser.fromTexttoTXT('./dossier/Lin_2004_Rouge.txt')
# parser.fromPDFtoXML('./dossier/Lin_2004_Rouge.pdf')
# parser.fromPDFtoTXT('./dossier/Lin_2004_Rouge.pdf')

APP_NAME = 'PDF Parser 1.1'

wd=''
gl = parser.listDir(wd)

files = []

FCNT = len(gl)

HTML_code = """
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
    .window { background: #F3F3F2; height: 100%; display: flex; flex-direction: column; transition: .2s all ease-in-out;}
    body { margin: 0; background: #F3F3F2; height: 100%;}
    .toolbar{ display: -webkit-flex; display: -ms-flexbox; display: flex;
    -webkit-flex-wrap: nowrap; -ms-flex-wrap: nowrap; flex-wrap: nowrap;
    box-sizing: border-box; padding-left: 8px; max-height: 80px; margin-bottom:
    0px; min-height: 56px;}
    .button { color: #424242; text-decoration: none; margin: 0; font-size: 14px;
    font-weight: 400; letter-spacing: 0; opacity: .87;
    line-height: 0px; padding: 0 24px; transition: .2s all ease-in-out;
    padding: 8px; max-height: 64px; overflow:  hidden;
    border:  0; border-radius: 32px; margin: 8px 4px; box-shadow: inset 0 0 0 1px #697F8A;
    background: transparent; min-width: 40px;}
    .button span { display: block; text-align: center; }
    .button:focus {outline: none;}
    .button:hover { background: rgba(105, 127, 138, .3); cursor: pointer; transition: .2s all
    ease-in-out; box-shadow: inset 0 0 64px 32px rgba(105, 127, 138, .3); outline:none;}
    .list { margin: 8px; background: #1E1E21; color: #eee; margin-top: 0; flex-grow: 1;}
    .files { padding: 0; margin: 0; padding-bottom: 8px;}
    .status { margin: 8px 16px; }
    .ico { width: 24px; height:  24px; }
    li.fhead { background:  #2F2F34; display:  flex; }
    .tb-e { padding:  8px 0; }
    .tb1 {width: 40px; overflow: hidden; text-overflow: ellipsis; padding-left:
    8px; min-width: 40px;}
    input[type="checkbox"]:hover { cursor:  pointer; }
    .sep { width: 1px; background: #5E6063; margin: 12px 8px; opacity: .8; }
    h1.big { line-height: 16px; font-weight: lighter; color: #5E6063; }
    li.file { padding-left: 8px; display: flex;}
    button:disabled:hover, button[disabled]:hover { box-shadow: inset 0 0 0 1px
    #697F8A; background: inherit; cursor: default; }
    button:disabled, button[disabled] { opacity:  .5; }
    body,html { font-family: Arial; font-size: 11pt; height: 100%; overflow: hidden;}
    div.msg { margin: 0.2em; line-height: 1.4em; }
    #XoT.act { box-shadow: inset 0 0 0 2px #C94F53; }
    #XoT.act .b-red{ fill: #C94F53 !important; }
    #XoT.act:hover { background: rgba(201, 79, 83, .3); }
    .tb-e.tb1 input { width: 16px; height: 16px; background: #eee; padding: 0;
    margin: 0; border-radius: 50%; margin-left: 4px; }
    b { background: #ccc; font-weight: bold; font-size: 10pt;
        padding: 0.1em 0.2em; }
    b.Python { background: #eee; }
    i { font-family: Courier new; font-size: 10pt; border: #eee 1px solid;
        padding: 0.1em 0.2em; }
    .left { float: right; margin-left: auto; margin-right: 4px; }
    .reduced .left { opacity:  0; }
    .settings { -ms-flex-direction: column; -webkit-box-direction: normal;
    -webkit-box-orient: vertical; bottom: 0; display: -webkit-box; display:
    -ms-flexbox; display: flex; flex-direction: column; left: 0; position:
    absolute; right: 0; top: 0; background:  #F3F3F2; z-index: -1; transition: .2s all ease-in-out;
    opacity: 0; flex-direction: row; transform: scale(1.2) translateZ(0px);
    transition: .2s all ease-in-out;}
    .settings.visible {z-index: 1; animation: pop 0.3s 0s ease-in-out 1 forwards;}
    .button.fixed { width:  40px; height:  40px; right: 4px; top: 4px; position:
    absolute; z-index: 99;}
    .settings .pane { -webkit-box-flex: 1; -webkit-box-pack: end; display:
    -webkit-box; display: -ms-flexbox; display: flex; justify-content: flex-end;
    z-index: 1;}
    .panels-menu li:hover { cursor:  pointer; background: rgba(243, 243, 242,
    .1); transition:  .2s all ease-in-out; }
    .panels-menu li { transition: .2s all ease-in-out; border-left:  0px; }
    .p0 { flex: 1 0 218px; background: #2F2F34; color: rgba(255,255,255,.8);
    font-size: 1.12em;}
    .p1 { flex: 1 1 800px; }
    ul.panels-menu { margin-bottom: 0; padding-left: 0; list-style: none;
    position: relative; min-width: 15em; max-width: 20em; margin-top: 3em;}
    .panels-content { margin-top: 3em; padding: 0px 40px; width: 100%; color:
    #5E6063; display: none;}
    .panels-content.active { display: block;}
    .pane-title { font-size: 1.75em; font-weight: bold; line-height:  1;
    margin-bottom: .75em; margin-top:  0; color: #2F2F34; }

    .panels-menu li a { padding: 0.75em 1.5em; transition: .2s all ease-in-out;
    display: block; margin-bottom: .5em;}
    .panels-menu li.selected{ border-left:  8px solid; border-color: #F3F3F2; }
    .reduced {transform: scale(.9) translateZ(0px); }
    .grow {transform: scale(.9) translateZ(0px);opacity: 0; transition: .2s all ease-in-out; }
    .animated { animation: show 0.3s 0.25s ease-in-out 1 forwards; opacity: 0;
    transform: translate(7%, 0); transition: height 2s ease-in-out; overflow: hidden; max-width: 90%;}
    .animated:nth-child(1) {animation-delay: .2s;}
    .animated:nth-child(2) {animation-delay: .3s;}
    .animated:nth-child(3) {animation-delay: .4s;}
    .animated:nth-child(4) {animation-delay: .5s;}
    .animated:nth-child(5) {animation-delay: .6s;}
    .animated:nth-child(6) {animation-delay: .7s;}
    .animated:nth-child(7) {animation-delay: .8s;}
    .animated:nth-child(8) {animation-delay: .9s;}
    .animated:nth-child(9) {animation-delay: 1s;}
    .animated:nth-child(10) {animation-delay: 1.1s;}
    .animated:nth-child(11) {animation-delay: 1.2s;}
    .animated:nth-child(12) {animation-delay: 1.3s;}
    .animated:nth-child(13) {animation-delay: 1.4s;}
    @keyframes show { 100% { opacity: 1; transform: translate(0,0); max-width:
    100%; } }
    @keyframes pop { 100% { opacity: 1; transform: scale(1) translateZ(0px); max-width:
    100%; } }

    </style>

    <script>
    var XML = false;
    function anyChecked() {
        var inp = document.getElementsByClassName("checkb");
        for (var i = 0; i < inp.length; i++)
            if (inp[i].type == "checkbox")
                if (inp[i].checked)
                    return true;
        return false;
    }
    function js_alert(msg) {
        alert(msg);
    }
    function flsSet(html) {
        var elem = document.querySelector('#fls');
        elem.innerHTML = html;
    }
    function flsAdd(html) {
        var elem = document.querySelector('#fls');
        elem.innerHTML += html;
    }
    function js_print(lang, event, msg) {
        msg = "<b class="+lang+">"+lang+": "+event+":</b> " + msg;
        console = document.getElementById("console")
        console.innerHTML += "<div class=msg>"+msg+"</div>";
    }

    function js_callback_1(ret) {
        js_print("Javascript", "html_to_data_uri", ret);
    }

    function js_callback_2(msg, py_callback) {
        js_print("Javascript", "js_callback", msg);
        py_callback("String sent from Javascript");
    }

    function setPane(pane) {
        document.querySelector(".selected").classList.remove("selected");
        document.querySelector(".l"+pane).classList.add("selected");
        document.querySelector(".active").classList.remove("active");
        document.querySelector("#"+pane).classList.add("active");
    }

    function menu() {
        if(document.querySelector(".window").classList.contains('reduced')) {
            //open
            document.querySelector(".settings").classList.remove("visible");
        } else {
            document.querySelector(".settings").classList.add("visible");
        }
        document.querySelector(".window").classList.toggle('reduced');
    }

    function plop(msg) {
        console.innerHTML += "<div class=msg>"+msg+"</div>";
        lol(msg);
    }

    function addFile(f) {
        console.innerHTML += "<div class=msg>"+f+"</div>";
        add_file(f);
    }

    function XoT() {
        XML = !XML;
        var elem = document.querySelector('#XoT');
        elem.classList.toggle("act");
    }

    function parseF() {
        if(anyChecked()) {
            var elem = document.querySelector('#fls');
            elem.innerHTML = "<h4 class='status'>Working . . .</h4>";
            document.getElementById("add").disabled = true;
            document.getElementById("start").disabled = true;
            document.getElementById("XoT").disabled = true;
            parse(js_callback_1, XML);
        } else {
            alert('None checked');
        }
    }

    window.onload = function(){
        html_to_data_uri("test", js_callback_1);
    };
    </script>
</head>
<body>
    <div class="window">
        <div class="toolbar">
            <button id="add" class="button" onclick="lol('btn')">
                <svg class="ico" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <path style="isolation:auto;mix-blend-mode:normal" fill="#303f46" d="M12 11l-1 1v9h2v-8h8v-2z" color="#000" overflow="visible"/>
                  <path style="isolation:auto;mix-blend-mode:normal" fill="#546e7a" d="M11 13l2-2V3h-2v8H3v2h8z" color="#000" overflow="visible"/>
                </svg>
            </button>
            <!--button class="button" onclick="plop('btn')">plop</button-->
            <button id="start" class="button" onclick="parseF()">
                <svg class="ico" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <path fill="#546e7a" d="M8 5l12 7-12 7z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
                  <path fill="#303f46" fill-rule="evenodd" d="M7 4l14 8-14 8zm1 2v12l4-6z"/>
                </svg>
            </button>
            <button id="XoT" class="button" onclick="XoT()">
                <svg class="ico" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <path style="isolation:auto;mix-blend-mode:normal" fill="#546e7a" d="M5 4v1h13v7h1V4H5zm0 7v9h12v-1H6v-8H5z" color="#000" overflow="visible"/>
                  <path style="isolation:auto;mix-blend-mode:normal" class="b-red" fill="#303f46" d="M18.5 13l-.7.7L20 16H15v1h5.1l-2.3 2.3.7.8 2.8-2.9.7-.7-3.5-3.5z" color="#000" overflow="visible"/>
                  <path style="isolation:auto;mix-blend-mode:normal" fill="#546e7a" d="M10 7v1h5V7h-5zm0 2v1h3V9h-3zm-2 2v1h8v-1H8zm0 2v1h4v-1H8zm0 2v1h5v-1H8z" color="#000" overflow="visible"/>
                  <path style="isolation:auto;mix-blend-mode:normal" class="b-red" fill="#303f46" d="M9 10V6H3v4zM5 8L4 9V7h4v1z" color="#000" overflow="visible"/>
                </svg>
            </button>
            <div class="sep"></div>"""
HTML_code += '<h1 class="big">{0} Items</h1>'.format(FCNT)
HTML_code += """<div class="left" style="
">
<button class="button" onclick="menu()">
    <svg class="ico" id="bham" viewBox="0 0 24 24"><path id="mon" fill="#303f46" d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z">
			   </svg>
    </button>
    </div>

</div>
        <div class="list">
            <ul class="files" id="fls">"""
HTML_code += '<li class="fhead"><div class="tb-e tb1"><span>Convert</span></div><div class="tb-e"><span>Name</span></div></li>'
for g in gl:
    HTML_code += '<li class="file animated"><div class="tb-e tb1"><input class="checkb" type="checkbox" name="pdfs" value="{0}" onclick="addFile(\'{0}\')"></div><div class="tb-e"><span>{1}<br></span></div></li>'.format(g, ''.join(g.split('/')[-1:]))

HTML_code += """</ul>
        </div>
    </div>
    <div class="settings">
        <div class="pane p0">
            <ul class="panels-menu">
                <li class="lCore selected"><a class="icon ico-c" onclick="setPane('Core');">Core</a></li>
                <li class="lAbout"><a class="icon ico-a" onclick="setPane('About');">About</a></li>
            </ul>
        </div>
        <div class="pane p1">
            <div class="panels-content active" id="Core">
                <h2 class="pane-title">Core Settings</h2>
                <div class="pane-block">
                    <span>Change core comportement</span>
                </div>
            </div>
            <div class="panels-content" id="About">
                <h2 class="pane-title">About</h2>
                <div class="pane-block">
                    <span>TODO: About</span>
                </div>
            </div>
        </div>

        <button class="button fixed" onclick="menu()">
        <svg class="ico" id="bham" viewBox="0 0 24 24"><path id="mon" fill="#303f46" <path d="M6.3 5L5 6.2l5.7 5.7-5.7 5.7L6.3 19l5.7-5.7 5.7 5.7 1.4-1.4-5.7-5.7 5.7-5.7L17.7 5 12 10.6 6.3 4.9z"/>>
    			   </path></svg>
        </button>
    </div>
    <div id="console"></div>
</body>
</html>
"""

def main():
    check_versions()
    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    browser = cef.CreateBrowserSync(url=html_to_data_uri(HTML_code),
                                    window_title=APP_NAME)
    #browser.SetIcon("./res/pdf.ico")
    set_client_handlers(browser)
    set_javascript_bindings(browser)
    cef.MessageLoop()
    cef.Shutdown()

def html_to_data_uri(html, js_callback=None):
    # This function is called in two ways:
    # 1. From Python: in this case value is returned
    # 2. From Javascript: in this case value cannot be returned because
    #    inter-process messaging is asynchronous, so must return value
    #    by calling js_callback.
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    if js_callback:
        #js_print(js_callback.GetFrame().GetBrowser(),
        #         "Python", "html_to_data_uri",
        #         "Called from Javascript. Will call Javascript callback now.")
        #js_callback.Call(ret)
        pass
    else:
        return ret

def set_javascript_bindings(browser):
    external = External(browser)
    bindings = cef.JavascriptBindings(
            bindToFrames=False, bindToPopups=False)
    bindings.SetProperty("python_property", "This property was set in Python")
    bindings.SetProperty("cefpython_version", cef.GetVersion())
    bindings.SetFunction("html_to_data_uri", html_to_data_uri)
    bindings.SetFunction("lol", lol)
    bindings.SetFunction("add_file", add_file)
    bindings.SetFunction("parse", _parse)
    bindings.SetObject("external", external)
    browser.SetJavascriptBindings(bindings)

def add_file(f):
    if f not in files:
        files.append(f)
    else:
        files.remove(f)

def _parse(js_callback=None, xml=True):
    outF = ""
    if js_callback:
        html = '<li class="fhead"><div class="tb-e tb1"><span>Status</span></div><div class="tb-e"><span>Name</span></div></li>'
        browser = js_callback.GetFrame().GetBrowser()
        fls_set(browser, html)
        for g in files:
            q = queue.Queue()
            if xml:
                t = threading.Thread(target=parser.fromTexttoXML, args=['{}'.format(g), q])
            else:
                t = threading.Thread(target=parser.fromTexttoTXT, args=['{}'.format(g), q])
            t.start()
            outF = q.get()
            html = '<li class="file animated"><div class="tb-e tb1"><span>OK</span></div><div class="tb-e"><span>{}</span></div></li>'.format(''.join(outF.split('/')[-1:]))
            # js_print(js_callback.GetFrame().GetBrowser(),
            #          "Parser", "file_load",
            #          "> {}".format(g))
            args = [browser, html]
            threading.Timer(0.5, fls_add, args).start()

def lol(str, js_callback=None):
    subprocess.Popen("gnome-terminal")
    print(str)

def fls_add(browser, html):
    browser.ExecuteFunction("flsAdd", html);

def fls_set(browser, html):
    browser.ExecuteFunction("flsSet", html);

def js_print(browser, lang, event, msg):
    # Execute Javascript function "js_print"
    browser.ExecuteFunction("js_print", lang, event, msg)


def set_client_handlers(browser):
    # client_handlers = [LoadHandler(), DisplayHandler()]
    # for handler in client_handlers:
    #     browser.SetClientHandler(handler)
    pass

def check_versions():
    ver = cef.GetVersion()

class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        if not is_loading:
            # Loading is complete. DOM is ready.
            # js_print(browser, "Python", "OnLoadingStateChange",
            #          "Loading is complete")
            pass

class External(object):
    def __init__(self, browser):
        self.browser = browser

    def test_multiple_callbacks(self, js_callback):
        """Test both javascript and python callbacks."""
        # js_print(self.browser, "Python", "test_multiple_callbacks",
        #          "Called from Javascript. Will call Javascript callback now.")
        pass

        def py_callback(msg_from_js):
            js_print(self.browser, "Python", "py_callback", msg_from_js)
        js_callback.Call("String sent from Python", py_callback)

if __name__ == '__main__':
    main()
