# Copyright (C) 2021-2022 Mo Zhou <cdluminate@gmail.com>
# License: Apache-2.0

LATEX:=pdflatex
BIBTEX:=bibtex
TEX:=robdml.tex
SUPP:=supp.tex
VIEWER:=evince

PDFS:= hmillust.pdf gaillust.pdf icsapn.pdf fighmeff.pdf figgaeff.pdf  introplot.pdf figics.pdf hmflexible.pdf

default: robdml

reb:
	$(MAKE) -C reb

robdml: $(PDFS)
	$(LATEX) $(TEX)
	$(BIBTEX) robdml
	$(LATEX) $(TEX)
	$(LATEX) $(TEX)
	-$(VIEWER) robdml.pdf

supp: $(PDFS)
	$(LATEX) $(SUPP)
	$(BIBTEX) supp
	$(LATEX) $(SUPP)
	$(LATEX) $(SUPP)
	-$(VIEWER) supp.pdf

clean:
	-$(RM) *.aux *.bbl *.blg *.brf *.log *.out *.pdf

introplot.pdf:
	python3 introplot.py -w 1
	inkscape -o introplot.pdf introplot.svg
	pdfcrop introplot.pdf
	mv introplot-crop.pdf introplot.pdf

hmillust.pdf:
	inkscape -o hmillust.pdf hmillust.svg
	pdfcrop hmillust.pdf
	mv hmillust-crop.pdf hmillust.pdf

gaillust.pdf:
	inkscape -o gaillust.pdf gaillust.svg

icsapn.pdf:
	inkscape -o icsapn.pdf icsapn.svg

fighmeff.pdf:
	python3 introplot.py -w 2
	inkscape -o fighmeff.pdf fighmeff.svg
	pdfcrop fighmeff.pdf
	mv fighmeff-crop.pdf fighmeff.pdf

figgaeff.pdf:
	python3 introplot.py -w 3
	inkscape -o figgaeff.pdf figgaeff.svg
	pdfcrop figgaeff.pdf
	mv figgaeff-crop.pdf figgaeff.pdf

figics.pdf:
	python3 introplot.py -w 4
	inkscape -o figics.pdf figics.svg
	pdfcrop figics.pdf
	mv figics-crop.pdf figics.pdf

hmflexible.pdf:
	inkscape -o hmflexible.pdf hmflexible.svg
