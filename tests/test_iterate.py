"""@@@"""

# Schema attributes
def get_schema_attributes(schema):
    """@@@"""
    return {attrib for attrib in schema}

def test_get_schema_attributes():
    """@@@"""
    attributes = get_schema_attributes(SCHEMA)
    assert "@context" in attributes
    assert "shapes" in attributes
    assert "type" in attributes
    assert isinstance(SCHEMA["@context"], str)
    assert isinstance(SCHEMA["shapes"], list)
    assert isinstance(SCHEMA["type"], str)

# Shape list
def get_shape_list(schema):
    """@@@"""
    return [shape for shape in schema["shapes"]]

def test_get_shape_list():
    """@@@"""
    shape_list = get_shape_list(SCHEMA)
    assert len(shape_list) == 2
    for item in shape_list:
        assert isinstance(item, dict)

def get_shape_attributes(schema):
    """@@@"""
    shape_attributes = list()
    for shape in schema["shapes"]:
        for key in shape:
            shape_attributes.append(key)
    return set(shape_attributes)

def test_get_shape_attributes():
    """@@@"""
    shapes = SCHEMA["shapes"]
    shape_attributes = get_shape_attributes(SCHEMA)
    assert "annotations" in shape_attributes
    assert "expression" in shape_attributes
    assert "id" in shape_attributes
    assert "type" in shape_attributes
    for shape in shapes:
        if shape.get("annotations"):
            assert isinstance(shape["annotations"], list)
        assert isinstance(shape["expression"], dict)
        assert isinstance(shape["id"], str)
        assert isinstance(shape["type"], str)

def get_annotation_attributes(schema):
    """@@@"""
    shapes = SCHEMA["shapes"]
    annotation_attributes = list()
    for shape in shapes:
        if shape.get("annotations"):
            for annotation in shape.get("annotations"):
                for key in annotation:
                    annotation_attributes.append(key)
    return set(annotation_attributes)

def test_get_annotation_attributes():
    """@@@"""
    expected_annotation_attributes = {'object', 'predicate', 'type'}
    annotation_attributes = get_annotation_attributes(SCHEMA)
    assert get_annotation_attributes(SCHEMA) == expected_annotation_attributes
    assert "type" in annotation_attributes
    assert "predicate" in annotation_attributes
    assert "object" in annotation_attributes
    shapes = SCHEMA["shapes"]
    for shape in shapes:
        if shape.get("annotations"):
            for annotation in shape.get("annotations"):
                assert isinstance(annotation.get("type"), str)
                assert isinstance(annotation.get("predicate"), str)
                assert isinstance(annotation.get("object"), dict)

def get_eachof_expression_attributes(schema):
    """Gets attributes from items of list "expressions" in object of type "EachOf"."""
    shapes = SCHEMA["shapes"]
    expression_attributes = list()
    for shape in shapes:
        if shape.get("expression"):
            expression = shape.get("expression")
            if expression.get("type") == "EachOf":
                for eachof_expression in expression["expressions"]:
                    for key in eachof_expression:
                        expression_attributes.append(key)
    return set(expression_attributes)

def test_get_eachof_expression_attributes():
    """@@@"""
    expected_expression_attributes = {'valueExpr', 'predicate', 'type', 'min', 'max', 'annotations'}
    expression_attributes = get_eachof_expression_attributes(SCHEMA)
    assert get_eachof_expression_attributes(SCHEMA) == expected_expression_attributes
    assert get_eachof_expression_attributes(SCHEMA) == expression_attributes
    assert "type" in expression_attributes
    assert "predicate" in expression_attributes
    assert "valueExpr" in expression_attributes
    assert "min" in expression_attributes
    assert "max" in expression_attributes
    assert "annotations" in expression_attributes
    shapes = SCHEMA["shapes"]
    for shape in shapes:
        if shape.get("expressions"):
            expression = shape.get("expression")
            if expression.get("type") == "EachOf":
                for eachof_expression in expression["expressions"]:
                    for key in eachof_expression:
                        assert isinstance(expression.get("type"), str)
                        assert isinstance(expression.get("predicate"), str)
                        assert isinstance(expression.get("min"), str)
                        assert isinstance(expression.get("max"), str)
                        assert isinstance(expression.get("valueExpr"), list)
                        assert isinstance(expression.get("annotations"), list)













SCHEMA = {
  "type": "Schema",
  "shapes": [
    {
      "type": "Shape",
      "id": "http://ex.example/#author",
      "expression": {
        "type": "TripleConstraint",
        "predicate": "http://ex.example/#nickname",
        "valueExpr": {
          "type": "NodeConstraint",
          "pattern": "John*"
        }
      }
    },
    {
      "type": "Shape",
      "id": "http://ex.example/#book",
      "expression": {
        "type": "EachOf",
        "expressions": [
          {
            "type": "TripleConstraint",
            "predicate": "http://purl.org/dc/terms/creator",
            "valueExpr": {
              "type": "ShapeAnd",
              "shapeExprs": [
                {
                  "type": "NodeConstraint",
                  "nodeKind": "iri"
                },
                "http://ex.example/#author"
              ]
            },
            "min": 1,
            "max": 1,
            "annotations": [
              {
                "type": "Annotation",
                "predicate": "http://www.w3.org/2000/01/rdf-schema#label",
                "object": {
                  "value": "Author"
                }
              },
              {
                "type": "Annotation",
                "predicate": "http://www.w3.org/2000/01/rdf-schema#comment",
                "object": {
                  "value": "Writer of the book"
                }
              }
            ]
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://purl.org/dc/terms/date",
            "valueExpr": {
              "type": "NodeConstraint",
              "datatype": "http://www.w3.org/2001/XMLSchema#date"
            }
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://purl.org/dc/terms/subject",
            "valueExpr": {
              "type": "NodeConstraint",
              "values": [
                {
                  "type": "IriStem",
                  "stem": "https://id.loc.gov"
                }
              ]
            }
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://ex.example/#status",
            "valueExpr": {
              "type": "NodeConstraint",
              "values": [
                {
                  "value": "confidential"
                }
              ]
            }
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://ex.example/#description",
            "valueExpr": {
              "type": "NodeConstraint",
              "values": [
                {
                  "type": "Language",
                  "languageTag": "fr"
                },
                {
                  "type": "Language",
                  "languageTag": "it"
                },
                {
                  "type": "Language",
                  "languageTag": "en"
                }
              ]
            },
            "min": 1,
            "max": 1
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://ex.example/#colors",
            "valueExpr": {
              "type": "NodeConstraint",
              "values": [
                {
                  "value": "blue"
                },
                {
                  "value": "green"
                }
              ]
            }
          },
        ]
      },
      "annotations": [
        {
          "type": "Annotation",
          "predicate": "http://www.w3.org/2000/01/rdf-schema#label",
          "object": {
            "value": "Book"
          }
        }
      ]
    }
  ],
  "@context": "http://www.w3.org/ns/shex.jsonld"
}
