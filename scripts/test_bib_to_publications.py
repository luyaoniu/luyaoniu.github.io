"""Tests for bib_to_publications: parsing, grouping, link rendering, file emission."""
from pathlib import Path
import pytest

from bib_to_publications import (
    parse_bib,
    group_by_year_and_type,
    render_authors,
    render_links,
    render_publications_markdown,
    render_featured_yaml,
    AUTHOR_NAME,
    clean_title,
    has_equal_contrib,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_bib_reads_entries():
    entries = parse_bib(FIXTURES / "sample.bib")
    assert len(entries) == 3
    keys = {e["ID"] for e in entries}
    assert keys == {"niu2024example", "cheng2023example", "niu2024preprint"}


def test_group_by_year_desc_then_type():
    entries = parse_bib(FIXTURES / "sample.bib")
    grouped = group_by_year_and_type(entries)
    # Outer key: year desc
    assert list(grouped.keys()) == [2024, 2023]
    # 2024 has Journal and Preprint
    assert set(grouped[2024].keys()) == {"Journal", "Preprint"}
    # 2023 has Conference
    assert set(grouped[2023].keys()) == {"Conference"}


def test_render_authors_bolds_target_name():
    rendered = render_authors("Cheng, Shiyu and Niu, Luyao and Other, A.")
    # First name first, last name last; target bolded
    assert rendered == "Shiyu Cheng, **Luyao Niu**, A. Other"


def test_render_authors_marks_equal_contrib():
    rendered = render_authors(
        "Cheng, Shiyu and Niu, Luyao",
        equal_contrib=True,
    )
    # Co-first authors get asterisks
    assert rendered == "Shiyu Cheng\\*, **Luyao Niu**\\*"


def test_render_links_includes_doi_and_code():
    entry = {
        "doi": "10.1109/XYZ.2024.000000",
        "url": "https://arxiv.org/abs/2300.00000",
        "code": "https://github.com/example/code",
    }
    links = render_links(entry)
    assert "[DOI](https://doi.org/10.1109/XYZ.2024.000000)" in links
    assert "[arXiv](https://arxiv.org/abs/2300.00000)" in links
    assert "[Code](https://github.com/example/code)" in links


def test_render_links_arxiv_field_and_order():
    entry = {
        "doi": "10.18653/v1/2024.acl-long.303",
        "arxiv": "2402.08983",
        "code": "https://github.com/uw-nsl/SafeDecoding",
        "project": "https://example.github.io/",
    }
    assert render_links(entry) == (
        "[DOI](https://doi.org/10.18653/v1/2024.acl-long.303)"
        " · [arXiv](https://arxiv.org/abs/2402.08983)"
        " · [Code](https://github.com/uw-nsl/SafeDecoding)"
        " · [Project](https://example.github.io/)"
    )


def test_render_links_non_arxiv_url_is_paper():
    links = render_links({"url": "https://openreview.net/forum?id=abc"})
    assert links == "[Paper](https://openreview.net/forum?id=abc)"


def test_render_links_empty_when_no_fields():
    assert render_links({}) == ""


def test_render_publications_markdown_has_year_headings_and_legend():
    entries = parse_bib(FIXTURES / "sample.bib")
    md = render_publications_markdown(entries)
    assert "## 2024" in md
    assert "## 2023" in md
    assert "### Journal" in md
    assert "### Conference" in md
    assert "### Preprint" in md
    # Legend appears because cheng2023example has equal_contrib
    assert "* indicates equal contribution" in md
    # Author bolding present
    assert "**Luyao Niu**" in md
    # Front matter present
    assert md.startswith("---\n")
    assert "permalink: /publications/" in md


def test_render_featured_yaml_only_includes_featured():
    entries = parse_bib(FIXTURES / "sample.bib")
    yaml_text = render_featured_yaml(entries)
    # Only niu2024example has featured=true
    assert "Example Journal Paper" in yaml_text
    assert "Example Conference Paper" not in yaml_text
    assert "Example Preprint" not in yaml_text


def test_render_publications_markdown_is_idempotent():
    entries = parse_bib(FIXTURES / "sample.bib")
    first = render_publications_markdown(entries)
    second = render_publications_markdown(entries)
    assert first == second


def test_render_authors_inline_equal_contrib_markers():
    # Per-author markers in the .bib (e.g. "Jiang$^*$, Fengqing" or "Niu*, Luyao")
    rendered = render_authors(
        "Jiang$^*$, Fengqing and Xu*, Zhangchen and Niu$^*$, Luyao and Li, Bo"
    )
    assert rendered == "Fengqing Jiang\\*, Zhangchen Xu\\*, **Luyao Niu**\\*, Bo Li"


def test_has_equal_contrib_detects_inline_markers():
    assert has_equal_contrib({"author": "Jiang$^*$, Fengqing and Li, Bo"})
    assert has_equal_contrib({"equal_contrib": "true", "author": "A, B"})
    assert not has_equal_contrib({"author": "Li, Bo and Niu, Luyao"})


def test_clean_title_strips_braces():
    assert clean_title("ArtPrompt: {ASCII} Art-based {LLMs}") == "ArtPrompt: ASCII Art-based LLMs"


def test_publication_line_renders_note():
    entry = {
        "ENTRYTYPE": "inproceedings",
        "author": "Niu, Luyao",
        "title": "A Paper",
        "booktitle": "ACL",
        "year": "2025",
        "note": "Oral Presentation",
    }
    md = render_publications_markdown([entry])
    assert '- **Luyao Niu**. "A Paper." *ACL*, 2025. **Oral Presentation.**' in md
    assert "equal contribution" not in md


def test_render_authors_others_becomes_et_al():
    assert render_authors("Li, Bo and Niu, Luyao and others") == "Bo Li, **Luyao Niu**, et al."


def test_question_mark_title_gets_no_extra_period():
    entry = {"ENTRYTYPE": "inproceedings", "author": "Li, Bo", "title": "Can it?", "booktitle": "X", "year": "2026"}
    assert '"Can it?"' in render_publications_markdown([entry])


def test_venue_braces_are_stripped():
    entry = {"ENTRYTYPE": "inproceedings", "author": "Li, Bo", "title": "T", "booktitle": "Conf, {IJCAI-23}", "year": "2023"}
    assert "*Conf, IJCAI-23*" in render_publications_markdown([entry])


def test_publications_page_redirects_legacy_url():
    md = render_publications_markdown(parse_bib(FIXTURES / "sample.bib"))
    front_matter = md.split("---")[1]
    assert "redirect_from:\n  - /publications.html" in front_matter
