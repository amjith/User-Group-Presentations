SOURCE = profiling.rst
TEX = profiling.tex
OUTPUT = profiling.pdf
PROG = python ~/Downloads/rst2beamer.py
#PROG = rst2beamer
TEX_PROG = /usr/texbin/pdflatex
#TEX_PROG = pdflatex
VIEWER = open
#VIEWER = xpdf

all:
	$(PROG) --codeblocks-use-pygments --overlaybullets='' $(SOURCE) $(TEX)
	$(TEX_PROG) $(TEX)
	$(VIEWER) $(OUTPUT)
