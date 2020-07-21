from django.db import models


class SchemeSourceType(models.TextChoices):
    coverage = 'coverage', 'Coverage'
    underwritingissue = 'underwritingissue', 'Underwriting Issue'
    exclusion = 'exclusion', 'Exclusion'
    modifier = 'modifier', 'Modifier'
    condition = 'condition', 'Condition'
    coverageterm = 'coverageterm', 'Coverage Term'
    attribute = 'attribute', 'Attribute'
    validationcontext = 'validationcontext', 'Validation Context'
    coverageoptionterm = 'coverageoptionterm', 'Coverage Option Term'
    conditionterm = 'conditionterm', 'Condition Term'
    conditionoptionterm = 'conditionoptionterm', 'Condition Option Term'
    exclusionterm = 'exclusionterm', 'Exclusion Term'
    exclusionoptionterm = 'exclusionoptionterm', 'Exclusion Option Term'
    ratecostcategory = 'ratecostcategory', 'Rate Cost Category'
    eligibility = 'eligibility', 'Eligibility'
    pcf = 'pcf', 'PCF'
    coveragedependency = 'coveragedependency', 'Coverage Dependency'
    coveragesync = 'coveragesync', 'Coverage Sync'
