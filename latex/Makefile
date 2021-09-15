LATEX:=pdflatex
BIBTEX:=bibtex
TEX:=robdml.tex

robdml:
	$(LATEX) $(TEX)
	$(BIBTEX) robdml
	$(LATEX) $(TEX)
	$(LATEX) $(TEX)

clean:
	-$(RM) *.aux *.bbl *.blg *.brf *.log *.out *.pdf
