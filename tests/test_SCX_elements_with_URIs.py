"""Test for elements mandatory and repeatable."""

from dctap2shex.xclasses import TAPStatementConstraintX

def test_warn_if_propertyID_not_URI():
    """In ShEx, property ID _must_ be an IRI."""
    sc = TAPStatementConstraintX()
    sc.propertyID = "P31"
    sc._elements_taking_IRIs_warn_if_not_IRIs()
    print(sc.sc_warnings)
    print(dict(sc.sc_warnings))
    print(len(dict(sc.sc_warnings)))
    assert len(dict(sc.sc_warnings)) == 1


def test_warn_if_valueShape_not_URI():
    """In ShEx, valueShape _must_ be an IRI."""
    sc = TAPStatementConstraintX()
    sc.propertyID = "wdt:P31"
    sc.valueShape = "Person"
    sc._elements_taking_IRIs_warn_if_not_IRIs()
    print(sc.sc_warnings)
    print(dict(sc.sc_warnings))
    print(len(dict(sc.sc_warnings)))
    assert len(dict(sc.sc_warnings)) == 1
