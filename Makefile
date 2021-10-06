LATEX:=pdflatex
BIBTEX:=bibtex
TEX:=robdml.tex

robdml: introdiag.pdf
	$(LATEX) $(TEX)
	$(BIBTEX) robdml
	$(LATEX) $(TEX)
	$(LATEX) $(TEX)
	-evince robdml.pdf

clean:
	-$(RM) *.aux *.bbl *.blg *.brf *.log *.out *.pdf

introdiag.pdf:
	inkscape -o introdiag.pdf introdiag.svg
