# Metadata Required for Auto Index

This document is for working out a system whereby certain kinds of materials (DemARKs; REMARKs) can be automatically indexed by econ-ark.org using metadata that resides with the material itself.

Desiderata:
1. We should have the same mechanism for DemARK and REMARK material
1. That mechanism should involve the following kinds of metadata:
    1.  Prohibited (at least for DemARK and REMARK items):
        * The name of the material itself (because this should never be different from the filename)
        * The location (DemARK; REMARK; examples)
	1. Strongly recommended (or should these be required?)
        * Title (like "Diamond OLG Model")
            * If it does not exist, the first line beginning with # will be treated as the titel
        * Author(s) of the material (name and GitHub ID(s))
	1. Recommended:
	    * tags
		* type (demonstration, etc)
		* summary: (one sentence summary)
	1. Optional:
	    * abstract
		* branch
1. A key question is where the metadata should reside. Options:
   1. A standalone markdown file with a name corresponding to the material
   1. Within the metadata of a Jupyter notebook
	  * This would require that an eponymous Jupyter notebook at its root
	  * At the moment, some of the eponymous notebooks are NOT at the root:
	      * Often, for example, in Code/Python
	  * Solutions:
	      1. Move the eponymous notebooks from Code/Python to the root
		  1. The notebook at the root could be a stub pointing to the real notebook
	  * CDC: I prefer the first solution because
        1. It is not uncommon for secure systems (like at central banks) to prohibit code from having any access to any parent directory to the directory in which the code runs
        1. This means that if the notebook were in (REMARK root)/Code/Python, it could not write to, say, (REMARK root)/Figures

I'd propose that we have somewhat different conventions for metadata for "published" REMARKs, "unpublished" REMARKs, and DemARKs:

1. DemARKs and "unpublished" REMARKs are the low bar
   * The system should work for a DemARK even if no metadata are available
   * Title can be taken from the first cell beginning with #
   * If there is a cell named ### Authors, the authors can be taken from that cell
   * We would *prefer* the metadata to exist rather than using these defaults
1. "Published" REMARKs would REQUIRE a minimal set of Metadata
   * These could be added by submitting a web form that lives on econ-ark.org
   * The web form would require the user to fill in all required fields and would permit the filling in of optional fields
   * The required fields should contain sufficient information to construct a CFF machine-readable reference to the REMARK
       * One element of this should be a doi for the REMARK
       * This should be obtained by us, automatically
       * The "publication date" would correspond to the day on which the doi was obtained
   * For REMARKs that are replications or reproductions of other work, there would also be required fields for the information about the source work being reproduced
       * Again, the minimal info for constructing a well-behaved CFF reference: Names of the authors, place and date of publication, and a doi (e.g.)
