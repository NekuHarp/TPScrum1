from cefpython3 import cefpython as cef
import base64
import platform
import sys
import threading
import subprocess
import glob
import time
import queue
import re

from Abstract import Parser

wd='./dossier/'
outF = 'outF'

parser = Parser(wd, outF)
# parser.fromTexttoXML('./dossier/Lin_2004_Rouge.txt')
# parser.fromTexttoTXT('./dossier/Lin_2004_Rouge.txt')
# parser.fromPDFtoXML('./dossier/Lin_2004_Rouge.pdf')
# parser.fromPDFtoTXT('./dossier/Lin_2004_Rouge.pdf')

APP_NAME = 'PDF Parser 1.1'
VERSION = '1.0.1 d'

TEAM = ['GRANIER Jean-Clair', 'BOUCHET Lucas', 'BARRIOL Rémy', 'WATTIN Tristan', 'MALEPLATE Bastien']

gl = parser.listDir()

files = []

FCNT = len(gl)

KBINDS = {',': 'Settings', 'Enter': 'Save/Start', 'Esc': 'Exit Settings', 'x': 'Toggle XML mode', 'r': 'Refresh', 's': 'Select all files / > Structures', 'c': '> Core', 'k': '> Keybind', 'a': '> About'}


ico_pdf = """<svg class="ico" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="#f3f3f2" d="M4 3v18h12l4-4V3z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
  <path fill="#f3f3f2" d="M2 5h8v6H2z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
  <path fill="#f3f3f2" d="M3 6h6v3H3z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
  <g fill="#bb2429">
    <path fill="#a4b1b6" d="M5 4v1h13v10h-4v4H6v-8H5v9h10l4-4V4z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
  </g>
  <path fill="#92999c" d="M10 7v1h5V7h-5zm0 2v1h3V9h-3zm-2 2v1h8v-1H8zm0 2v1h4v-1H8zm0 2v1h5v-1H8z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
  <path fill="#c94f53" d="M9 10V6H3v4zM5 8L4 9V7h4v1z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
</svg>
"""

HTML_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
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
    .list { margin: 8px; background: #1E1E21; color: #eee; margin-top: 0;
    flex-grow: 1; overflow: visible; overflow-x: hidden; overflow-y: auto;}
    .files { padding: 0; margin: 0; padding-bottom: 8px;}
    .status { margin: 8px 16px; }
    .ico { width: 24px; height:  24px; }
    li.fhead { background:  #2F2F34; display:  flex; }
    .tb-e { padding:  8px 0; min-width: 7em; overflow: hidden; text-overflow:
    ellipsis;}
    .tb-g { width: 100%;}
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
    .tb-e.tb1 input { padding: 0; margin: 0; margin-left: 4px; }
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
    transition: .2s all ease-in-out; display: none;}
    .settings.visible {z-index: 1; animation: pop 0.3s 0s ease-in-out 1 forwards; display: flex;}
    .button.fixed { width:  40px; height:  40px; right: 4px; top: 4px; position:
    absolute; z-index: 99;}
    .settings .pane { -webkit-box-flex: 1; -webkit-box-pack: end; display:
    -webkit-box; display: -ms-flexbox; display: flex; justify-content: flex-end;
    z-index: 1;}
    .panels-menu li:hover { cursor:  pointer; background: rgba(243, 243, 242,
    .1); transition:  .2s all ease-in-out; }
    .panels-menu li { transition: .2s all ease-in-out; border-left:  0px; margin: 0 1rem; border-radius: .3rem;}
    .p0 { flex: 1 0 218px; background: #2F2F34; color: rgba(255,255,255,.8);
    font-size: 1.12em;}
    .p1 { flex: 1 1 800px; }
    ul.panels-menu { margin-bottom: 0; padding-left: 0; list-style: none;
    position: relative; min-width: 15em; max-width: 20em; margin-top: 3em;}
    .panels-content { padding: 0px 40px; width: 100%; color:
    #5E6063; display: none; margin-right: 54px;}
    .panels-content.active { display: block; overflow-x: auto;}
    .pane-title { font-size: 1.75em; font-weight: bold; line-height:  1;
    margin-bottom: .75em; margin-top: 2.5em; color: #2F2F34; }

    #console { max-height: 8rem; overflow-wrap: normal; overflow-y: auto; padding: 0 8px;}
    .msg:before { content:  ''; width:  8px; background: rgba(105, 127, 138,
    .3); display: inline-block; height: 8px; margin-right: 8px; border-radius:
    8px; }

    .checkb { vertical-align: middle; -webkit-appearance: none; display:
    inline-block; position: relative; width: 16px; height: 16px; font-size: inherit;
    border-radius: 3px; background-color: #c2c5c9; transition: background-color
    0.16s cubic-bezier(0.5, 0.15, 0.2, 1); margin: 4px 0 0; margin-top: 1px \9;
    line-height: normal; }
    input[type="checkbox"]:active, input[type="checkbox"]:checked {
    background-color: #303f46; } input[type="checkbox"]:after { width: 10.56px;
    margin: -1px; transform: translate3d(0, 0, 0) rotate(-45deg) scale(0);
    transition-delay: .05s; } input[type="checkbox"]:before { width: 5.28px;
    transform: translate3d(0, 0, 0) rotate(225deg) scale(0); }
    input[type="checkbox"]:before, input[type="checkbox"]:after { content: "";
    position: absolute; top: 12px; left: 6.4px; height: 2px; border-radius: 1px;
    background-color: #e8eaed; transform-origin: 0 0; opacity: 0; transition:
    transform 0.1s cubic-bezier(0.5, 0.15, 0.2, 1), opacity 0.1s cubic-bezier(0.5,
    0.15, 0.2, 1); }
    input[type="checkbox"]:checked:after { opacity: 1; transform: translate3d(0, 0,
    0) rotate(-45deg) scale(1); transition-delay: 0; }
    input[type="checkbox"]:checked:before { opacity: 1; transform: translate3d(0, 0,
    0) rotate(225deg) scale(1); transition-delay: .05s; }
    input[type="checkbox"]:before, input[type="checkbox"]:after { background-color:
    #fff; }
    input[type="checkbox"]:active, input[type="checkbox"]:focus { outline:  none; }

    h4.small-title { margin-bottom: .25rem; font-size: 1.2em; }
    span.muted { opacity:  .8; display: block;}
    input.input-text { border: none; background-color: rgba(0,0,0,.1); border-color:
    rgba(0,0,0,.3); height: 32px; padding: 10px; -webkit-box-sizing: border-box;
    -webkit-transition: background-color .15s ease,border .15s ease; border-radius:
    3px; border-style: solid; border-width: 1px; box-sizing: border-box; width:
    100%; line-height:  32px; color: #222; margin-top:  .75em; transition:  .2s all
    ease-in-out; }
    input.input-text:focus { outline:  none; box-shadow: 0 0 0 2px rgba(0,0,0,.2); }

    .btn { height: initial; padding: 0 0.8em; font-size: 1em; line-height: 2em;
    display: inline-block; margin-bottom: 0; font-weight: normal; text-align:
    center; vertical-align: middle; border: none; border-radius: 3px;
    background-color: #f3f4f6; white-space: nowrap; cursor: pointer; z-index: 0;
    -webkit-user-select: none; width: 7em;}
    .pane-block.fixed { position:  absolute; right:  3em; bottom:  3em; }
    .btn-save { font-size:  1.2em; padding: .2em .5em; }
    .btn-cancel { font-size:  1.2em; padding: .2em .5em; }
    .btn:active, .btn:focus { box-shadow: inset 0 0 0 1px #697F8A, 0 0 0 2px
    rgba(0,0,0,.2); }

    .khead { border-bottom: 2px solid rgba(0,0,0,0.1); display: flex;
    font-weight: bold; }
    .keys { padding: 0; margin: 0; padding-bottom: 8px; }
    li.key { padding-left: 8px; display: flex; border-bottom: 1px solid rgba(0,0,0,0.1);}
    li.key:last-child { border: none; }

    span.about-title { font-size: 3rem; font-weight: 600; line-height: 4rem;
    margin-bottom: .75em; color: #2F2F34; display: flex;
    text-align:  center; margin:  0 auto; margin-left:  auto; width:
    fit-content; eight: 4rem; transition: .2s all ease-in-out; transform:
    scale3d(1, 1, 1); margin-top: 1.5em;}
    .about-title .ico { width: 4rem; height: 4rem; }
    span.about-version { text-align: center; width: 100%; margin:  0 auto;
    margin-bottom: .25rem; font-size: 1.6rem; font-weight: 200; display: flex;
    flex-grow:  1; flex-direction: column-reverse; }
    span.about-title:hover { transform: scale3d(1.1, 1.1, 1.1); transition:  .2s
    all ease-in-out; text-shadow: 2px 2px 0px #F3F3F2, 4px 4px 2px rgba(164,
    177, 182, 0.6); }

    ::-webkit-scrollbar { height: 14px; width: 14px; border-color: #F3F3F2; }
    ::-webkit-scrollbar-thumb { background-clip: padding-box; border-radius: 7px;
    border-color: #F3F3F2; background-color: rgba(66, 66, 66, 0.8); border-style:
    solid; border-width: 3px; } ::-webkit-scrollbar-track { background-clip:
    padding-box; border-radius: 8px; border-color: #F3F3F2; background-color:
    rgba(66, 66, 66, .12); border-style: solid; border-width: 2px; }
    ::-webkit-scrollbar-track { border-width: initial }
    ::-webkit-scrollbar-corner { background-color: transparent }

    .markup { font-size: 0.9375rem; word-wrap: break-word; margin: 0; padding: 0; }
    pre { background: rgba(47, 47, 52, .9); display: flex; }
    .markup pre { border-radius: 5px; box-sizing: border-box; font-family:
    Consolas,Liberation Mono,Menlo,Courier,monospace; max-width: 90%; white-space:
    pre-wrap; line-height: 1.3; user-select: text; padding:  .5rem; }
    code { margin:  0; padding:  0; display: flex; }
    .tag .name {color: #e06c75;}
    .xml { color: #abb2bf; flex-direction: column;}
    .text { color: #abb2bf; flex-direction: column;}
    .sub { padding-left: 1em; }

    .panels-menu li a { padding: 0.75em 1.5em; transition: .2s all ease-in-out;
    display: block; margin-bottom: .5em;}
    .panels-menu li.selected{ border-left:  4px solid; border-color: #F3F3F2;
    background: rgba(0,0,0,0.2); border-radius: .3rem; margin: 0 1rem;}
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
    var timeout;
    var T = true;

    document.onkeydown = checkKey;

    function stageAll() {
        var inp = document.getElementsByClassName("checkb");
        for (var i = 0; i < inp.length; i++)
            if (inp[i].type == "checkbox") {
                if(! inp[i].checked) {
                    inp[i].checked = true;
                    addFile(inp[i].value);
                }
            }
    }

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

    function setCount(cnt) {
        document.querySelector("#fcount").innerHTML = cnt+' Items';
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
        console = document.getElementById("console");
        console.innerHTML += "<div class=msg>"+msg+"</div>";
        //lol(msg);
    }

    function log(msg) {
        console = document.getElementById("console");
        console.innerHTML += "<div class=msg>"+msg+"</div>";
    }

    function addFile(f) {
        //console = document.getElementById("console");
        //console.innerHTML += "<div class=msg>"+f+"</div>";
        switch_file(f);
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
            log('Please select at least one file.');
        }
    }

    function resetT() {
        T = true;
    }

    function checkKey(e) {
        e = e || window.event;
        if(document.activeElement.tagName == "INPUT") {
            if (e.keyCode == '27') {
                document.activeElement.blur();
            }
        } else if (document.activeElement.tagName == "BODY") {
            if (e.keyCode == '38') {
                // up arrow
            }
            else if (e.keyCode == '83') {
                // s
                if(T) {
                    if(! document.querySelector(".settings").classList.contains("visible")) {
                        stageAll();
                        T = false;
                        timeout = setTimeout(resetT, 750);
                    } else {
                        setPane('Struc');
                        T = false;
                        timeout = setTimeout(resetT, 300);
                    }
                }

            }
            else if (e.keyCode == '82') {
                // r
                if(T) {
                    if(! document.querySelector(".settings").classList.contains("visible")) {
                        refresh(js_callback_1);
                        enable();
                        T = false;
                        timeout = setTimeout(resetT, 750);
                    }
                }
            }
            else if (e.keyCode == '88') {
                // x
                if(T) {
                    if(! document.querySelector(".settings").classList.contains("visible")) {
                        if(! document.getElementById("XoT").disabled) XoT();
                        T = false;
                        timeout = setTimeout(resetT, 750);
                    }
                }
            }
            else if (e.keyCode == '13') {
                if(T) {
                    if(document.querySelector(".settings").classList.contains("visible")) {
                        save();
                    } else {
                        parseF();
                    }
                    T = false;
                    timeout = setTimeout(resetT, 750);
                }
                // Enter
            }
            else if (e.keyCode == '32') {
                // Space
            }
            else if (e.keyCode == '67') {
                // c
                if(T) {
                    if(document.querySelector(".settings").classList.contains("visible")) {
                        setPane('Core');
                        T = false;
                        timeout = setTimeout(resetT, 300);
                    }
                }
            }
            else if (e.keyCode == '75') {
                // k
                if(T) {
                    if(document.querySelector(".settings").classList.contains("visible")) {
                        setPane('Keys');
                        T = false;
                        timeout = setTimeout(resetT, 300);
                    }
                }
            }
            else if (e.keyCode == '65') {
                // a
                if(T) {
                    if(document.querySelector(".settings").classList.contains("visible")) {
                        setPane('About');
                        T = false;
                        timeout = setTimeout(resetT, 300);
                    }
                }
            }
            else if (e.keyCode == '84') {
                // t
            }
            else if (e.keyCode == '27') {
                if(document.querySelector(".settings").classList.contains("visible")) {
                    menu();
                }
                // Esc
            }
            else if (e.keyCode == '188') {
                if(T) {
                    menu();
                    T = false;
                    timeout = setTimeout(resetT, 750)
                }
                // ,
            }
            else if (e.keyCode == '191') {
                // /
            }

        }
    }

    function enable() {
        document.querySelector("input[name='path']").blur();
        document.querySelector("input[name='out']").blur();
        document.getElementById("add").disabled = false;
        document.getElementById("start").disabled = false;
        document.getElementById("XoT").disabled = false;
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
HTML_code += '<h1 class="big" id="fcount">{0} Items</h1>'.format(FCNT)
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
HTML_code += '<li class="fhead"><div class="tb-e tb1"><span>Convert</span></div><div class="tb-e"><span>Author</span></div><div class="tb-e"><span>Year</span></div><div class="tb-e tb-g"><span>File</span></div></li>'
for g in gl:
    f = ''.join(g.split('/')[-1:])
    if('_' in f):
        _f = f.split('_')
        f0 = _f[0] if len(_f)>0 else ''
        f1 = _f[1] if len(_f)>1 else ''
        f2 = _f[2] if len(_f)>2 else ''
    else:
        if('-' in f):
            _f = f.split('-')
            f0 = _f[0] if len(_f)>0 else ''
        else:
            f0 = '?'
        m_year = re.match(r'.*([1-3][0-9]{3})', f)
        f1 = m_year.group(1)
        if f1 == '': f1 = '?'
    HTML_code += """<li class="file animated"><div class="tb-e tb1"><input class="checkb" type="checkbox" name="pdfs" value="{0}" onclick="addFile('{0}')"></div>
    <div class="tb-e"><span>{2}</span></div>
    <div class="tb-e"><span>{3}</span></div>
    <div class="tb-e tb-g"><span>{1}</span></div>
    </li>""".format(g, f, f0, f1, f2)

HTML_code += """</ul>
        </div>
        <div id="console"></div>
    </div>
    <div class="settings">
        <div class="pane p0">
            <ul class="panels-menu">
                <li class="lCore selected"><a class="icon ico-c" onclick="setPane('Core');">Core</a></li>
                <li class="lKeys"><a class="icon ico-k" onclick="setPane('Keys');">Keybind</a></li>
                <li class="lStruc"><a class="icon ico-s" onclick="setPane('Struc');">Structures</a></li>
                <li class="lAbout"><a class="icon ico-a" onclick="setPane('About');">About</a></li>
            </ul>
        </div>
        <div class="pane p1">
            <div class="panels-content active" id="Core">
                <script>
                var _path = '{0}';
                var _out = '{1}';""".format(wd, outF)
HTML_code += """
    function reset() {
        document.querySelector("input[name='path']").value = _path;
        document.querySelector("input[name='out']").value = _out;
        refresh(js_callback_1);
    }

    function save() {
        var p = document.querySelector("input[name='path']").value;
        var o = document.querySelector("input[name='out']").value;
        if(p != _path) {
            if(o != _out) {
                set(js_callback_1, p, o);
                setTimeout(menu, 750);
                _out = o;
            } else {
                set(js_callback_1, p, '');
                setTimeout(menu, 750);
            }
            _path = p;
            refresh(js_callback_1);
            enable();
        } else {
            if(o != _out) {
                set(js_callback_1, '', o);
                setTimeout(menu, 750);
                _out = o;
                refresh(js_callback_1);
                enable();
            } else {
                //pass
            }
        }
    }

"""

HTML_code += """</script>
                <h2 class="pane-title">Core Settings</h2>
                <div class="pane-block">
                    <span>Change core comportement</span>
                </div>
                <div class="pane-block">
                    <h4 class="small-title">Search path</h4>
                    <span class="muted">Folder where source file are</span>
                    <input class="input-text" name="path" type="text" placeholder="path" maxlength="256" value="{0}">
                </div>
                <div class="pane-block">
                    <h4 class="small-title">Output folder</h4>
                    <span class="muted">Folder where files will output</span>
                    <input class="input-text" name="out" type="text" placeholder="path" maxlength="256" value="{1}">
                </div>
                <div class="pane-block fixed">
                    <button class="button btn btn-cancel" onClick="reset();">Cancel</button>
                    <button class="button btn btn-save" onClick="save();">Save</button>
                </div>
            </div>
            <div class="panels-content" id="Keys">
                <h2 class="pane-title">Keybind</h2>
                <div class="pane-block">
                    <ul class="keys"><li class="khead"><div class="tb-e"><span>Key</span></div><div class="tb-e tb-g"><span>Action</span></div></li>""".format(wd, outF)
for i in KBINDS:
    HTML_code += """<li class="key">
                            <div class="tb-e"><span>{0}</span></div>
                            <div class="tb-e tb-g"><span>{1}</span></div>
                        </li>""".format(i, KBINDS[i])
DO_TAGS = parser.getDoTags()
XML_TAGS = parser.getXMLTags()
TXT_TAGS = parser.getTXTTags()
HTML_code += """</ul>
                </div>
            </div>
            <div class="panels-content" id="Struc">
                <h2 class="pane-title">Structures</h2>
                <div class="pane-block">
                    <span>Pre-defined output</span>
                </div>
                <div class="pane-block">
                    <div class="markup">
                        <pre>
                            <code class="xml">
                                <span class="tag">&lt;<span class="name">article</span>&gt;</span>
                            """
for tag in DO_TAGS:
    if tag in XML_TAGS and DO_TAGS[tag]:
        HTML_code += """ <span class="tag sub">&lt;<span class="name">{0}</span>&gt; the {0} &lt;/<span class="name">{0}</span>&gt;</span>
                                """.format(XML_TAGS[tag])
HTML_code += """                <span class="tag">&lt;/<span class="name">article</span>&gt;</span>
                            </code>
                        </pre>
                    </div>
                </div>
                <div class="pane-block">
                    <div class="markup">
                        <pre>
                            <code class="text">
                            """
for tag in DO_TAGS:
    if tag in TXT_TAGS and DO_TAGS[tag]:
        if(tag != '_HEADER'):
            HTML_code += """ <span class="tag"><span class="name">{0}</span></span>
                            <span class="tag"> the {1} </span>""".format(TXT_TAGS[tag], tag[1:].lower())
        else:
            HTML_code += """ <span class="tag"><span class="name">{0}</span></span>""".format(TXT_TAGS[tag].strip())
HTML_code += """            </code>
                        </pre>
                    </div>
                </div>
            </div>"""
HTML_code += """
            <div class="panels-content" id="About">
                <span class="about-title">
                    <svg class="ico" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                      <path fill="#f3f3f2" d="M4 3v18h12l4-4V3z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
                      <path fill="#f3f3f2" d="M2 5h8v6H2z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
                      <path fill="#f3f3f2" d="M3 6h6v3H3z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
                      <g fill="#bb2429">
                        <path fill="#a4b1b6" d="M5 4v1h13v10h-4v4H6v-8H5v9h10l4-4V4z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
                      </g>
                      <path fill="#92999c" d="M10 7v1h5V7h-5zm0 2v1h3V9h-3zm-2 2v1h8v-1H8zm0 2v1h4v-1H8zm0 2v1h5v-1H8z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
                      <path fill="#c94f53" d="M9 10V6H3v4zM5 8L4 9V7h4v1z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
                    </svg>
                PDF Parser</span>

                <div class="pane-block">
                    <span class="about-version">{}</span>
                </div>
                <div class="pane-block">
                    <h4 class="small-title">Used libraries</h4>
                    <span class="muted">Python {}</span>
                    <span class="muted">Chrome {}</span>
                    <span class="muted">CEF {}</span>
                </div>
                <div class="pane-block">
                    <h4 class="small-title">Team</h4>""".format(VERSION,'.'.join(['{}'.format(i) for i in sys.version_info]), cef.GetVersion()['chrome_version'], cef.GetVersion()['cef_version'])

for i in TEAM:
    HTML_code +=  """<span class="muted">{}</span>""".format(i)
                    #<span class="muted">{}</span>
HTML_code += """</div>
            </div>
        </div>

        <button class="button fixed" onclick="menu()">
        <svg class="ico" id="bham" viewBox="0 0 24 24"><path id="mon" fill="#303f46" <path d="M6.3 5L5 6.2l5.7 5.7-5.7 5.7L6.3 19l5.7-5.7 5.7 5.7 1.4-1.4-5.7-5.7 5.7-5.7L17.7 5 12 10.6 6.3 4.9z"/>>
    			   </path></svg>
        </button>
    </div>
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

def setWD(wd=False):
    if wd != False:
        files.clear()
        return parser.setWD(wd)
    else:
        return False

def setOut(outf=False):
    if outf != False:
        return parser.setOut(outf)
    else:
        return False

def set(js_callback=None, wd='', outf=''):
    #if js_callback:
    #    js_print(browser, "Python", "set", "{} {}".format(wd, outf))
    if wd != '':
        if not setWD(wd):
            if js_callback:
                browser = js_callback.GetFrame().GetBrowser()
                js_print(browser, "Python", "set", "Invalid path : {}".format(wd))
        else:
            if js_callback:
                _refresh(js_callback)
    if outf != '':
        if not setOut(outf):
            if js_callback:
                browser = js_callback.GetFrame().GetBrowser()
                js_print(browser, "Python", "set", "Out folder invalid ({}).".format(outf))

def _refresh(js_callback=None):
    gl = parser.listDir()
    FCNT = len(gl)

    clear_files()

    if js_callback:
        browser = js_callback.GetFrame().GetBrowser()
        file_count(browser, FCNT)
        html = '<li class="fhead"><div class="tb-e tb1"><span>Convert</span></div><div class="tb-e"><span>Author</span></div><div class="tb-e"><span>Year</span></div><div class="tb-e tb-g"><span>File</span></div></li>'
        fls_set(browser, html)
        for g in gl:
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

            if g in files:
                html = """<li class="file animated"><div class="tb-e tb1"><input class="checkb" type="checkbox" name="pdfs" value="{0}" onclick="addFile('{0}')" checked></div>
                <div class="tb-e"><span>{2}</span></div>
                <div class="tb-e"><span>{3}</span></div>
                <div class="tb-e tb-g"><span>{1}</span></div>
                </li>""".format(g, f, f0, f1, f2)
            else:
                html = """<li class="file animated"><div class="tb-e tb1"><input class="checkb" type="checkbox" name="pdfs" value="{0}" onclick="addFile('{0}')"></div>
                <div class="tb-e"><span>{2}</span></div>
                <div class="tb-e"><span>{3}</span></div>
                <div class="tb-e tb-g"><span>{1}</span></div>
                </li>""".format(g, f, f0, f1, f2)
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
            except:
                continue
            html = '<li class="file animated"><div class="tb-e tb1">{}</div><div class="tb-e"><span>{}</span></div></li>'.format(ico_pdf, ''.join(outF.split('/')[-1:]))
            # js_print(js_callback.GetFrame().GetBrowser(),
            #          "Parser", "file_load",
            #          "> {}".format(g))
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
