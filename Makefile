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

ALL_LANGS =

## kaitai -- everything needs this
OUTDIR_KSY ?= $(OUTDIR)/ksy
KSY_TARGETS = $(addprefix $(OUTDIR_KSY)/, $(addsuffix .ksy, $(FILETYPES)))

ksy: $(KSY_TARGETS)
ALL_LANGS += ksy

.PRECIOUS: $(OUTDIR_KSY)/%.ksy
$(OUTDIR_KSY)/%.ksy:
	@mkdir -p $(OUTDIR_KSY)
	$(KSY_MERGE) --deps-file $(DEPS_DIR)/$(subst /,__,$@)P --deps-target $(OUTDIR_KSY)/$(@F) filetypes/$(@F) >$@.tmp && mv $@.tmp $@


## python
OUTDIR_PYTHON ?= $(OUTDIR)/python
PYTHON_TARGETS = $(addprefix $(OUTDIR_PYTHON)/, $(addsuffix .py, $(FILETYPES)))

python: $(PYTHON_TARGETS)
ALL_LANGS += python

.PRECIOUS: $(OUTDIR_PYTHON)/%.py
$(OUTDIR_PYTHON)/%.py: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_PYTHON)
	$(KSY_COMPILER) --outdir $(OUTDIR_PYTHON) --target python $<


## wowdump
OUTDIR_WOWDUMP = wowdump/filetypes
WOWDUMP_TARGETS = $(addprefix $(OUTDIR_WOWDUMP)/, $(addsuffix .py, $(FILETYPES)))

wowdump: $(WOWDUMP_TARGETS)

.PRECIOUS: $(OUTDIR_WOWDUMP)/%.py
$(OUTDIR_WOWDUMP)/%.py: $(OUTDIR_PYTHON)/%.py
	cp "$<" "$@"


## The rest of our possible outputs are listed here. Ones commented out
## and marked "NEEDS CAPS" need to have the makefile adjusted to have
## the first letter of the output filenames capitalized, which we still
## need to find a good way to do in a makefile

## construct
OUTDIR_CONSTRUCT ?= $(OUTDIR)/construct
CONSTRUCT_TARGETS = $(addprefix $(OUTDIR_CONSTRUCT)/, $(addsuffix .py, $(FILETYPES)))

construct: $(CONSTRUCT_TARGETS)
ALL_LANGS += construct

.PRECIOUS: $(OUTDIR_CONSTRUCT)/%.py
$(OUTDIR_CONSTRUCT)/%.py: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_CONSTRUCT)
	$(KSY_COMPILER) --outdir $(OUTDIR_CONSTRUCT) --target construct $<


## csharp NEEDS CAPS
# OUTDIR_CSHARP ?= $(OUTDIR)/csharp
# CSHARP_TARGETS = $(addprefix $(OUTDIR_CSHARP)/, $(addsuffix .cs, $(FILETYPES)))

# csharp: $(CSHARP_TARGETS)

# .PRECIOUS: $(OUTDIR_CSHARP)/%.cs
# $(OUTDIR_CSHARP)/%.cs: $(OUTDIR_KSY)/%.ksy
# 	@mkdir -p $(OUTDIR_CSHARP)
# 	$(KSY_COMPILER) --outdir $(OUTDIR_CSHARP) --target csharp $<


## go
OUTDIR_GO ?= $(OUTDIR)/go
GO_TARGETS = $(addprefix $(OUTDIR_GO)/, $(addsuffix .go, $(FILETYPES)))

go: $(GO_TARGETS)
ALL_LANGS += go

.PRECIOUS: $(OUTDIR_GO)/%.go
$(OUTDIR_GO)/%.go: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_GO)
	$(KSY_COMPILER) --outdir $(OUTDIR_GO) --target go $<


## graphviz
OUTDIR_GRAPHVIZ ?= $(OUTDIR)/graphviz
GRAPHVIZ_TARGETS = $(addprefix $(OUTDIR_GRAPHVIZ)/, $(addsuffix .dot, $(FILETYPES)))

graphviz: $(GRAPHVIZ_TARGETS)
ALL_LANGS += graphviz

.PRECIOUS: $(OUTDIR_GRAPHVIZ)/%.dot
$(OUTDIR_GRAPHVIZ)/%.dot: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_GRAPHVIZ)
	$(KSY_COMPILER) --outdir $(OUTDIR_GRAPHVIZ) --target graphviz $<


## svg
OUTDIR_SVG ?= $(OUTDIR)/svg
SVG_TARGETS = $(addprefix $(OUTDIR_SVG)/, $(addsuffix .svg, $(FILETYPES)))

svg: $(SVG_TARGETS)
ALL_LANGS += svg

.PRECIOUS: $(OUTDIR_SVG)/%.svg
$(OUTDIR_SVG)/%.svg: $(OUTDIR_GRAPHVIZ)/%.dot
	@mkdir -p $(OUTDIR_SVG)
	dot -Tsvg $< >$@


## html
OUTDIR_HTML ?= $(OUTDIR)/html
HTML_TARGETS = $(addprefix $(OUTDIR_HTML)/, $(addsuffix .html, $(FILETYPES)))

html: $(HTML_TARGETS)
ALL_LANGS += html

.PRECIOUS: $(OUTDIR_HTML)/%.html
$(OUTDIR_HTML)/%.html: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_HTML)
	$(KSY_COMPILER) --outdir $(OUTDIR_HTML) --target html $<


## java NEEDS CAPS
# OUTDIR_JAVA ?= $(OUTDIR)/java
# JAVA_TARGETS = $(addprefix $(OUTDIR_JAVA)/, $(addsuffix .java, $(FILETYPES)))

# java: $(JAVA_TARGETS)
# ALL_LANGS += java

# .PRECIOUS: $(OUTDIR_JAVA)/%.java
# $(OUTDIR_JAVA)/%.java: $(OUTDIR_KSY)/%.ksy
# 	@mkdir -p $(OUTDIR_JAVA)
# 	$(KSY_COMPILER) --outdir $(OUTDIR_JAVA) --target java $<


## javascript NEEDS CAPS
# OUTDIR_JAVASCRIPT ?= $(OUTDIR)/javascript
# JAVASCRIPT_TARGETS = $(addprefix $(OUTDIR_JAVASCRIPT)/, $(addsuffix .js, $(FILETYPES)))

# javascript: $(JAVASCRIPT_TARGETS)
# ALL_LANGS += javascript

# .PRECIOUS: $(OUTDIR_JAVASCRIPT)/%.js
# $(OUTDIR_JAVASCRIPT)/%.js: $(OUTDIR_KSY)/%.ksy
# 	@mkdir -p $(OUTDIR_JAVASCRIPT)
# 	$(KSY_COMPILER) --outdir $(OUTDIR_JAVASCRIPT) --target javascript $<


## lua
OUTDIR_LUA ?= $(OUTDIR)/lua
LUA_TARGETS = $(addprefix $(OUTDIR_LUA)/, $(addsuffix .lua, $(FILETYPES)))

lua: $(LUA_TARGETS)
ALL_LANGS += lua

.PRECIOUS: $(OUTDIR_LUA)/%.lua
$(OUTDIR_LUA)/%.lua: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_LUA)
	$(KSY_COMPILER) --outdir $(OUTDIR_LUA) --target lua $<


## nim
OUTDIR_NIM ?= $(OUTDIR)/nim
NIM_TARGETS = $(addprefix $(OUTDIR_NIM)/, $(addsuffix .nim, $(FILETYPES)))

nim: $(NIM_TARGETS)
ALL_LANGS += nim

.PRECIOUS: $(OUTDIR_NIM)/%.nim
$(OUTDIR_NIM)/%.nim: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_NIM)
	$(KSY_COMPILER) --outdir $(OUTDIR_NIM) --target nim $<


## perl NEEDS CAPS
# OUTDIR_PERL ?= $(OUTDIR)/perl
# PERL_TARGETS = $(addprefix $(OUTDIR_PERL)/, $(addsuffix .pm, $(FILETYPES)))

# perl: $(PERL_TARGETS)
# ALL_LANGS += perl

# .PRECIOUS: $(OUTDIR_PERL)/%.pm
# $(OUTDIR_PERL)/%.pm: $(OUTDIR_KSY)/%.ksy
# 	@mkdir -p $(OUTDIR_PERL)
# 	$(KSY_COMPILER) --outdir $(OUTDIR_PERL) --target perl $<


## php NEEDS CAPS
# OUTDIR_PHP ?= $(OUTDIR)/php
# PHP_TARGETS = $(addprefix $(OUTDIR_PHP)/, $(addsuffix .php, $(FILETYPES)))

# php: $(PHP_TARGETS)

# .PRECIOUS: $(OUTDIR_PHP)/%.php
# $(OUTDIR_PHP)/%.php: $(OUTDIR_KSY)/%.ksy
# 	@mkdir -p $(OUTDIR_PHP)
# 	$(KSY_COMPILER) --outdir $(OUTDIR_PHP) --target php $<


## ruby
OUTDIR_RUBY ?= $(OUTDIR)/ruby
RUBY_TARGETS = $(addprefix $(OUTDIR_RUBY)/, $(addsuffix .rb, $(FILETYPES)))

ruby: $(RUBY_TARGETS)
ALL_LANGS += ruby

.PRECIOUS: $(OUTDIR_RUBY)/%.rb
$(OUTDIR_RUBY)/%.rb: $(OUTDIR_KSY)/%.ksy
	@mkdir -p $(OUTDIR_RUBY)
	$(KSY_COMPILER) --outdir $(OUTDIR_RUBY) --target ruby $<


## And a target to make all of the above, once we've accumulated them
all_langs: $(ALL_LANGS)


## Other misc stuff

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
