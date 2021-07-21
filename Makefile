# This makefile probably requires GNU make. Sorry.
OUTDIR=outputs
OUTDIR_WOWDUMP=wowdump/filetypes

DEFAULT_TARGETS=python wowdump

PYTHON_BIN ?= python3
PIP_BIN ?= pip3
KSY_COMPILER ?= kaitai-struct-compiler
KSY_MERGE=$(PYTHON_BIN) ./ksy-merge.py

FILETYPES = $(basename $(notdir $(wildcard filetypes/*.ksy)))


all: $(DEFAULT_TARGETS)


DEPS_DIR = .deps
DEPSFILES = $(wildcard .deps/*.ksyP)
$(foreach file,$(DEPSFILES),$(eval -include $(file)))

# FIXME: Is there a better way? This way seems... awful...
.PHONY: depend
depend:
	@for type in $(FILETYPES); do \
		depsfile=$$(echo "$(OUTDIR)/$${type}.ksy" | sed 's,/,__,g'); \
		$(KSY_MERGE) --deps-only --deps-file "$(DEPS_DIR)/$${depsfile}P" --deps-target "$(OUTDIR)/$${type}.ksy" "filetypes/$${type}.ksy"; \
	done


# .PHONY: test
# test: $(TARGETS)
# 	python3 ./wowdump.py


.PHONY: lint
lint:
	yamllint --config-file .yamllint.yaml chunks enums filetypes types


## kaitai -- everything needs this
OUTDIR_KSY ?= $(OUTDIR)/ksy

.PRECIOUS: $(OUTDIR_KSY)/%.ksy
$(OUTDIR_KSY)/%.ksy:
	@mkdir -p $(OUTDIR_KSY)
	$(KSY_MERGE) --deps-file $(DEPS_DIR)/$(subst /,__,$@)P --deps-target $(OUTDIR_KSY)/$(@F) filetypes/$(@F) >$@.tmp && mv $@.tmp $@


## python
OUTDIR_PYTHON ?= $(OUTDIR)/python
PYTHON_TARGETS = $(addprefix $(OUTDIR_PYTHON)/, $(addsuffix .py, $(FILETYPES)))

python: $(PYTHON_TARGETS)

.PRECIOUS: $(OUTDIR_PYTHON)/%.py
$(OUTDIR_PYTHON)/%.py: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_PYTHON)
	$(KSY_COMPILER) --outdir $(OUTDIR_PYTHON) --target python $<


## svg
$(OUTDIR)/%.svg: $(OUTDIR)/%.dot
	dot -Tsvg $< >$@

$(OUTDIR)/%.dot: $(OUTDIR)/%.ksy
	$(KSY_COMPILER) --outdir $(OUTDIR) --target graphviz $<


## wowdump
OUTDIR_WOWDUMP = wowdump/filetypes
WOWDUMP_TARGETS = $(addprefix $(OUTDIR_WOWDUMP)/, $(addsuffix .py, $(FILETYPES)))

wowdump: $(WOWDUMP_TARGETS)

.PRECIOUS: $(OUTDIR_WOWDUMP)/%.py
$(OUTDIR_WOWDUMP)/%.py: $(OUTDIR_PYTHON)/%.py
	cp "$<" "$@"


# build distribution packages -- just python, for right now, at least.
.PHONY: dist
dist:
	$(PYTHON_BIN) -m build


# install it, develop it, use it
.PHONY: install
install:
	$(PIP_BIN) install .

.PHONY: localdev
localdev:
	$(PIP_BIN) install --editable .


# cleanup
.PHONY: clean realclean
clean:
	rm -rf ./$(OUTDIR)/* ./$(DEPS_DIR)/*.*P

realclean: clean
	rm -rf dist build */*.egg-info *.egg-info


# debug
print-%: ;@echo $*=$($*)
