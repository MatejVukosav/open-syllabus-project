

from osp.institutions.models import Institution_Document


def test_institution(add_doc, add_institution, add_citation):

    """
    Citation#institution should provide the document's institution.
    """

    document = add_doc()

    institution = add_institution()

    # Link doc -> inst.
    Institution_Document.create(
        institution=institution,
        document=document,
    )

    citation = add_citation(document=document)

    assert citation.institution.id == institution.id
