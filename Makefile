# This makefile probably requires GNU make. Sorry.
KSY_COMPILER ?= kaitai-struct-compiler
KSY_MERGE=python3 ./ksy-merge.py
FILETYPES = $(basename $(notdir $(wildcard filetypes/*.ksy)))
TARGETS ?= $(addprefix $(OUTDIR)/, $(addsuffix .py, $(FILETYPES)))

OUTDIR=output
DEPS_DIR = .deps

all: $(OUTDIR) $(TARGETS)

DEPSFILES = $(wildcard .deps/*.ksyP)
$(foreach file,$(DEPSFILES),$(eval -include $(file)))


# FIXME: Is there a better way? This way seems... awful...
.PHONY: depend
depend:
	@for type in $(FILETYPES); do \
		depsfile=$$(echo "$(OUTDIR)/$${type}.ksy" | sed 's,/,__,g'); \
		$(KSY_MERGE) --deps-only --deps-file "$(DEPS_DIR)/$${depsfile}P" --deps-target "$(OUTDIR)/$${type}.ksy" "filetypes/$${type}.ksy"; \
	done

.PHONY: test
test: $(TARGETS)
	python3 ./wowdump.py

.PHONY: lint
lint:
	yamllint --config-file .yamllint.yaml chunks enums filetypes types
# We're just going to force it to rebuild everything every time, so we don't
# have to deal with the complexity of having a way to dynamically track
# included files as dependencies
#
# FIXME: Building everything every time has gotten kinda slow

$(OUTDIR):
	@mkdir -p $(OUTDIR)

.PRECIOUS: $(OUTDIR)/%.ksy
$(OUTDIR)/%.ksy:
	$(KSY_MERGE) --deps-file $(DEPS_DIR)/$(subst /,__,$@)P --deps-target $(OUTDIR)/$(@F) filetypes/$(@F) >$@.tmp && mv $@.tmp $@

$(OUTDIR)/%.py: $(OUTDIR)/%.ksy
	$(KSY_COMPILER) --outdir $(OUTDIR) --target python $<

$(OUTDIR)/%.svg: $(OUTDIR)/%.dot
	dot -Tsvg $< >$@

$(OUTDIR)/%.dot: $(OUTDIR)/%.ksy
	$(KSY_COMPILER)  --outdir $(OUTDIR) --target graphviz $<

.PHONY: clean
clean:
	rm -f $(OUTDIR)/*.ksy $(TARGETS) $(DEPS_DIR)/*.*P

print-%: ;@echo $*=$($*)
