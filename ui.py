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

HTML_code = """
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
    .window { background: #F3F3F2; }
    body { margin: 0; }
    .toolbar{ display: -webkit-flex; display: -ms-flexbox; display: flex;
    -webkit-flex-wrap: nowrap; -ms-flex-wrap: nowrap; flex-wrap: nowrap;
    box-sizing: border-box;}
    .button { color: #424242; text-decoration: none; margin: 0; font-size: 14px;
    font-weight: 400; line-height: 24px; letter-spacing: 0; opacity: .87;
    line-height: 64px; padding: 0 24px; transition: .2s all ease-in-out; }
    .button span { display: block; text-align: center; }
    .button:hover { background: #aaa; cursor: pointer; transition: .2s all
    ease-in-out; }
    .list { margin: 8px; background: #1E1E21; color: #eee; }
    .files { padding: 8px 0; }
    .status { margin: 8px 16px; }
    li.file { padding-left: 8px; padding: 8px; }
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
            <button class="button" onclick="lol('btn')">Add files</button>
            <button class="button" onclick="plop('btn')">plop</button>
            <button class="button" onclick="parseF()">Parse !</button>
        </div>
        <div class="list">
            <ul class="files" id="fls">"""
for g in gl:
    HTML_code += '<li class="file"><input type="checkbox" name="pdfs" value="{0}" onclick="addFile(\'{0}\')"> {1}<br></li>'.format(g, ''.join(g.split('/')[-1:]))

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
        html = ""
        browser = js_callback.GetFrame().GetBrowser()
        fls_set(browser, html)
        for g in files:
            q = queue.Queue()
            t = threading.Thread(target=parser.fromTexttoXML, args=['{}'.format(g), q])
            t.start()
            outF = q.get()
            html = "<li class='file'>{}</li>".format(''.join(outF.split('/')[-1:]))
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
