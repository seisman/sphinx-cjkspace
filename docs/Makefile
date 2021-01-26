# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = sphinx-cjkspace
SOURCEDIR     = .
BUILDDIR      = _build
BUILDER       = html

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
	sed -i.bak "s/'sphinx_cjkspace.cjkspace'/#'sphinx_cjkspace.cjkspace'/" conf.py
	sed -i.bak "s/（使用后）/（使用前）/" example/*.rst
	make $(BUILDER)
	cp -r $(BUILDDIR)/$(BUILDER)/example/ $(BUILDDIR)

	# with cjkspace extension
	sed -i.bak "s/#'sphinx_cjkspace.cjkspace'/'sphinx_cjkspace.cjkspace'/" conf.py
	sed -i.bak "s/（使用前）/（使用后）/" example/*.rst
	make $(BUILDER)
	mv $(BUILDDIR)/example/ $(BUILDDIR)/$(BUILDER)/example2/

serve: docs
	cd $(BUILDDIR)/$(BUILDER) && python -m http.server
