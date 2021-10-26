LATEX:=pdflatex
BIBTEX:=bibtex
TEX:=robdml.tex

PDFS:= introplot.pdf hmillust.pdf gaillust.pdf icsapn.pdf

robdml: $(PDFS)
	$(LATEX) $(TEX)
	$(BIBTEX) robdml
	$(LATEX) $(TEX)
	$(LATEX) $(TEX)
	-evince robdml.pdf

clean:
	-$(RM) *.aux *.bbl *.blg *.brf *.log *.out *.pdf

introplot.pdf:
	python3 introplot.py
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
