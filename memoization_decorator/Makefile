SOURCE = memoization_decorator.rst
TEX = memoization_decorator.tex
OUTPUT = memoization_decorator.pdf
PROG = python ~/Downloads/rst2beamer.py
#PROG = rst2beamer
#TEX_PROG = /usr/texbin/pdflatex
TEX_PROG = pdflatex
#VIEWER = open
VIEWER = xpdf

all:
	$(PROG) --codeblocks-use-pygments --overlaybullets='' $(SOURCE) $(TEX)
	$(TEX_PROG) $(TEX)
	$(VIEWER) $(OUTPUT)
