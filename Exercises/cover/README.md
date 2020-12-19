# Custom LaTeX Cover Page
This is a custom LaTeX cover that can be used to concatenate with 
other (MS Word or LaTeX) pdf files via 
![ghostscript](https://www.ghostscript.com/) with command like this:

```
gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=combine.pdf -dBATCH
cover.pdf Making_Dumplings_1.pdf
```

It adds the cover page at the front of the main pdf file
(`Making_Dumplings_1.pdf`) and creates a new file named
`combine.pdf`, **preserving all the pdf links and bookmarks**
in both source pdf files. An alternative in LaTeX is to 
use `\includepdf` command with `pdfpages` package to 
incorporate the cover page into the main pdf file, but
all the links will get lost during inclusion (however,
it is said that the `![pax](http://ctan.org/pkg/pax)` package
can help, see ![here](https://tex.stackexchange.com/questions/26128/
embedding-a-pdf-file-with-clickable-external-links-into-a-latex-document)
for more information).
