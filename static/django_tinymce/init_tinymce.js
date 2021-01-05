'use strict';

{
  function initTinyMCE(el) {
    if (el.closest('.empty-form') === null) {  // Don't do empty inlines
      var mce_conf = JSON.parse(el.dataset.mceConf);

      mce_conf.relative_urls = false;
      mce_conf.remove_script_host = false;
      mce_conf.document_base_url = 'https://www.trdwll.com/';
      mce_conf.codesample_languages = [
        { text: 'None ', value : 'no-highlighting'},
        { text: '1C ', value : '1c'},
        { text: '4D ', value : '4d'},
        { text: 'ABNF ', value : 'abnf'},
        { text: 'Access logs', value : 'accesslog'},
        { text: 'Ada', value : 'ada'},
        { text: 'Arduino', value : 'arduino'},
        { text: 'ARM assembler', value : 'armasm'},
        { text: 'AVR assembler', value : 'avrasm'},
        { text: 'ActionScript ', value : 'actionscript'},
        { text: 'Alan IF', value : 'alan'},
        { text: 'Alan ', value : 'ln'},
        { text: 'AngelScript', value : 'angelscript'},
        { text: 'Apache ', value : 'apache'},
        { text: 'AppleScript', value : 'applescript'},
        { text: 'Arcade ', value : 'arcade'},
        { text: 'AsciiDoc ', value : 'asciidoc'},
        { text: 'AspectJ', value : 'aspectj'},
        { text: 'AutoHotkey ', value : 'autohotkey'},
        { text: 'AutoIt ', value : 'autoit'},
        { text: 'Awk', value : 'awk'},
        { text: 'Bash ', value : 'bash'},
        { text: 'Basic', value : 'basic'},
        { text: 'BBCode ', value : 'bbcode'},
        { text: 'Blade (Laravel)', value : 'blade'},
        { text: 'BNF', value : 'bnf'},
        { text: 'Brainfuck', value : 'brainfuck'},
        { text: 'C# ', value : 'csharp'},
        { text: 'C', value : 'c'},
        { text: 'C++', value : 'cpp'},
        { text: 'C/AL ', value : 'cal'},
        { text: 'Cache Object Script', value : 'cos'},
        { text: 'CMake', value : 'cmake'},
        { text: 'Coq', value : 'coq'},
        { text: 'CSP', value : 'csp'},
        { text: 'CSS', value : 'css'},
        { text: 'Cap’n Proto', value : 'capnproto'},
        { text: 'Chaos', value : 'chaos'},
        { text: 'Chapel ', value : 'chapel'},
        { text: 'Cisco CLI', value : 'cisco'},
        { text: 'Clojure', value : 'clojure'},
        { text: 'CoffeeScript ', value : 'coffeescript'},
        { text: 'CpcdosC+ ', value : 'cpc'},
        { text: 'Crmsh', value : 'crmsh'},
        { text: 'Crystal', value : 'crystal'},
        { text: 'Cypher (Neo4j) ', value : 'cypher'},
        { text: 'D', value : 'd'},
        { text: 'DNS Zone file', value : 'dns'},
        { text: 'DOS', value : 'dos'},
        { text: 'Dart ', value : 'dart'},
        { text: 'Delphi ', value : 'delphi'},
        { text: 'Diff ', value : 'diff'},
        { text: 'Django ', value : 'django'},
        { text: 'Dockerfile ', value : 'dockerfile'},
        { text: 'dsconfig ', value : 'dsconfig'},
        { text: 'DTS (Device Tree)', value : 'dts'},
        { text: 'Dust ', value : 'dust'},
        { text: 'Dylan', value : 'dylan'},
        { text: 'EBNF ', value : 'ebnf'},
        { text: 'Elixir ', value : 'elixir'},
        { text: 'Elm', value : 'elm'},
        { text: 'Erlang ', value : 'erlang'},
        { text: 'Excel', value : 'excel'},
        { text: 'Extempore', value : 'extempore'},
        { text: 'F# ', value : 'fsharp'},
        { text: 'FIX', value : 'fix'},
        { text: 'Fortran', value : 'fortran'},
        { text: 'G-Code ', value : 'gcode'},
        { text: 'Gams ', value : 'gams'},
        { text: 'GAUSS', value : 'gauss'},
        { text: 'GDScript ', value : 'godot'},
        { text: 'Gherkin', value : 'gherkin'},
        { text: 'GN for Ninja ', value : 'gn'},
        { text: 'Go ', value : 'go'},
        { text: 'Grammatical Framework', value : 'gf'},
        { text: 'Golo ', value : 'golo'},
        { text: 'Gradle ', value : 'gradle'},
        { text: 'Groovy ', value : 'groovy'},
        { text: 'HTML, XML', value : 'xml'},
        { text: 'HTTP ', value : 'http'},
        { text: 'Haml ', value : 'haml'},
        { text: 'Handlebars ', value : 'handlebars'},
        { text: 'Haskell', value : 'haskell'},
        { text: 'Haxe ', value : 'haxe'},
        { text: 'Hy ', value : 'hy'},
        { text: 'Ini, TOML', value : 'ini'},
        { text: 'Inform7', value : 'inform7'},
        { text: 'IRPF90 ', value : 'irpf90'},
        { text: 'JSON ', value : 'json'},
        { text: 'Java ', value : 'java'},
        { text: 'JavaScript ', value : 'javascript'},
        { text: 'Jolie', value : 'jolie'},
        { text: 'Julia', value : 'julia'},
        { text: 'Kotlin ', value : 'kotlin'},
        { text: 'LaTeX', value : 'tex'},
        { text: 'Leaf ', value : 'leaf'},
        { text: 'Lean ', value : 'lean'},
        { text: 'Lasso', value : 'lasso'},
        { text: 'Less ', value : 'less'},
        { text: 'LDIF ', value : 'ldif'},
        { text: 'Lisp ', value : 'lisp'},
        { text: 'LiveCode Server', value : 'livecodeserver'},
        { text: 'LiveScript ', value : 'livescript'},
        { text: 'Lua', value : 'lua'},
        { text: 'Makefile ', value : 'makefile'},
        { text: 'Markdown ', value : 'markdown'},
        { text: 'Mathematica', value : 'mathematica'},
        { text: 'Matlab ', value : 'matlab'},
        { text: 'Maxima ', value : 'maxima'},
        { text: 'Maya Embedded Language ', value : 'mel'},
        { text: 'Mercury', value : 'mercury'},
        { text: 'mIRC Scripting Language', value : 'mirc'},
        { text: 'Mizar', value : 'mizar'},
        { text: 'Mojolicious', value : 'mojolicious'},
        { text: 'Monkey ', value : 'monkey'},
        { text: 'Moonscript ', value : 'moonscript'},
        { text: 'N1QL ', value : 'n1ql'},
        { text: 'NSIS ', value : 'nsis'},
        { text: 'Never', value : 'never'},
        { text: 'Nginx', value : 'nginx'},
        { text: 'Nim', value : 'nim'},
        { text: 'Nix', value : 'nix'},
        { text: 'Object Constraint Language', value : 'ocl'},
        { text: 'OCaml', value : 'ocaml'},
        { text: 'Objective C', value : 'objectivec'},
        { text: 'OpenGL Shading Language', value : 'glsl'},
        { text: 'OpenSCAD ', value : 'openscad'},
        { text: 'Oracle Rules Language', value : 'ruleslanguage'},
        { text: 'Oxygene', value : 'oxygene'},
        { text: 'PF ', value : 'pf'},
        { text: 'PHP', value : 'php'},
        { text: 'Parser3', value : 'parser3'},
        { text: 'Perl ', value : 'perl'},
        { text: 'Plaintext', value : 'plaintext'},
        { text: 'Pony ', value : 'pony'},
        { text: 'PostgreSQL & PL/pgSQL', value : 'pgsql'},
        { text: 'PowerShell ', value : 'powershell'},
        { text: 'Processing ', value : 'processing'},
        { text: 'Prolog ', value : 'prolog'},
        { text: 'Properties ', value : 'properties'},
        { text: 'Protocol Buffers ', value : 'protobuf'},
        { text: 'Puppet ', value : 'puppet'},
        { text: 'Python ', value : 'python'},
        { text: 'Python profiler results', value : 'profile'},
        { text: 'Python REPL', value : 'python-repl'},
        { text: 'Q', value : 'k'},
        { text: 'QML', value : 'qml'},
        { text: 'R', value : 'r'},
        { text: 'Razor CSHTML ', value : 'cshtml'},
        { text: 'ReasonML ', value : 'reasonml'},
        { text: 'Rebol & Red', value : 'redbol'},
        { text: 'RenderMan RIB', value : 'rib'},
        { text: 'RenderMan RSL', value : 'rsl'},
        { text: 'Roboconf ', value : 'graph'},
        { text: 'Robot Framework', value : 'robot'},
        { text: 'RPM spec files ', value : 'rpm-specfile'},
        { text: 'Ruby ', value : 'ruby'},
        { text: 'Rust ', value : 'rust'},
        { text: 'SAS', value : 'SAS'},
        { text: 'SCSS ', value : 'scss'},
        { text: 'SQL', value : 'sql'},
        { text: 'STEP Part 21 ', value : 'p21'},
        { text: 'Scala', value : 'scala'},
        { text: 'Scheme ', value : 'scheme'},
        { text: 'Scilab ', value : 'scilab'},
        { text: 'Shape Expressions', value : 'shexc'},
        { text: 'Shell', value : 'shell'},
        { text: 'Smali', value : 'smali'},
        { text: 'Smalltalk', value : 'smalltalk'},
        { text: 'SML', value : 'sml'},
        { text: 'Solidity ', value : 'solidity'},
        { text: 'Stan ', value : 'stan'},
        { text: 'Stata', value : 'stata'},
        { text: 'Structured Text', value : 'iecst'},
        { text: 'Stylus ', value : 'stylus'},
        { text: 'SubUnit', value : 'subunit'},
        { text: 'Supercollider', value : 'supercollider'},
        { text: 'Svelte ', value : 'svelte'},
        { text: 'Swift', value : 'swift'},
        { text: 'Tcl', value : 'tcl'},
        { text: 'Terraform (HCL)', value : 'terraform'},
        { text: 'Test Anything Protocol ', value : 'tap'},
        { text: 'Thrift ', value : 'thrift'},
        { text: 'TP ', value : 'tp'},
        { text: 'Transact-SQL ', value : 'tsql'},
        { text: 'Twig ', value : 'twig'},
        { text: 'TypeScript ', value : 'typescript'},
        { text: 'Unicorn Rails log', value : 'unicorn-rails-log'},
        { text: 'VB.Net ', value : 'vbnet'},
        { text: 'VBA', value : 'vba'},
        { text: 'VBScript ', value : 'vbscript'},
        { text: 'VHDL ', value : 'vhdl'},
        { text: 'Vala ', value : 'vala'},
        { text: 'Verilog', value : 'verilog'},
        { text: 'Vim Script ', value : 'vim'},
        { text: 'X++', value : 'axapta'},
        { text: 'x86 Assembly ', value : 'x86asm'},
        { text: 'XL ', value : 'xl'},
        { text: 'XQuery ', value : 'xquery'},
        { text: 'YAML ', value : 'yml'},
        { text: 'Zephir ', value : 'zephir'}
      ];

      // There is no way to pass a JavaScript function as an option
      // because all options are serialized as JSON.
      const fns = [
        'color_picker_callback',
        'file_browser_callback',
        'file_picker_callback',
        'images_dataimg_filter',
        'images_upload_handler',
        'paste_postprocess',
        'paste_preprocess',
        'setup',
        'urlconverter_callback',
      ];
      fns.forEach((fn_name) => {
        if (typeof mce_conf[fn_name] != 'undefined') {
          if (mce_conf[fn_name].includes('(')) {
            mce_conf[fn_name] = eval('(' + mce_conf[fn_name] + ')');
          }
          else {
            mce_conf[fn_name] = window[mce_conf[fn_name]];
          }
        }
      });

      const id = el.id;
      if ('elements' in mce_conf && mce_conf['mode'] == 'exact') {
        mce_conf['elements'] = id;
      }
      if (el.dataset.mceGzConf) {
        tinyMCE_GZ.init(JSON.parse(el.dataset.mceGzConf));
      }
      if (!tinyMCE.editors[id]) {
        tinyMCE.init(mce_conf);
      }
    }
  }

  // Call function fn when the DOM is loaded and ready. If it is already
  // loaded, call the function now.
  // http://youmightnotneedjquery.com/#ready
  function ready(fn) {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  }

  ready(function() {
    // initialize the TinyMCE editors on load
    document.querySelectorAll('.tinymce').forEach(function(el) {
      initTinyMCE(el);
    });

    // initialize the TinyMCE editor after adding an inline
    document.body.addEventListener("click", function(ev) {
      if (!ev.target.parentNode ||
          !ev.target.parentNode.getAttribute("class") ||
          !ev.target.parentNode.getAttribute("class").includes("add-row")) {
        return;
      }
      const addRow = ev.target.parentNode;
      setTimeout(function() {  // We have to wait until the inline is added
        addRow.parentNode.querySelectorAll('textarea.tinymce').forEach(function(el) {
          initTinyMCE(el);
        });
      }, 0);
    }, true);
  });
}
