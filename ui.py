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

wd = "./dossier/"
gl = glob.glob('{}/*.{}'.format(wd, "pdf"))
gl = [g.replace('\\','/') for g in gl]

files = []

FCNT = len(gl)

HTML_code = """
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
    .window { background: #F3F3F2; }
    body { margin: 0; background: #F3F3F2;}
    .toolbar{ display: -webkit-flex; display: -ms-flexbox; display: flex;
    -webkit-flex-wrap: nowrap; -ms-flex-wrap: nowrap; flex-wrap: nowrap;
    box-sizing: border-box; padding-left: 8px; max-height: 80px; margin-bottom:
    0px;}
    .button { color: #424242; text-decoration: none; margin: 0; font-size: 14px;
    font-weight: 400; letter-spacing: 0; opacity: .87;
    line-height: 0px; padding: 0 24px; transition: .2s all ease-in-out;
    padding: 8px; max-height: 64px; overflow:  hidden;
    border:  0; border-radius: 32px; margin: 8px 4px; box-shadow: inset 0 0 0 1px #697F8A;
    background:  transparent; }
    .button span { display: block; text-align: center; }
    .button:focus {outline: none;}
    .button:hover { background: #aaa; cursor: pointer; transition: .2s all
    ease-in-out; box-shadow: inset 0 0 64px 32px rgba(105, 127, 138, .05); outline:none;}
    .list { margin: 8px; background: #1E1E21; color: #eee; margin-top: 0;}
    .files { padding: 0; margin: 0; padding-bottom: 8px;}
    .status { margin: 8px 16px; }
    .ico { width: 24px; height:  24px; }
    li.fhead { background:  #2F2F34; display:  flex; }
    .tb-e { padding:  8px 0; }
    .tb1 {width: 40px; overflow: hidden; text-overflow: ellipsis; padding-left:
    8px; }
    .sep { width: 1px; background: #5E6063; margin: 12px 8px; opacity: .8; }
    h1.big { line-height: 16px; font-weight: lighter; color: #5E6063; }
    li.file { padding-left: 8px; display: flex;}
    button:disabled:hover, button[disabled]:hover { box-shadow: inset 0 0 0 1px
    #697F8A; background: inherit; cursor: default; }
    button:disabled, button[disabled] { opacity:  .5; }
    body,html { font-family: Arial; font-size: 11pt; }
    div.msg { margin: 0.2em; line-height: 1.4em; }
    b { background: #ccc; font-weight: bold; font-size: 10pt;
        padding: 0.1em 0.2em; }
    b.Python { background: #eee; }
    i { font-family: Courier new; font-size: 10pt; border: #eee 1px solid;
        padding: 0.1em 0.2em; }
    </style>

    <script>
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

    function plop(msg) {
        console.innerHTML += "<div class=msg>"+msg+"</div>";
        lol(msg);
    }

    function addFile(f) {
        console.innerHTML += "<div class=msg>"+f+"</div>";
        add_file(f);
    }

    function parseF() {
        var elem = document.querySelector('#fls');
        elem.innerHTML = "<h4 class='status'>Working . . .</h4>";
        document.getElementById("add").disabled = true;
        document.getElementById("start").disabled = true;
        parse(js_callback_1);
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
            <div class="sep"></div>"""
HTML_code += '<h1 class="big">{0} Items</h1>'.format(FCNT)
HTML_code += """</div>
        <div class="list">
            <ul class="files" id="fls">"""
HTML_code += '<li class="fhead"><div class="tb-e tb1"><span>Convert</span></div><div class="tb-e"><span>Name</span></div></li>'
for g in gl:
    HTML_code += '<li class="file"><div class="tb-e tb1"><input type="checkbox" name="pdfs" value="{0}" onclick="addFile(\'{0}\')"></div><div class="tb-e"><span>{1}<br></span></div></li>'.format(g, ''.join(g.split('/')[-1:]))

HTML_code += """</ul>
        </div>
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

def list_files():
    for i in range(0,9):
        js_print(self.browser, "Python", "py_callback", "{}".format(i))

def add_file(f):
    if f not in files:
        files.append(f)
    else:
        files.remove(f)

def _parse(js_callback=None):
    outF = ""
    if js_callback:
        html = '<li class="fhead"><div class="tb-e tb1"><span>Status</span></div><div class="tb-e"><span>Name</span></div></li>'
        browser = js_callback.GetFrame().GetBrowser()
        fls_set(browser, html)
        for g in files:
            q = queue.Queue()
            t = threading.Thread(target=parser.fromTexttoXML, args=['{}'.format(g), q])
            t.start()
            outF = q.get()
            html = '<li class="file"><div class="tb-e tb1"><span>OK</span></div><div class="tb-e"><span>{}</span></div></li>'.format(''.join(outF.split('/')[-1:]))
            # js_print(js_callback.GetFrame().GetBrowser(),
            #          "Parser", "file_load",
            #          "> {}".format(g))
            args = [browser, html]
            threading.Timer(0.5, fls_add, args).start()

def lol(str, js_callback=None):
    subprocess.Popen("notepad.exe")
    print(str)

def fls_add(browser, html):
    browser.ExecuteFunction("flsAdd", html);

def fls_set(browser, html):
    browser.ExecuteFunction("flsSet", html);

def js_print(browser, lang, event, msg):
    # Execute Javascript function "js_print"
    browser.ExecuteFunction("js_print", lang, event, msg)

def set_global_handler():
    # A global handler is a special handler for callbacks that
    # must be set before Browser is created using
    # SetGlobalClientCallback() method.
    global_handler = GlobalHandler()
    cef.SetGlobalClientCallback("OnAfterCreated",
                                global_handler.OnAfterCreated)

def set_client_handlers(browser):
    client_handlers = [LoadHandler(), DisplayHandler()]
    for handler in client_handlers:
        browser.SetClientHandler(handler)

def check_versions():
    ver = cef.GetVersion()

class GlobalHandler(object):
    def OnAfterCreated(self, browser, **_):
        """Called after a new browser is created."""
        # js_print(browser, "Python", "OnAfterCreated",
        #          "This will probably never display as DOM is not yet loaded")
        # Delay print by 0.5 sec, because js_print is not available yet
        # args = [browser, "Python", "OnAfterCreated",
        #         "(Delayed) Browser id="+str(browser.GetIdentifier())]
        # threading.Timer(0.5, js_print, args).start()
        pass

class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        if not is_loading:
            # Loading is complete. DOM is ready.
            # js_print(browser, "Python", "OnLoadingStateChange",
            #          "Loading is complete")
            pass

class DisplayHandler(object):
    def OnConsoleMessage(self, browser, message, **_):
        """Called to display a console message."""
        # This will intercept js errors, see comments in OnAfterCreated
        if "error" in message.lower() or "uncaught" in message.lower():
            # Prevent infinite recurrence in case something went wrong
            if "js_print is not defined" in message.lower():
                if hasattr(self, "js_print_is_not_defined"):
                    print("Python: OnConsoleMessage: "
                          "Intercepted Javascript error: "+message)
                    return
                else:
                    self.js_print_is_not_defined = True
            # Delay print by 0.5 sec, because js_print may not be
            # available yet due to DOM not ready.
            args = [browser, "Python", "OnConsoleMessage",
                    "(Delayed) Intercepted Javascript error: <i>{error}</i>"
                    .format(error=message)]
            threading.Timer(0.5, js_print, args).start()

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
