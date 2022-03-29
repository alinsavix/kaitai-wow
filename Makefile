# This makefile probably requires GNU make. Sorry.
OUTDIR=outputs
KSY_DIR=ksy
PYTHON_BIN ?= python3
PIP_BIN ?= pip3
BASH ?= bash
KSY_COMPILER ?= kaitai-struct-compiler
KSY_MERGE=$(PYTHON_BIN) scripts/ksy-merge.py

FILETYPES = $(basename $(notdir $(wildcard $(KSY_DIR)/filetypes/*.ksy)))
KSY_SUBDIRS=chunks enums filetypes types


all: ksy python wowdump

# all_langs:


DEPS_DIR = .deps
DEPSFILES = $(wildcard .deps/*.d)
$(foreach file,$(DEPSFILES),$(eval -include $(file)))

#
# ksy -- everything needs this
#
KSY_OUTDIR ?= $(OUTDIR)/ksy
KSY_TARGETS = $(addprefix $(KSY_OUTDIR)/, $(addsuffix .ksy, $(FILETYPES)))

METADATA_OUTDIR ?= $(OUTDIR)/metadata
METADATA_TARGETS = $(addprefix $(METADATA_OUTDIR)/, $(addsuffix .yaml, $(FILETYPES)))

ksy: $(KSY_TARGETS) $(METADATA_TARGETS)

.PRECIOUS: $(KSY_OUTDIR)/%.ksy
$(KSY_OUTDIR)/%.ksy $(METADATA_OUTDIR)/%.yaml:
	@mkdir -p $(KSY_OUTDIR) $(METADATA_OUTDIR)
	$(KSY_MERGE) --deps-file $(DEPS_DIR)/$(*F).ksy.d --deps-target $(KSY_OUTDIR)/$(*F).ksy --metadata-file $(METADATA_OUTDIR)/$(*F).yaml $(KSY_DIR)/filetypes/$(*F).ksy >$@.tmp && mv $@.tmp $@


#
# python
#
PYTHON_OUTDIR ?= $(OUTDIR)/python
PYTHON_TARGETS = $(addprefix $(PYTHON_OUTDIR)/, $(addsuffix .py, $(FILETYPES)))

python: $(PYTHON_TARGETS)

.PRECIOUS: $(PYTHON_OUTDIR)/%.py
$(PYTHON_OUTDIR)/%.py: $(KSY_OUTDIR)/%.ksy
	$(KSY_COMPILER) --outdir $(PYTHON_OUTDIR) --target python $<


#
# wowdump
#
WOWDUMP_OUTDIR = wowdump/filetypes
WOWDUMP_FILETYPE_TARGETS = $(addprefix $(WOWDUMP_OUTDIR)/, $(addsuffix .py, $(FILETYPES)))
WOWDUMP_FILEMETA_TARGETS = $(addprefix $(WOWDUMP_OUTDIR)/, $(addsuffix .yaml, $(FILETYPES)))
WOWDUMP_TARGETS = $(WOWDUMP_OUTDIR)/__init__.py $(WOWDUMP_FILETYPE_TARGETS) $(WOWDUMP_FILEMETA_TARGETS)

wowdump: $(WOWDUMP_TARGETS)

$(WOWDUMP_OUTDIR)/__init__.py: $(WOWDUMP_FILETYPE_TARGETS) scripts/gen_wowdump_filetypes.sh
	@mkdir -p $(WOWDUMP_OUTDIR)
	bash scripts/gen_wowdump_filetypes.sh $(FILETYPES) >"$@"


$(WOWDUMP_OUTDIR)/%.py: $(PYTHON_OUTDIR)/%.py
	@mkdir -p $(WOWDUMP_OUTDIR)
	cp "$<" "$@"

$(WOWDUMP_OUTDIR)/%.yaml: $(METADATA_OUTDIR)/%.yaml
	@mkdir -p $(WOWDUMP_OUTDIR)
	cp "$<" "$@"


#
# svg
#
SVG_OUTDIR ?= $(OUTDIR)/svg
SVG_TARGETS = $(addprefix $(SVG_OUTDIR)/, $(addsuffix .svg, $(FILETYPES)))

svg: $(SVG_TARGETS)

$(SVG_OUTDIR)/%.svg: $(SVG_OUTDIR)/%.dot
	dot -Tsvg $< >$@

$(SVG_OUTDIR)/%.dot: $(KSY_OUTDIR)/%.ksy
	$(KSY_COMPILER) --outdir $(SVG_OUTDIR) --target graphviz $<


#
# html
#
HTML_OUTDIR ?= $(OUTDIR)/html
HTML_TARGETS = $(addprefix $(HTML_OUTDIR)/, $(addsuffix .html, $(FILETYPES)))

html: $(HTML_TARGETS)

$(HTML_OUTDIR)/%.html: $(KSY_OUTDIR)/%.ksy
	$(KSY_COMPILER) --outdir $(HTML_OUTDIR) --target html $<


#
# all_langs
#
.PHONY: all_langs
ALL_LANGS_OUTDIR ?= $(OUTDIR)/all
ALL_LANGS_LIST = construct csharp go graphviz html java javascript lua nim perl php python ruby

# We could do this with just `--target all`, except that throws a lot of
# warnings -and- exits with an error code because of languages that are
# not well-supported by kaitai-struct. So instead we cycle through the
# languages one at a time, which takes forever, but stops everything from
# erroring unless there's actually an error
all_langs: ksy
	@for lang in $(ALL_LANGS_LIST); \
	do \
		for type in $(FILETYPES); \
		do \
			echo $(KSY_COMPILER) --outdir $(ALL_LANGS_OUTDIR)/$${lang} --target $${lang} $(KSY_OUTDIR)/$${type}.ksy; \
			$(KSY_COMPILER) --outdir $(ALL_LANGS_OUTDIR)/$${lang} --target $${lang} $(KSY_OUTDIR)/$${type}.ksy; \
			if [ $$? -gt 0 ]; then echo "$(KSY_COMPILER) failed on $${type}.ksy for $${lang}"; exit 1; fi \
		done; \
	done


#
# utility and other targets
#

# FIXME: Is there a better way? This way seems... awful...
.PHONY: depend
depend:
	@for type in $(FILETYPES); do \
		$(KSY_MERGE) --deps-only --deps-file "$(DEPS_DIR)/$${type}.ksy.d" --deps-target "$(KSY_OUTDIR)/$${type}.ksy" "$(KSY_DIR)/filetypes/$${type}.ksy"; \
	done


.PHONY: test
test: wowdump
	pytest


.PHONY: benchmark
benchmark: wowdump
	python3 -m cProfile -o wowdump-m2-valeera-geometry-$$(date +%Y%m%dT%H%M%S).prof ./wowdump-script.py -o zot.tmp --geometry --arraylimit 0 testfiles/valeera/valeera.m2
	python3 -m cProfile -o wowdump-m2-valeera-nogeometry-$$(date +%Y%m%dT%H%M%S).prof ./wowdump-script.py -o zot.tmp testfiles/valeera/valeera.m2


.PHONY: lint
lint:
	yamllint --config-file $(KSY_DIR)/.yamllint.yaml $(addprefix $(KSY_DIR)/, $(KSY_SUBDIRS))


# Just python packaging, for right now, at least.
.PHONY: dist
dist: wowdump
	@if ! $(PIP_BIN) show 'build' >/dev/null 2>&1; then \
		echo "ERROR: python 'build' package is required (hint: $(PIP_BIN) install build)";  \
		exit 1; \
	fi
	$(PYTHON_BIN) -m build -n -w


.PHONY: install
install: wowdump
	$(PIP_BIN) install .


.PHONY: localdev
localdev: wowdump
	$(PIP_BIN) install --editable .


.PHONY: clean realclean
clean:
	rm -rf ./$(OUTDIR)/* ./$(WOWDUMP_OUTDIR)/* ./$(DEPS_DIR)/*.*P ./$(DEPS_DIR)/*.d

realclean: clean
	rm -rf dist build */*.egg-info *.egg-info


print-%: ;@echo $*=$($*)
