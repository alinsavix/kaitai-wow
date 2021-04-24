# This is a shitty makefile. Don't use it as a model for anything
KSY_COMPILER ?= kaitai-struct-compiler
KSY_MERGE=python3 ./ksy-merge.py
TARGETS ?= m2.py   # also available: m2.svg

all: $(TARGETS)

test: $(TARGETS)
	./test.py

# We're just going to force it to rebuild everything every time, so we don't
# have to deal with the complexity of having a way to dynamically track
# included files as dependencies
.PRECIOUS: %-merged.ksy
%-merged.ksy: %.ksy FORCE
	$(KSY_MERGE) $< >$@

%.py: %-merged.ksy
	$(KSY_COMPILER) --target python $<

%.svg: %.dot
	dot -Tsvg $< >$@

%.dot: %-merged.ksy
	$(KSY_COMPILER) --target graphviz $<

clean: FORCE
	rm $(TARGETS)
	rm *-merged.ksy

FORCE:
