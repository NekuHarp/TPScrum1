# -*- coding: utf-8 -*-

import os
import re
from cefpython3 import cefpython as cef
import base64
import platform
import sys
import threading
import subprocess
import re
import pickle

if sys.version_info[0] < 3:
    import Queue
else:
    import queue

from .Version import getFullVersion
from .Client import Client as _C
from .Parser import Parser as _P
from . import Defs as _D
from . import HTMLRes as _H

APP_NAME = _D.APP_NAME
_HTML = _H._HTML_code
_DEBUG = _H._DEBUG
TEAM = _H.TEAM
VERSION = getFullVersion()
KBINDS = _H.KBINDS
_MESSAGE = _H._MESSAGE
ico_pdf = _H.ico_pdf
ico_failed = _H.ico_failed
ico_splash = _H.ico_splash

parser = _P()
c = _C()

#parser.fromTexttoXML('./a/Lin_2004_Rouge.txt')
#parser.fromTexttoTXT('./a/Lin_2004_Rouge.txt')
#parser.fromPDFtoXML('./a/Lin_2004_Rouge.pdf')
#parser.fromPDFtoTXT('./a/Lin_2004_Rouge.pdf')

wd = parser.getWD()
outF = parser.getOutF()

gl = c.ls(wd)

files = []

FCNT = len(gl)

def html_to_data_uri(html, js_callback=None):
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    if js_callback:
        pass
    else:
        return ret

def js_print(browser, lang, event, msg):
    browser.ExecuteFunction("js_print", lang, event, msg)

def file_name(g):
    f = ''.join(g.split('/')[-1:])
    if('_' in f):
        _f = f.split('_')
        f0 = _f[0] if len(_f)>0 else ''
        try:
            m_year = re.match(r'.*([1-3][0-9]{3})', f)
            f1 = m_year.group(1)
        except:
            f1 = '?'
        f2 = _f[2] if len(_f)>2 else ''
    else:
        if('-' in f):
            _f = f.split('-')
            f0 = _f[0] if len(_f)>0 else ''
            f1 = _f[1] if len(_f)>1 else ''
            f2 = _f[2] if len(_f)>2 else ''
        else:
            f0 = '?'
        try:
            m_year = re.match(r'.*([1-2][0-9]{3})', f)
            f1 = m_year.group(1)
        except:
            f1 = '?'
        f2 = ''
    return [f, f0, f1, f2]

def _make_html(s=""):
    s = _HTML[0]
    s += _HTML[1].format(FCNT)
    s += _HTML[2]
    if len(gl)<1:
        s += _HTML[3].format(ico_splash, _MESSAGE[2])
    else:
        for g in gl:
            g_f = file_name(g)
            s += _HTML[4].format(g, g_f[0], g_f[1], g_f[2], g_f[3])
    s += _HTML[5].format(wd, outF)
    s += _HTML[6]
    s += _HTML[7].format(wd, outF)
    for i in KBINDS:
        s += _HTML[8].format(i, KBINDS[i])
    DO_TAGS = parser.conf.getDoTags()
    XML_TAGS = parser.conf.getXMLTags()
    TXT_TAGS = parser.conf.getTXTTags()
    s += _HTML[9]
    for tag in DO_TAGS:
        if tag in XML_TAGS and DO_TAGS[tag]:
            s += _HTML[10].format(XML_TAGS[tag])
    s += _HTML[11]
    for tag in DO_TAGS:
        if tag in TXT_TAGS and DO_TAGS[tag]:
            if(tag != '_HEADER'):
                s += _HTML[12].format(TXT_TAGS[tag], tag[1:].lower())
            else:
                s += _HTML[13].format(TXT_TAGS[tag].strip())
    s += _HTML[14]
    s += _HTML[15].format(VERSION,'.'.join(['{}'.format(i) for i in sys.version_info]), cef.GetVersion()['chrome_version'], pickle.format_version, cef.GetVersion()['cef_version'])
    for i in TEAM:
        s += _HTML[16].format(i)
    s += _HTML[17]
    return s

def check_versions():
    ver = cef.GetVersion()

def main():
    print("main")
    check_versions()
    parser.loadConfig()
    wd = parser.getWD()
    if(not _DEBUG): sys.excepthook = cef.ExceptHook
    settings = {
        "context_menu": {
            "enabled": _DEBUG,
            "navigation": False,
            "print": False,
            "view_source": False,
            "external_browser": False,
            "devtools": True,
        },
        # "product_version": "MyProduct/10.00",
        # "user_agent": "MyAgent/20.00 MyProduct/10.00",
    }
    cef.Initialize(settings=settings)
    browser = cef.CreateBrowserSync(url=html_to_data_uri(_make_html()),
                                    window_title=APP_NAME)
    set_client_handlers(browser)
    set_javascript_bindings(browser)

    cef.MessageLoop()
    cef.Shutdown()

def set_javascript_bindings(browser):
    external = External(browser)
    bindings = cef.JavascriptBindings(
            bindToFrames=False, bindToPopups=False)
    bindings.SetProperty("python_property", "This property was set in Python")
    bindings.SetProperty("cefpython_version", cef.GetVersion())
    bindings.SetFunction("html_to_data_uri", html_to_data_uri)
    bindings.SetFunction("lol", lol)
    bindings.SetFunction("add_file", add_file)
    bindings.SetFunction("switch_file", switch_file)
    bindings.SetFunction("remove_file", remove_file)
    bindings.SetFunction("parse", _parse)
    bindings.SetFunction("setWD", setWD)
    bindings.SetFunction("setOut", setOut)
    bindings.SetFunction("set", set)
    bindings.SetFunction("refresh", _refresh)
    bindings.SetObject("external", external)
    browser.SetJavascriptBindings(bindings)

def add_file(f):
    if f not in files:
        files.append(f)

def switch_file(f):
    if f not in files:
        files.append(f)
    else:
        files.remove(f)

def remove_file(f):
    if f in files:
        files.remove(f)

def clear_files():
    files.clear()

def setWD(w=False):
    if w != False:
        files.clear()
        r = parser.setWD(w)
        if r:wd = w
        return r
    else:
        return False

def setOut(outf=False):
    if outf != False:
        return parser.setOut(outf)
    else:
        return False

def set(js_callback=None, w='', outf=''):
    #if js_callback:
    #    js_print(browser, "Python", "set", "{} {}".format(wd, outf))
    if w != '':
        if not parser.setWD(w):
            if js_callback:
                browser = js_callback.GetFrame().GetBrowser()
                js_print(browser, "Python", "set", "Invalid path : {}".format(w))
        else:
            if js_callback:
                _refresh(js_callback)
    if outf != '':
        if not parser.setOut(outf):
            if js_callback:
                browser = js_callback.GetFrame().GetBrowser()
                js_print(browser, "Python", "set", "Out folder invalid ({}).".format(outf))


def _refresh(js_callback=None):
    wd = parser.getWD()
    gl = c.ls(wd)
    FCNT = len(gl)

    clear_files()

    parser.saveConfig()
    #parser.loadConfig()

    if js_callback:
        browser = js_callback.GetFrame().GetBrowser()
        file_count(browser, FCNT)
        html = '<li class="fhead"><div class="tb-e tb1"><span>Convert</span></div><div class="tb-e"><span>Author</span></div><div class="tb-e"><span>Year</span></div><div class="tb-e tb-g"><span>File</span></div></li>'
        fls_set(browser, html)
        if FCNT<1:
            html = """ <div class="splash">{}<span>{}</span></div> """.format(ico_splash, _MESSAGE[2])
            fls_add(browser, html)
        else:
            for g in gl:
                g_f = file_name(g)
                #TODO: PARSE

                if g in files:
                    html = """<li class="file animated"><div class="tb-e tb1"><input class="checkb" type="checkbox" name="pdfs" value="{0}" onclick="addFile('{0}')" checked></div>
                    <div class="tb-e"><span>{2}</span></div>
                    <div class="tb-e"><span>{3}</span></div>
                    <div class="tb-e tb-g"><span>{1}</span></div>
                    </li>""".format(g, g_f[0], g_f[1], g_f[2], g_f[3])
                else:
                    html = """<li class="file animated"><div class="tb-e tb1"><input class="checkb" type="checkbox" name="pdfs" value="{0}" onclick="addFile('{0}')"></div>
                    <div class="tb-e"><span>{2}</span></div>
                    <div class="tb-e"><span>{3}</span></div>
                    <div class="tb-e tb-g"><span>{1}</span></div>
                    </li>""".format(g, g_f[0], g_f[1], g_f[2], g_f[3])
                fls_add(browser, html)

def _parse(js_callback=None, xml=True):
    outF = ""

    if js_callback:
        html = '<li class="fhead"><div class="tb-e tb1"><span>Status</span></div><div class="tb-e"><span>Name</span></div></li>'
        browser = js_callback.GetFrame().GetBrowser()
        fls_set(browser, html)
        for g in files:
            q = queue.Queue()
            try:
                if xml:
                    t = threading.Thread(target=parser.fromTexttoXML, args=['{}'.format(g), q])
                else:
                    t = threading.Thread(target=parser.fromTexttoTXT, args=['{}'.format(g), q])
                t.start()
                outF = q.get()
                if(outF == ''):
                    html = '<li class="file animated"><div class="tb-e tb1">{}</div><div class="tb-e"><span>{}</span></div></li>'.format(ico_failed, ''.join(outF.split('/')[-1:]))
                else:
                    html = '<li class="file animated"><div class="tb-e tb1">{}</div><div class="tb-e"><span>{}</span></div></li>'.format(ico_pdf, ''.join(outF.split('/')[-1:]))
                # js_print(js_callback.GetFrame().GetBrowser(),
                #          "Parser", "file_load",
                #          "> {}".format(g))
            except:
                html = '<li class="file animated"><div class="tb-e tb1">{}</div><div class="tb-e"><span>{}</span></div></li>'.format(ico_failed, ''.join(outF.split('/')[-1:]))
            args = [browser, html]
            threading.Timer(0.5, fls_add, args).start()

def lol(str, js_callback=None):
    #subprocess.Popen("gnome-terminal")
    print(str)

def fls_add(browser, html):
    browser.ExecuteFunction("flsAdd", html);

def fls_set(browser, html):
    browser.ExecuteFunction("flsSet", html);

def file_count(browser, val):
    browser.ExecuteFunction("setCount", val);

def js_print(browser, lang, event, msg):
    browser.ExecuteFunction("js_print", lang, event, msg)

def set_client_handlers(browser):
    # client_handlers = [LoadHandler(), DisplayHandler()]
    # for handler in client_handlers:
    #     browser.SetClientHandler(handler)
    pass

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
