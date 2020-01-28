---

<!-- html Comments are scattered throughout --> 
<!-- first section is material that should stay in _materials -->
<!-- remainder is material that should live in REMARK/[name] -->
name: LiqConstr
type: replication <!-- Not sure what this controls, distinctly from tags --> 
testfile: do_min.py <!-- Name of the file in the root directory to test, if different from name.py; for Travis etc-->

is_notebook: false <!-- I think we want to insist that there must ALWAYS be an (eponymous) notebook -->
published:

<!-- The following are relevant only for REMARKs where there is a submodule that contains the paper and code -->
<!-- They should be constructed from the info in the git submodule config files -->

authors:
  - Christopher Carroll
tags:
  - Replication

<!-- The following are relevant only for REMARKs where there is a submodule that contains the paper and code -->
<!-- They should be constructed from the info in the git submodule config files, rather than by hand -->

location_url: https://github.com/llorracc/LiqConstr/tree/01253c2e57b2278c41b6a9a01e61a666edcc5239
github_user: llorracc
github_repository: LiqConstr

<!-- These should rarely be present, and if not present should take their default values (master, etc) -->
github_branch: <!-- default, of course, is master; my sense is that this might be mainly useful for referencing PR's -->
github_path: <!-- like, "notebooks" for DemARK and "REMARKs" for REMARK?  Why did it not need to be "REMARKs" for this entry? -->

<!-- Content that should be in the REMARK's own directory --> 
authors: [name]-REMARK-Authors.md <!-- One author per line; they can include a link []() if they like -->
authors: [name]-REMARK-Authors.md <!-- One author per line; they can include a link []() if they like -->
bibtex_reference: [name]-Original-Paper.bib <!-- Bibliographical entry for the paper being reproduced; ideally sourced by Zotero -->
title: [name]-REMARK-title.md <!-- This probably should replace "summary" --> 
url_to_original_being_REMARKed: [name]-Original-Paper.URL <!-- On macs such files have the .webloc extension; but https://en.wikipedia.org/wiki/Shortcut_(computing) says that .URL is a standard for Windows -->
summary: [name]-One-Sentence-Summary.md <!-- This should contain the info that comes below the triple-dashes --- below --> 

---

Liquidity Constraints and Precautionary Saving <!-- This should be sourced from the [name]-REMARK-title.md file --> 

<!-- The material below should be sourced from the [name]-One-Sentence-Description.md file -->

This paper shows that liquidity constraints and precautionary saving are closely related to each other, since both can be thought of is "counterclockwise concavifications" of the consumption function.
