---
title: Acknowledging Econ-ARK
permalink: acknowledging
menu_item: false
---
# Acknowledging Econ-ARK

Please use the following methods to acknowledge or cite the Econ-ARK project.

In Projects
-----------

If you are using Econ-ARK as part of a code project you can simply acknowledge your use of Econ-ARK with a badge in your README. We suggest this badge:

![](https://img.shields.io/badge/Powered%20by-Econ--ARK-3e8acc.svg)

You can use the following line of HTML:

    <a href="https://econ-ark.org/" title="econ-ark.org"><img alt="Powered by Econ-ARK" src="https://img.shields.io/badge/Powered%20by-Econ--ARK-3e8acc.svg" /></a>

Or Markdown:

    [![econ-ark.org](https://img.shields.io/badge/Powered%20by-Econ--ARK-3e8acc.svg)](https://econ-ark.org/)
    

For LaTeX:

1. Download either (or both) versions of the button to the directory containing the LaTeX file:
https://github.com/econ-ark/econ-ark.org/tree/Fix-LaTeX-Button/pages/resources
    * [pdf](https://github.com/econ-ark/econ-ark.org/raw/master/pages/resources/PoweredByEconARK.pdf)
    * [svg](https://github.com/econ-ark/econ-ark.org/raw/master/pages/resources/PoweredByEconARK.svg)
1. Render the button using:
'''
\DeclareGraphicsExtensions{[whichever type you chose above]}, e.g. \DeclareGraphicsExtensions{.pdf}
`\centerline{includegraphics{PoweredByEconARK}`
'''
    
------------------------------------------------------------------------

In Publications
---------------

If you use Econ-ARK for work/research presented in a publication we ask that you please cite Econ-ARK papers:

    @InProceedings{carroll_et_al-proc-scipy-2018,
                      author    = { {C}hristopher {D}. {C}arroll and {A}lexander {M}. {K}aufman and {J}acqueline {L}. {K}azil and {N}athan {M}. {P}almer and {M}atthew {N}. {W}hite },
                      title     = { {T}he {E}con-{A}{R}{K} and {H}{A}{R}{K}: {O}pen {S}ource {T}ools for {C}omputational {E}conomics },
                      booktitle = { {P}roceedings of the 17th {P}ython in {S}cience {C}onference },
                      pages     = { 25 - 30 },
                      year      = { 2018 },
                      editor    = { {F}atih {A}kici and {D}avid {L}ippa and {D}illon {N}iederhut and {M} {P}acer },
                      doi       = { 10.25080/Majora-4af1f417-004 }
                    }

------------------------------------------------------------------------

In Presentations
----------------

If you are giving a presentation or talk and would like to acknowledge Econ-ARK, we suggest using this logo:

![](assets/img/econ-ark-logo-small.png)
