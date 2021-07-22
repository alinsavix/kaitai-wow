# This makefile probably requires GNU make. Sorry.
OUTDIR=outputs

PYTHON_BIN ?= python3
PIP_BIN ?= pip3
KSY_COMPILER ?= kaitai-struct-compiler
KSY_MERGE=$(PYTHON_BIN) ./ksy-merge.py

FILETYPES = $(basename $(notdir $(wildcard filetypes/*.ksy)))


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

ksy: $(KSY_TARGETS)

.PRECIOUS: $(KSY_OUTDIR)/%.ksy
$(KSY_OUTDIR)/%.ksy:
	@mkdir -p $(KSY_OUTDIR)
	$(KSY_MERGE) --deps-file $(DEPS_DIR)/$(@F).d --deps-target $(KSY_OUTDIR)/$(@F) filetypes/$(@F) >$@.tmp && mv $@.tmp $@


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
WOWDUMP_TARGETS = $(addprefix $(WOWDUMP_OUTDIR)/, $(addsuffix .py, $(FILETYPES)))

wowdump: $(WOWDUMP_TARGETS)

$(WOWDUMP_OUTDIR)/%.py: $(PYTHON_OUTDIR)/%.py
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
		$(KSY_MERGE) --deps-only --deps-file "$(DEPS_DIR)/$${type}.ksy.d" --deps-target "$(KSY_OUTDIR)/$${type}.ksy" "filetypes/$${type}.ksy"; \
	done


.PHONY: test
test: wowdump
	python3 ./wowdump.py


.PHONY: lint
lint:
	yamllint --config-file .yamllint.yaml chunks enums filetypes types


# Just python packaging, for right now, at least.
.PHONY: dist
dist:
	$(PYTHON_BIN) -m build


.PHONY: install
install:
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
