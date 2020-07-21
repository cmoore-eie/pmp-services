from django.db import models


class AttributeValueType(models.TextChoices):
    stringType = "string", "String"
    objectType = "object", "Object"
    calculatedType = "calculated", "Calculated"
    otherType = "other", "Other"
    listType = "list", "List"
    string_multilineType = "string_multiline", "String Multi Line"
    booleanType = "boolean", "Boolean"
    integerType = "integer", "Integer"
    integer_rangeType = "integer_range", "Integer Range"
    integer_setType = "integer_set", "Integer Set"
    money_rangeType = "money_range", "Money Range"
    money_setType = "money_set", "Money Set"
    longType = "long", "Long"
    decimalType = "decimal", "Decimal"
    dateType = "date", "Date"
    code = "money", "Money"
    typekeyType = "typekey", "Typekey"
    optionType = "option", "Option"
    labelType = "label", "Label"
    locationType = "location", "Location"
    money_usdType = "money_usd", "Money USD"
    money_eurType = "money_eur", "Money EUR"
    money_gbpType = "money_gbp", "Money GBP"
    percentType = "percent", "Percentage"
    percentdecType = "percentdec", "Percentage Decimal"
    yearType = "year", "Percentage"
    addressType = "address", "Address"
    afpfunctionType = "afpfunction", "AFP Function"
