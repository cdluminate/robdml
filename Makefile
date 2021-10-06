LATEX:=pdflatex
BIBTEX:=bibtex
TEX:=robdml.tex

robdml: introplot.pdf
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
