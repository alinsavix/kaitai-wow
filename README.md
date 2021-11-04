# kaitai-warcraft: WoW Datafile Descriptions and Reading

## What

[Kaitai Struct](https://github.com/kaitai-io/kaitai_struct) is a declarative language that can describe the structure of binary files on disk, and from that create bindings for a multitude of programming languages, allowing them to read those structures without needing to write language-specific code to do so. As of this writing, Kaitai Struct works with C++, C#, Go, Java, JavaScript, Lua, Perl, PHP, Python, Ruby, Rust, and Swift. That's a lot of languages able to read data formats without any extra work!


## Why?

As Asher and I (Alinsa) were working on [WoWbject Importer](https://github.com/ThatAsherGuy/WoWbjectImporter), we kept running into the same problem: There's a lot of information out there about the various World of Warcraft file formats, but that info can sometimes be pretty difficult to get at and parse. Some was somewhat human-readable (lots of the information on wowdev.wiki, for example), but sometimes the best reference was existing, running code, like WowModelViewer, where we had to dig into the code and figure out exactly how it was reading the files.

And after we did all that, we still needed to *implement* code for what we had learned. Code that would just become another chunk of code for someone in the future to need to do archeology on, when they wanted to do things similar to what we were doing (but, perhaps, in a different language).

So, since we had to write something to read these files anyhow (because there was no functional Python library for doing so, and Blender uses Python for addons), we decided we would write the file readers using Kaitai Struct, so that those who come after us will have access to the same information we eventually collected, in a declarative format that could be turned into running code with very little effort on their part -- or just to have as an easy(ish)-to-read reference for the file formats.

...we, of course, know that everyone will just write their own readers for WoW formats *anyhow*, but we can't say we didn't try!


## Who?

Asher and Alinsa!


## Where?

Here!


## When?

Now.


## But when will *then* be *now*?

SOON.


## How (to use, generally)

This document won't go too deeply into how kaitai-struct itself is used, because that's an entire discussion unto itself, but basically: kaitai-struct is a compiler. You feed it a `ksy` file, and tell it what languages you want to use, and it will export a module that can then be used with that language to read files of a given type.

For example, we have the m2 file format defined in a `m2.ksy` file. If we want to use that in python, you would compile it like this:

```
$ kaitai-struct-compiler --target python output/m2.ksy
```

This will (silently, if there are no problems) create an output file for use with your language of choice (in this case, `m2.py` gets created). You can then use that output file in your language. Again in python:

```
from m2 import M2
m2_struct = M2.from_file("spectraltiger.m2")

for vert in m2_struct.model.vertices:
    print(f"found vertex: {vert.pos.x}, {vert.pos.y}, {vert.pos.z}")
```

...which when executed, gives:
```
$ ./test.sh
found vertex: -0.0007805426721461117, 0.29509320855140686, 1.0803431272506714
found vertex: 0.05740489065647125, 0.23616205155849457, 1.2855159044265747
found vertex: 0.0798923596739769, 0.14575813710689545, 1.3968963623046875
found vertex: 0.10975730419158936, -0.00014191120862960815, 1.470015048980713
found vertex: -0.0007805426721461117, 0.29509320855140686, 1.0803431272506714
[...etc...]
```

### How (to use, World of Warcraft (kaitai-wow) specific)

Because of the amount of data structure reuse, and the complexity of the WoW files, our kaitai struct configuration is split into multiple files, spread across the following subdirectories:

* `filetypes`: Top level filetypes, which are generally identified by the extension on the internal WoW filenames. This is where the top-level declarations are made for those files (m2, skin, skel, etc)
* `chunks`: Internally to a given file type, the WoW file format uses 'chunks' identified by four-character identifiers, which declare the type of data stored in a given chunk. The definitions for each of these individual chunks are in this directory, named after their four-character ID.
* `types`: All of the common WoW data types (c4vertex, m2array, and many many others) exist within this directory, ready to be used by filetype and chunk decoders.
* `enums`: Some basic enums that are not filetype-specific, that can potentially be useful

Currently, kaitai-struct does not have a good way to split these configurations into separate files like this (or, more precisely, the way it has available for doing it is... quite awkward to use), so we came up with a simple script (`ksy-merge.py`) for combining needed files together prior to being passed to `kaitai-struct-compiler`. You need to have Python (3.x) and the pyYAML module installed to use this script.

The project ships with a simple `Makefile` that can handle this automatically; if you can't/don't use GNU make or a similar build tool, you can look in the Makefile to see how the commands are intended to be used.

The abbreviated form of what is in the Makefile is, e.g.:

```
$ python3 ./ksy-merge.py filetypes/m2.ksy >output/m2.ksy
$ kaitai-struct-compiler --outdir output --target python output/m2.ksy
```

The generated `m2.ksy` is human readable and if your use case doesn't have you needing to make any changes to the structures, and you just want to read some files, you can just use that combined file in your own build and not even need all the individual piecemeal ksy files.

Alternately, the provided `Makefile` will build the kaitai-struct outputs for a (supported) language of your choice, with just `make <language>`. The supported languages currently are: `construct`, `csharp`, `go`, `graphviz`, `html`, `java`, `javascript`, `lua`, `nim`, `perl`, `php`, `python`, and `ruby`. The output files will be created in `outputs/<language>`.

Please note that we don't personally test any of these outputs, other than `python`; theoretically they are all supported by kaitai-struct and should work correctly, but we make no promises that theory will actually meet practice here.


## wowdump

There is a utility included with this kaitai-wow repo, `wowdump`, which is intended as both an easy way to get at the data in various WoW filetypes (because, well, that's why we made this), and also serves as a bit of a more complex example of the ways that kaitai-struct can be used to read and process data.

You can install this tool with either `make install` or `make localdev`, where it will install the script into your bindir as part of the python module install. You will need a relatively recent version of `pip` for this.

If you use this tool, please don't use it as part of some complex workflow -- it is experimental at best, *very* much a work in progress, and just about every aspect of it can (and will) change without warning. It is also rather crap code in a number of places. Patches to make it less garbage are gladly accepted.

edit: The above is still largely true, but everything *is* getting slowly better and the code is becoming very slightly less crap. There are also now some (relatively good) unit tests, which have a secondary function of also helping to verify the kaitai code itself. You can run `pytest` directly, or `make test` from the root directory.


## Other warnings

This is very much still a work in progress. The data structures defined by the kaitai-struct code can and will change, possibly drastically. We will *try* to call out those breaking changes when they happen, but until we reach a more stable place with the development of this, you may have to regularly update your code when you update your copy of kaitai-wow. Sorry about that. It'll get better.


## Credits

Almost none of the information encapsulated by this library is our original work; as with many things in the computer world (and even moreso the reverse engineering world), we stand on the shoulders of the giants that have come before us. Many thousands of hours have been spent, by tens or hundreds of people, to understand these file structures and how to make them useful.

Some of the work we have referenced, in no particular order:

* [wowdev.wiki](https://wowdev.wiki), and the many many people who have contributed to the almost overwhelming amount of knowledge contained there.
* [https://wow.tools](https://wow.tools/), created and maintained by [Marlamin](https://github.com/Marlamin)
* [WebWowViewerCpp](https://github.com/Deamon87/WebWowViewerCpp) by [Deamon](https://github.com/Deamon87)
* [wow.export](https://github.com/Kruithne/wow.export), courtesy of the eternally patient [Kruithne](https://github.com/Kruithne)
* [Wow Model Viewer](https://wowmodelviewer.net/) by Jeromnimo
* Probably many others we are unintentionally forgetting

Thank all of you for all of the work you have done for this community. :green_heart:
