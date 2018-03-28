# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = sphinx-cjkspace
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

docs: clean
	# without cjkspace extension
	sed -i "s/'sphinx_cjkspace.cjkspace'/#'sphinx_cjkspace.cjkspace'/" conf.py
	sed -i "s/效果演示（使用后）/效果演示（使用前）/" example.rst
	make html
	cp $(BUILDDIR)/html/example.html $(BUILDDIR)

	# with cjkspace extension
	sed -i "s/#'sphinx_cjkspace.cjkspace'/'sphinx_cjkspace.cjkspace'/" conf.py
	sed -i "s/效果演示（使用前）/效果演示（使用后）/" example.rst
	make html
	mv $(BUILDDIR)/example.html $(BUILDDIR)/html/example2.html
