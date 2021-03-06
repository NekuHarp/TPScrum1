# -*- coding: utf-8 -*-

###############################################################################
# UI DEFS
###############################################################################

_DEBUG = True

TEAM = ['GRANIER Jean-Clair', 'BOUCHET Lucas', 'BARRIOL Rémy', 'WATTIN Tristan', 'MALEPLATE Bastien']

KBINDS = {',': 'Settings', 'Enter': 'Save/Start', 'Esc': 'Exit Settings', 'x': 'Toggle XML mode', 'r': 'Refresh', 's': 'Select all files / > Structures', 'c': '> Core', 'k': '> Keybind', 'a': '> About'}

_MESSAGE = ['','','No Files Found.']

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

ico_failed = """ <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="#f3f3f2" d="M8.3 3L3 8.3v7.4L8.3 21h7.4l5.3-5.3V8.3L15.7 3H8.3z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
  <path fill="#c94f53" d="M8.7 4L4 8.7v6.6L8.7 20h6.6l4.7-4.7V8.7L15.3 4H8.7zM9 5h5.8L19 9.1v5.8L14.9 19H9.1L5 14.9V9.1L9.1 5z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
  <path fill="#c94f53" d="M9.2 7.8L7.8 9.2l2.8 2.8-2.8 2.8 1.4 1.4 2.8-2.8 2.8 2.8 1.4-1.4-2.8-2.8 2.8-2.8-1.4-1.4-2.8 2.8-2.8-2.8z" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"/>
</svg> """

ico_splash = """<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="b">
      <stop offset="0" stop-color="#a4b1b6" stop-opacity=".3"></stop>
      <stop offset="1" stop-color="#a4b1b6" stop-opacity="0"></stop>
    </linearGradient>
    <linearGradient id="a">
      <stop offset="0" stop-color="#5a6b74"></stop>
      <stop offset="1" stop-color="#697f8a"></stop>
    </linearGradient>
    <linearGradient id="f" x1="49.6" x2="23.5" y1="63.6" y2="37.5" gradientTransform="translate(-1 18)" gradientUnits="userSpaceOnUse" xlink:href="#a"></linearGradient>
    <linearGradient id="g" x1="94" x2="38.1" y1="63" y2="7.1" gradientTransform="translate(0 3)" gradientUnits="userSpaceOnUse" xlink:href="#a"></linearGradient>
    <linearGradient id="e" x1="33" x2="16.7" y1="68" y2="51.7" gradientTransform="translate(-1 13)" gradientUnits="userSpaceOnUse" xlink:href="#a"></linearGradient>
    <linearGradient id="d" x1="85" x2="15" y1="85" y2="15" gradientUnits="userSpaceOnUse" xlink:href="#a"></linearGradient>
    <linearGradient id="h" x1="85" x2="15" y1="85" y2="15" gradientUnits="userSpaceOnUse" xlink:href="#a"></linearGradient>
    <linearGradient id="i" x1="65.5" x2="47.5" y1="70" y2="52" gradientUnits="userSpaceOnUse" xlink:href="#b"></linearGradient>
    <linearGradient id="c" x1="85" x2="15" y1="85" y2="15" gradientUnits="userSpaceOnUse" xlink:href="#a"></linearGradient>
  </defs>
  <path fill="url(#c)" d="M85 50a35 35 0 0 1-35 35 35 35 0 0 1-35-35 35 35 0 0 1 34.9-35A35 35 0 0 1 85 49.9" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path><g class="svg_t t_1" color="#000">
    <path fill="url(#e)" d="M32 69a12 12 0 0 1-12 12A12 12 0 0 1 8 69a12 12 0 0 1 12-12 12 12 0 0 1 12 12" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
    <path fill="url(#f)" d="M60 73a20 20 0 0 1-20 20 20 20 0 0 1-20-20 20 20 0 0 1 20-20 20 20 0 0 1 20 20" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
  </g>
  <path class="svg_t t_2" fill="url(#g)" d="M94 50a16 16 0 0 1-16 16 16 16 0 0 1-16-16 16 16 0 0 1 16-16 16 16 0 0 1 16 16" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
  <path class="svg_t t_3" fill="url(#h)" d="M58 19a12 12 0 0 1-12 12 12 12 0 0 1-12-12A12 12 0 0 1 45.8 7a12 12 0 0 1 12 11.9" color="#000" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
  <g fill="#f3f3f2" color="#000" class="svg_l t_1">
    <rect width="3" height="1" x="16" y="45" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="5" height="1" x="14" y="43" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="3" height="1" x="17" y="47" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="3" height="1" x="21" y="47" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="7" height="1" x="9" y="47" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="3" height="1" x="8" y="49" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="9" height="1" x="12" y="49" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="2" height="1" x="22" y="49" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="4" height="1" x="10" y="51" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="2" height="1" x="16" y="51" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
  </g>
  <g fill="#f3f3f2" color="#000" class="svg_l t_2">
    <rect width="7" height="1" x="65" y="20" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="2" height="1" x="73" y="20" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="7" height="1" x="62" y="22" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="4" height="1" x="70" y="22" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="3" height="1" x="64" y="24" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="4" height="1" x="68" y="24" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="2" height="1" x="73" y="24" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="6" height="1" x="69" y="26" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="2" height="1" x="66" y="26" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="8" height="1" x="57" y="26" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
  </g>
  <g color="#000">
    <path fill="#f3f3f2" d="M40 33a3 3 0 0 0-3 3v28a3 3 0 0 0 3 3h17a2 2 0 0 0 1.4-.6l8-8A2 2 0 0 0 67 57V36a3 3 0 0 0-3-3H40z" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
    <path fill="url(#i)" d="M40 34a2 2 0 0 0-2 2v28c0 1.1.9 2 2 2h17l9-9V36a2 2 0 0 0-2-2z" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
    <path fill="#fff" fill-opacity=".5" d="M51 34L38 47v2l15-15zM54 34L38 50v4l20-20zM60 35L38 57v7l2 2h1l25-25v-5l-1-1z" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
    <path fill="#a4b1b6" d="M40 34a2 2 0 0 0-2 2v28c0 1.1.9 2 2 2h17v-1H40a1 1 0 0 1-1-1V36c0-.6.4-1 1-1h24c.6 0 1 .4 1 1v21h1V36a2 2 0 0 0-2-2H40z" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
    <path fill="#a4b1b6" fill-opacity=".5" d="M58 56a2 2 0 0 0-2 2v6a2 2 0 0 0 1.2 1.8l8.6-8.6A2 2 0 0 0 64 56h-6z" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
    <path fill="#a4b1b6" d="M58 56a2 2 0 0 0-2 2v8h1a1 1 0 0 0 .7-.3l8-8a1 1 0 0 0 .3-.7v-1h-8zm0 1h7l-8 8v-7c0-.6.4-1 1-1z" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
    <rect width="10" height="1" x="48" y="40" fill="#92999c" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="6" height="1" x="48" y="44" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="16" height="1" x="44" y="48" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="8" height="1" x="44" y="52" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="10" height="1" x="44" y="56" fill="#92999c" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="14" height="10" x="33" y="37" fill="#f3f3f2" overflow="visible" ry="2" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="12" height="8" x="34" y="38" fill="#c94f53" overflow="visible" ry="1" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="8" height="2" x="36" y="40" fill="#f3f3f2" overflow="visible" ry="0" style="isolation:auto;mix-blend-mode:normal"></rect>
    <path fill="#f3f3f2" d="M36 41v3l2-2v-1z" overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path>
    <rect width="4" height="1" x="48" y="42" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="8" height="1" x="53" y="42" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="2" height="1" x="55" y="44" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="8" height="1" x="48" y="46" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="5" height="1" x="44" y="50" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="3" height="1" x="50" y="50" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="4" height="1" x="53" y="52" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="3" height="1" x="44" y="54" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="7" height="1" x="48" y="54" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="4" height="1" x="44" y="58" fill="#92999c" overflow="visible" rx=".5" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
  </g>
  <g fill="#f3f3f2" color="#000" class="svg_l t_3">
    <rect width="5" height="1" x="67" y="72" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="3" height="1" x="73" y="72" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="2.8" height="1" x="67.2" y="74" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="4" height="1" x="71" y="74" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="7" height="1" x="67" y="76" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="4" height="1" x="75" y="76" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="2" height="1" x="68" y="78" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="5" height="1" x="71" y="78" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="4" height="1" x="67" y="80" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
    <rect width="6" height="1" x="72" y="80" overflow="visible" ry=".5" style="isolation:auto;mix-blend-mode:normal"></rect>
  </g>
</svg>
"""

_HTML_code = [ """
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
    0px; min-height: 56px; z-index: 2; background: #F3F3F2;}
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

    .list::-webkit-scrollbar { height: 14px; width: 14px; border-color: #1E1E21; }
    .list::-webkit-scrollbar-thumb { background-clip: padding-box; border-radius: 7px;
    border-color: #1E1E21; background-color: #c2c5c9; border-style:
    solid; border-width: 3px; }
    .list::-webkit-scrollbar-track { background-clip:
    padding-box; border-radius: 8px; border-color: #1E1E21; background-color:
    #2F2F34; border-style: solid; border-width: 2px; }

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

    .splash { display: initial; text-align: center; bottom: 0; height:
    max-content; left: 0; margin: auto; position: absolute; right: 0; top: 0;
    max-width: 430px; }
    .splash svg {max-height: 400px;}
    .splash span {line-height: 0; font-size: 2em; color: #a4b1b6;}
    .svg_t {animation-direction: alternate;animation-duration: 1.5s;animation-iteration-count: infinite;animation-name: float-landing;animation-timing-function: ease-in-out;}
    .svg_l { animation-direction: alternate; animation-duration: 2s;
    animation-iteration-count: infinite; animation-name: text-landing;
    animation-timing-function: ease-in-out; }
    @keyframes float-landing { 0% { -webkit-transform: translate3d(0,-2px,0);
    transform: translate3d(0,-2px,0) }
    to { -webkit-transform: translate3d(0,2px,0); transform: translate3d(0,2px,0) } }
    @keyframes text-landing { 0% { opacity: 0.1; }
    to { opacity: 1; } }

    .t_3 { animation-delay: .4s; }
    .t_2 { animation-delay: .6s; }


    .panels-menu li a { padding: 0.75em 1.5em; transition: .2s all ease-in-out;
    display: block; margin-bottom: .5em;}
    .panels-menu li.selected{ border-left:  4px solid; border-color: #F3F3F2;
    background: rgba(0,0,0,0.2); border-radius: .3rem; margin: 0 1rem;}
    .reduced {transform: scale(.9) translateZ(0px); }
    .grow {transform: scale(.9) translateZ(0px);opacity: 0; transition: .2s all ease-in-out; }
    .animated { animation: show 0.3s 0.25s ease-in-out 1 forwards; opacity: 0;
    transform: translate(4em, 0); transition: height 2s ease-in-out; overflow: hidden; max-width: 90%;}
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
            <div class="sep"></div>""",

            '<h1 class="big" id="fcount">{0} Items</h1>',

            """<div class="left"> <button class="button" onclick="menu()"> <svg class="ico"
id="bham" viewBox="0 0 24 24"><path id="mon" fill="#303f46" d="M3
18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"> </svg> </button> </div>
</div> <div class="list"> <ul class="files" id="fls">""",

            """ <div class="splash">{}<span>{}</span></div> """,

            """<li class="file animated"><div class="tb-e tb1"><input class="checkb" type="checkbox" name="pdfs" value="{0}" onclick="addFile('{0}')"></div>
            <div class="tb-e"><span>{2}</span></div>
            <div class="tb-e"><span>{3}</span></div>
            <div class="tb-e tb-g"><span>{1}</span></div>
            </li>""", #4

            """</ul> </div> <div id="console"></div> </div> <div class="settings"> <div
class="pane p0"> <ul class="panels-menu"> <li class="lCore selected"><a
class="icon ico-c" onclick="setPane('Core');">Core</a></li> <li class="lKeys"><a
class="icon ico-k" onclick="setPane('Keys');">Keybind</a></li> <li
class="lStruc"><a class="icon ico-s"
onclick="setPane('Struc');">Structures</a></li> <li class="lAbout"><a
class="icon ico-a" onclick="setPane('About');">About</a></li> </ul> </div> <div
class="pane p1"> <div class="panels-content active" id="Core"> <script> var
_path = '{0}'; var _out = '{1}';""", #5

            """ function reset() {
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
                } """, #6

                """</script> <h2 class="pane-title">Core Settings</h2> <div class="pane-block">
<span>Change core comportement</span> </div> <div class="pane-block"> <h4
class="small-title">Search path</h4> <span class="muted">Folder where source
file are</span> <input class="input-text" name="path" type="text"
placeholder="path" maxlength="256" value="{0}"> </div> <div class="pane-block">
<h4 class="small-title">Output folder</h4> <span class="muted">Folder where
files will output</span> <input class="input-text" name="out" type="text"
placeholder="path" maxlength="256" value="{1}"> </div> <div class="pane-block
fixed"> <button class="button btn btn-cancel" onClick="reset();">Cancel</button>
<button class="button btn btn-save" onClick="save();">Save</button> </div>
</div> <div class="panels-content" id="Keys"> <h2
class="pane-title">Keybind</h2> <div class="pane-block"> <ul class="keys"><li
class="khead"><div class="tb-e"><span>Key</span></div><div class="tb-e
tb-g"><span>Action</span></div></li>""", #7

            """<li class="key"> <div class="tb-e"><span>{0}</span></div> <div class="tb-e
tb-g"><span>{1}</span></div> </li>""", #8

            """</ul> </div> </div> <div class="panels-content" id="Struc"> <h2
class="pane-title">Structures</h2> <div class="pane-block"> <span>Pre-defined
output</span> </div> <div class="pane-block"> <div class="markup"> <pre> <code
class="xml"> <span class="tag">&lt;<span class="name">article</span>&gt;</span> """, #9

            """ <span class="tag sub">&lt;<span class="name">{0}</span>&gt; the {0} &lt;/<span class="name">{0}</span>&gt;</span> """, #10

            """ <span class="tag">&lt;/<span
class="name">article</span>&gt;</span> </code> </pre> </div> </div> <div
class="pane-block"> <div class="markup"> <pre> <code class="text"> """, #11

            """ <span class="tag"><span class="name">{0}</span></span> <span class="tag">
the {1} </span>""", #12

            """ <span class="tag"><span class="name">{0}</span></span>""", #13

            """ </code> </pre> </div> </div> </div>""", #14

            """ <div class="panels-content" id="About"> <span class="about-title"> <svg
class="ico" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"> <path
fill="#f3f3f2" d="M4 3v18h12l4-4V3z" color="#000" overflow="visible"
style="isolation:auto;mix-blend-mode:normal"></path> <path fill="#f3f3f2" d="M2
5h8v6H2z" color="#000" overflow="visible"
style="isolation:auto;mix-blend-mode:normal"></path> <path fill="#f3f3f2" d="M3
6h6v3H3z" color="#000" overflow="visible"
style="isolation:auto;mix-blend-mode:normal"></path> <g fill="#bb2429"> <path
fill="#a4b1b6" d="M5 4v1h13v10h-4v4H6v-8H5v9h10l4-4V4z" color="#000"
overflow="visible" style="isolation:auto;mix-blend-mode:normal"></path> </g>
<path fill="#92999c" d="M10 7v1h5V7h-5zm0 2v1h3V9h-3zm-2 2v1h8v-1H8zm0
2v1h4v-1H8zm0 2v1h5v-1H8z" color="#000" overflow="visible"
style="isolation:auto;mix-blend-mode:normal"></path> <path fill="#c94f53" d="M9
10V6H3v4zM5 8L4 9V7h4v1z" color="#000" overflow="visible"
style="isolation:auto;mix-blend-mode:normal"></path> </svg> PDF Parser</span>
<div class="pane-block"> <span class="about-version">{}</span> </div> <div
class="pane-block"> <h4 class="small-title">Used libraries</h4> <span
class="muted">Python {}</span> <span class="muted">Chrome {}</span> <span
class="muted">Pickle {}</span> <span class="muted">CEF {}</span> </div> <div
class="pane-block"> <h4 class="small-title">Team</h4>""", #15

        """<span class="muted">{}</span>""", #16

        """</div> </div> </div> <button class="button fixed" onclick="menu()">
<svg class="ico" id="bham" viewBox="0 0 24 24"><path id="mon" fill="#303f46"
<path d="M6.3 5L5 6.2l5.7 5.7-5.7 5.7L6.3 19l5.7-5.7 5.7 5.7 1.4-1.4-5.7-5.7
5.7-5.7L17.7 5 12 10.6 6.3 4.9z"/>> </path></svg> </button> </div> </body>
</html> """, #17
        """ ERROR """ #18
            ]
