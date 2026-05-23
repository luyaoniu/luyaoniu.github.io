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
    assert "[code](https://github.com/example/code)" in links


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
